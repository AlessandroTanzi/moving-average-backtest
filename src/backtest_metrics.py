import numpy as np


def calculate_cumulative_returns(returns):
    """
    Calculate cumulative returns from daily returns.
    """
    cumulative_returns = (1 + returns).cumprod()
    return cumulative_returns


def calculate_sharpe_ratio(returns, risk_free_rate=0):
    """
    Calculate annualized Sharpe Ratio.
    """
    excess_returns = returns - risk_free_rate / 252
    sharpe_ratio = (excess_returns.mean() / excess_returns.std()) * np.sqrt(252)
    return sharpe_ratio


def calculate_drawdown(cumulative_returns):
    """
    Calculate drawdown from cumulative returns.
    """
    running_max = cumulative_returns.cummax()
    drawdown = (cumulative_returns / running_max) - 1
    return drawdown


def calculate_max_drawdown(drawdown):
    """
    Calculate maximum drawdown.
    """
    max_drawdown = drawdown.min()
    return max_drawdown
