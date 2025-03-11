"""
Financial Analysis System

This module provides functions for analyzing investment portfolios, 
assessing risk, tracking budgets, and generating financial reports.
"""

# Sample data for demonstration
def get_sample_portfolio():
    """Return sample portfolio data for demonstration."""
    return [
        {"ticker": "AAPL", "shares": 10, "purchase_price": 150.0, "current_price": 175.0, "sector": "Technology"},
        {"ticker": "MSFT", "shares": 5, "purchase_price": 250.0, "current_price": 280.0, "sector": "Technology"},
        {"ticker": "JNJ", "shares": 8, "purchase_price": 160.0, "current_price": 155.0, "sector": "Healthcare"},
        {"ticker": "PG", "shares": 12, "purchase_price": 140.0, "current_price": 145.0, "sector": "Consumer Staples"},
        {"ticker": "JPM", "shares": 7, "purchase_price": 130.0, "current_price": 150.0, "sector": "Financial Services"}
    ]

def get_sample_transactions():
    """Return sample transaction data for demonstration."""
    return [
        {"date": "2023-01-05", "type": "income", "amount": 3000.00, "category": "Salary"},
        {"date": "2023-01-10", "type": "expense", "amount": 1200.00, "category": "Rent"},
        {"date": "2023-01-15", "type": "expense", "amount": 200.00, "category": "Utilities"},
        {"date": "2023-01-20", "type": "expense", "amount": 350.00, "category": "Groceries"},
        {"date": "2023-01-25", "type": "expense", "amount": 80.00, "category": "Transportation"},
        {"date": "2023-02-05", "type": "income", "amount": 3000.00, "category": "Salary"},
        {"date": "2023-02-10", "type": "expense", "amount": 1200.00, "category": "Rent"},
        {"date": "2023-02-18", "type": "expense", "amount": 180.00, "category": "Utilities"},
        {"date": "2023-02-22", "type": "expense", "amount": 320.00, "category": "Groceries"},
        {"date": "2023-02-27", "type": "expense", "amount": 95.00, "category": "Entertainment"}
    ]

def get_sample_financial_goals():
    """Return sample financial goals for demonstration."""
    return [
        {"name": "Emergency Fund", "target_amount": 10000, "deadline": "2023-12-31", "priority": "high", "current_amount": 6500},
        {"name": "Vacation", "target_amount": 3000, "deadline": "2023-08-31", "priority": "medium", "current_amount": 1500},
        {"name": "Down Payment", "target_amount": 50000, "deadline": "2025-06-30", "priority": "high", "current_amount": 15000}
    ]

def get_sample_market_data():
    """Return sample market data for demonstration."""
    return {
        "risk_free_rate": 0.03,
        "market_return": 0.08,
        "volatility": 0.15,
        "historical_prices": {
            "AAPL": [150, 155, 153, 160, 158, 165, 175],
            "MSFT": [240, 245, 250, 255, 260, 270, 280],
            "JNJ": [165, 163, 160, 158, 155, 157, 155],
            "PG": [138, 140, 139, 142, 144, 143, 145],
            "JPM": [125, 130, 135, 140, 145, 148, 150]
        }
    }

# Portfolio Analysis Functions
def calculate_portfolio_value(stocks):
    """
    Calculate the current total value of a stock portfolio.
    
    Args:
        stocks (list): List of stock dictionaries
        
    Returns:
        float: Total current value of the portfolio
    """
    # TODO: Implement this function to calculate total portfolio value
    pass

def analyze_portfolio_performance(stocks, *, period="1y"):
    """
    Analyze the performance of a portfolio over a specified period.
    Demonstrates keyword-only arguments.
    
    Args:
        stocks (list): List of stock dictionaries
        period (str, optional): Time period for analysis. Defaults to "1y".
                                Must be one of: "1m", "3m", "6m", "1y", "5y"
    
    Returns:
        dict: Performance metrics including total gain/loss, percentage, best/worst performers
    """
    # TODO: Implement portfolio performance analysis with keyword-only parameters
    pass

def calculate_sector_allocation(stocks):
    """
    Calculate the percentage allocation of a portfolio by sector.
    
    Args:
        stocks (list): List of stock dictionaries
    
    Returns:
        dict: Sector allocation percentages and values
    """
    # TODO: Implement sector allocation calculation
    pass

def create_diversification_calculator(risk_profile):
    """
    Create a function that calculates recommended diversification based on risk profile.
    Demonstrates closure technique and nested functions.
    
    Args:
        risk_profile (str): Investor risk profile ("conservative", "moderate", or "aggressive")
    
    Returns:
        function: A function that calculates recommended allocation
    """
    # TODO: Implement nested function and closure for diversification calculation
    # Don't forget to use nonlocal variables in the inner function
    pass

# Risk Assessment Functions
def calculate_volatility(historical_prices):
    """
    Calculate the volatility (standard deviation) of stock prices.
    
    Args:
        historical_prices (list): List of historical prices
        
    Returns:
        float: Volatility as standard deviation
    """
    # TODO: Implement volatility calculation
    pass

def calculate_risk_metrics(returns, risk_free_rate=0.03):
    """
    Calculate risk metrics including Sharpe Ratio.
    Demonstrates default parameter values.
    
    Args:
        returns (list): List of historical returns
        risk_free_rate (float, optional): Risk-free interest rate. Defaults to 0.03.
        
    Returns:
        tuple: (average_return, volatility, sharpe_ratio)
    """
    # TODO: Implement risk metrics calculation with default parameter
    pass

def generate_risk_report(**options):
    """
    Generate a risk assessment report with various options.
    Demonstrates **kwargs usage.
    
    Args:
        **options: Variable keyword arguments including:
                  - include_volatility (bool): Include volatility metrics
                  - include_sharpe (bool): Include Sharpe ratio
                  - include_beta (bool): Include beta calculation
                  - format (str): Report format ('summary' or 'detailed')
                  
    Returns:
        dict: Risk report with specified metrics
    """
    # TODO: Implement risk report generation with **kwargs
    pass

# Budget Analysis Functions
def categorize_transactions(*transactions):
    """
    Categorize transactions by type and category.
    Demonstrates *args usage.
    
    Args:
        *transactions: Variable number of transaction dictionaries
        
    Returns:
        dict: Transactions organized by type and category
    """
    # TODO: Implement transaction categorization with *args
    pass

def generate_savings_projection(income, expenses, years, /, *, savings_rate=0.2):
    """
    Generate savings projection based on income, expenses, and years.
    Demonstrates position-only and keyword-only arguments.
    
    Args:
        income (float): Monthly income (position-only)
        expenses (float): Monthly expenses (position-only)
        years (int): Number of years to project (position-only)
        savings_rate (float, optional): Target savings rate. Defaults to 0.2. (keyword-only)
        
    Returns:
        dict: Savings projection by year
    """
    # TODO: Implement savings projection with position-only and keyword-only arguments
    pass

# Report Generation Functions
def format_currency(amount):
    """
    Format a number as a currency string.
    
    Args:
        amount (float): Amount to format
        
    Returns:
        str: Formatted currency string
    """
    # TODO: Implement currency formatting
    pass

def format_percentage(value):
    """
    Format a number as a percentage string.
    
    Args:
        value (float): Value to format as percentage
        
    Returns:
        str: Formatted percentage string
    """
    # TODO: Implement percentage formatting
    pass

def monthly_performance_generator(data):
    """
    Generator function that yields monthly portfolio performance data.
    Demonstrates generator function with yield.
    
    Args:
        data (dict): Dictionary with monthly portfolio values
        
    Yields:
        tuple: (month, value, percent_change)
    """
    # TODO: Implement generator function with yield
    pass

def main():
    """
    Main function demonstrating financial analysis functions.
    """
    print("===== FINANCIAL ANALYSIS SYSTEM =====")
    
    # Get sample data
    portfolio = get_sample_portfolio()
    transactions = get_sample_transactions()
    goals = get_sample_financial_goals()
    market_data = get_sample_market_data()
    
    # TODO: Demonstrate portfolio analysis functions
    
    # TODO: Demonstrate risk assessment functions
    
    # TODO: Demonstrate budget analysis functions
    
    # TODO: Demonstrate report generation functions
    
    # TODO: Demonstrate generator function

if __name__ == "__main__":
    main()