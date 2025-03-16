import numpy as np
import pandas as pd

def generate_board(n_trails, pr_ratio=3, p=0.4, stop_threshold=2):
    """
    Generates a board game matrix as a Pandas DataFrame with integer values, based on the specified rules.
    Fixed to 5 iterations (rows).

    Args:
        n_trails (int): Number of columns (trials).
        pr_ratio (float): The positive value to sample from. Defaults to 3.
        p (float, optional): Probability of sampling pr_ratio. Defaults to 0.4.
        stop_threshold (int, optional): Threshold for -1s to stop the game. Defaults to 2.

    Returns:
        pandas.DataFrame: The generated board game matrix as a DataFrame with integer values.
    """
    n_iterations = 5  # Fixed number of iterations (rows)
    board = np.zeros((n_iterations, n_trails))
    for i in range(n_iterations):
        stop_count = 0
        for j in range(n_trails):
            if stop_count >= stop_threshold:
                board[i, j] = 0
            else:
                sample = np.random.choice([-1, pr_ratio], p=[1-p, p])
                board[i, j] = sample
                if sample == -1:
                    stop_count += 1
    
    # Convert numpy array to pandas DataFrame with column names
    columns = [f'trail{j+1}' for j in range(n_trails)]
    df_board = pd.DataFrame(board, columns=columns)
    # Add total gain for each round
    df_board['total'] = df_board[columns].sum(axis = 1)
    # Add accumulate gain
    df_board['total_acc'] = df_board['total'].cumsum()
    return df_board.astype(int)

def generate_multiple_boards(n_rounds, n_trails, pr_ratio=3, p_range=(0.3, 0.4), stop_threshold=2):
    """
    Generates multiple board game matrices, concatenates them, and calculates accumulated total gain.

    Args:
        n_rounds (int): Number of rounds (number of boards to generate).
        n_trails (int): Number of columns (trials) for each board.
        pr_ratio (float): The positive value to sample from. Defaults to 3.
        p_range (tuple of float, optional): Probability of sampling pr_ratio. Defaults to (0.2, 0.4).
        stop_threshold (int, optional): Threshold for -1s to stop the game. Defaults to 2.

    Returns:
        pandas.DataFrame: Concatenated board game matrix with accumulated total gain.
    """
    board_list = []
    p_list = []
    for _ in range(n_rounds):
        p = np.round(np.random.uniform(min(p_range), max(p_range)), 3)
        board = generate_board(n_trails, pr_ratio, p, stop_threshold)
        board_list.append(board)
        p_list.append([p for _ in range(len(board))])
    
    concatenated_board = pd.concat(board_list, ignore_index=True)
    
    # Recalculate total and total_acc for the concatenated board
    columns = [col for col in concatenated_board.columns if col.startswith('trail')]
    concatenated_board['total'] = concatenated_board[columns].sum(axis=1)
    concatenated_board['total_acc'] = concatenated_board['total'].cumsum()
    concatenated_board = concatenated_board.astype(int)
    concatenated_board['winning_rate'] = sum(p_list, []) # flatten the nested list
    
    # turn all columns into capital letters
    concatenated_board.columns = [col.upper() for col in concatenated_board.columns]
    # rename 'total' to '每日損益' and 'total_acc' into ‘累積損益’
    concatenated_board = concatenated_board.rename(columns={'TOTAL': '每日損益', 'TOTAL_ACC': '累積損益', 'WINNING_RATE': '勝率'})
    concatenated_board.index = concatenated_board.index + 1
    return concatenated_board


if __name__ == '__main__':
    n_trails = 5
    board_df = generate_board(n_trails, pr_ratio=2)
    print("Single Board:")
    print(board_df)

    n_rounds = 3
    multiple_boards_df = generate_multiple_boards(n_rounds, n_trails, pr_ratio=2)
    print("\nMultiple Boards (concatenated):")
    print(multiple_boards_df)