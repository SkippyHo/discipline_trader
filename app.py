import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from board_game import generate_multiple_boards

import streamlit as st

# Set page config with browser tab title and wide layout
st.set_page_config(page_title="Discipline Trader", layout="wide")

# Render the page title at the top of the content
st.title("Discipline Trader")


st.markdown(
    """
    <style>
    /* This targets the direct child divs in the horizontal block */
    div[data-testid="stHorizontalBlock"] > div {
        padding-right: 20px;  /* Adjust this value as needed */
    }
    /* Optionally remove padding on the last column */
    div[data-testid="stHorizontalBlock"] > div:last-child {
        padding-right: 0;
    }
    /* Table styling */
    table.styled-table {
        width: 100%;
        table-layout: fixed;
    }
    table th, table td {
        min-width: 60px;
        text-align: center;
    }
    table td.negative {
        color: red;
    }
    table th:nth-child(7),
    table td:nth-child(7),
    table th:nth-child(8),
    table td:nth-child(8) {
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# Sidebar inputs (unchanged)
st.sidebar.header('Variables')
n_rounds = st.sidebar.number_input('回合數:', min_value=1, value=3)
n_trails = st.sidebar.number_input('每日交易次數:', min_value=1, value=5, disabled=True, help='This option is fixed and hidden from user')
pr_ratio = st.sidebar.number_input('賺賠比:', min_value=0.1, value=3.0)
#p = st.sidebar.slider('勝率:', min_value=0.01, max_value=0.99, value=0.4, step=0.01, format="%.2f")
#p_range = st.sidebar.slider(
#    '勝率範圍:',
#    min_value=0.01,
#    max_value=0.99,
#    value=(0.3, 0.5),  # Default lower and upper bounds
#    step=0.01,
#    format="%.2f"
#)
lower_p = st.sidebar.number_input(
    '最低勝率:',
    min_value=0.01,
    max_value=0.99,
    value=0.3,
    step=0.01,
    format="%.2f"
)
upper_p = st.sidebar.number_input(
    '最高勝率:',
    min_value=0.01,
    max_value=0.99,
    value=0.4,
    step=0.01,
    format="%.2f"
)


stop_threshold = st.sidebar.number_input('每日最大停損次數:', min_value=0, value=2)

if st.sidebar.button('Generate Board'):
    board_df  = generate_multiple_boards(n_rounds, n_trails, pr_ratio, (lower_p, upper_p), stop_threshold)
    
    st.header('Generated Board')
    
    # Create two columns with custom ratio.
    col1, col2 = st.columns([5,5], gap="small")
    
    with col1:
        st.subheader("Board Table")
        html_table = (
            board_df.style
            .map(lambda x: "color: red;" if isinstance(x, (int, float)) and x < 0 else "")
            .format({"勝率": "{:.3f}"})  # Apply three-decimal format only to the '勝率' column
            .set_properties(subset=['每日損益'], **{'background-color': 'rgba(255,165,0,0.5)'})
            .set_properties(subset=['累積損益'], **{'background-color': 'rgba(255,255,0,0.5)'})
            .to_html(
                index=True,
                classes='dataframe styled-table',
                render_links=True,
                float_format='%.2f',
                sparsify=False,
                escape=False
            )
        )
        st.markdown(html_table, unsafe_allow_html=True)
        
    with col2:
        st.subheader("Accumulated P/L Chart")
        accumulated_pl = board_df['累積損益'].tolist()
        winning_rate = board_df['勝率'].tolist()
        
        fig, ax = plt.subplots(figsize=(9, 5))
        ax.plot(accumulated_pl, label='Accumulated P/L (left)', marker="o", linewidth = 2)
        ax1 = ax.twinx()
        ax1.scatter(x = range(len(winning_rate)), y = winning_rate, label = "Winning percentage (right)", color = 'orange', linewidth = 2)
        ax1.set_ylabel('winning percentage')
        ax.set_xlabel('Day')
        ax.set_ylabel('Accumulated P/L')
        ax.set_ylim(min(accumulated_pl)-3, max(accumulated_pl)+3)
        ax1.set_ylim(lower_p-0.1, upper_p+0.1)
        
        # Combine legend entries from both axes
        handles1, labels1 = ax.get_legend_handles_labels()
        handles2, labels2 = ax1.get_legend_handles_labels()
        handles = handles1 + handles2
        labels = labels1 + labels2

        ax.legend(handles, labels)

        st.pyplot(fig)
else:
    st.write("Click 'Generate Board' to generate the board game and chart.")
