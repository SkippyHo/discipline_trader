# Discipline Trader

This is a Streamlit application that simulates a trading board game. It allows users to generate a board with profit/loss outcomes based on specified parameters and visualize the accumulated profit/loss and winning rate.

## Features

- **Interactive Board Generation:** Users can specify the number of rounds, profit/loss ratio, winning probability range, and daily stop-loss threshold to generate a customized trading board.
- **Data Visualization:** The application displays the generated board in a table format and provides an interactive chart visualizing the accumulated profit/loss and winning rate over the rounds.
- **Customizable Parameters:** Users can adjust various parameters via the sidebar to explore different trading scenarios.

## How to Use

1.  **Sidebar Inputs:**
    - **回合數 (Number of Rounds):**  Specify the number of rounds for the simulation.
    - **每日交易次數 (Daily Trades):**  Fixed at 5 trades per day (not adjustable by the user).
    - **賺賠比 (Profit/Loss Ratio):**  Set the ratio of profit to loss for winning trades.
    - **最低勝率 (Minimum Winning Rate):**  Set the lower bound for the winning probability range.
    - **最高勝率 (Maximum Winning Rate):** Set the upper bound for the winning probability range.
    - **每日最大停損次數 (Daily Stop-Loss Threshold):** Set the maximum number of losses allowed per day before stopping trading for the day.

2.  **Generate Board:**
    - Click the "Generate Board" button in the sidebar to generate the trading board and chart based on the specified parameters.
    - The generated board table and accumulated P/L chart will be displayed in the main area.

## Deployment to Vercel

This application is configured for deployment to Vercel. You can deploy it using either the Vercel CLI or by connecting your Bitbucket repository to Vercel.

### Deployment via Vercel CLI

1.  **Install Vercel CLI:**
    If you haven't already, install the Vercel CLI globally using npm:
    ```bash
    npm install -g vercel
    ```

2.  **Deploy:**
    Navigate to your project directory in the terminal and run:
    ```bash
    vercel
    ```
    Follow the prompts to deploy your application.

### Deployment via Bitbucket

1.  **Create a Bitbucket Repository:**
    Create a new repository on Bitbucket and push your project files to it.

2.  **Create a New Project on Vercel:**
    - Go to your Vercel dashboard and click "Add New Project".
    - Choose "Deploy from Git Repository" and select "Bitbucket".
    - Authorize Vercel to access your Bitbucket account if needed.
    - Select your repository and click "Import".
    - Configure project settings (defaults should work).
    - Click "Deploy".

## Dependencies

- streamlit
- pandas
- numpy
- matplotlib

These dependencies are listed in `requirements.txt`. Vercel will automatically install them during deployment.

## Project Files

- `app.py`:  Main Streamlit application file.
- `board_game.py`: Python module containing the logic for generating the board game.
- `vercel.json`: Vercel configuration file for deployment settings.
- `requirements.txt`: Lists Python dependencies.
- `README.md`: Project documentation (this file).
- `.gitignore`: Specifies intentionally untracked files that Git should ignore.

---

Enjoy simulating your trading strategies with Discipline Trader!