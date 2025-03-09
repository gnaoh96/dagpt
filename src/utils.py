import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

def exec_plt_code(code: str, df: pd.DataFrame):
    """
        Execute the passing code to plot figure

    Args:
        code (str): action string (containing plt code)
        df (pd.DataFrame): dataframe

    Returns:
        _type_: plt figure 
    """
    try:
        local_vars = {"plt": plt, "df": df}
        compilied_code = compile(code, "<string>", "exec")
        exec(compilied_code, globals(), local_vars)

        return plt.gcf()

    except Exception as e:
        st.error(f"Error executing plat code: {e}")
        return None
