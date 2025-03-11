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
    """Calculate the current total value of a stock portfolio."""
    total_value = 0
    for stock in stocks:
        total_value += stock["shares"] * stock["current_price"]
    return total_value

def analyze_portfolio_performance(stocks, *, period="1y"):
    """Analyze portfolio performance over a specified period. Uses keyword-only arguments."""
    valid_periods = ["1m", "3m", "6m", "1y", "5y"]
    if period not in valid_periods:
        raise ValueError(f"Period must be one of: {', '.join(valid_periods)}")
    
    total_investment = sum(stock["shares"] * stock["purchase_price"] for stock in stocks)
    current_value = calculate_portfolio_value(stocks)
    
    # Calculate individual stock performance
    stock_performances = []
    for stock in stocks:
        purchase_value = stock["shares"] * stock["purchase_price"]
        current_stock_value = stock["shares"] * stock["current_price"]
        percent_change = (current_stock_value - purchase_value) / purchase_value * 100
        stock_performances.append({
            "ticker": stock["ticker"],
            "percent_change": percent_change,
            "dollar_change": current_stock_value - purchase_value
        })
    
    # Find best and worst performers
    best_performer = max(stock_performances, key=lambda x: x["percent_change"])
    worst_performer = min(stock_performances, key=lambda x: x["percent_change"])
    
    return {
        "total_gain_loss": current_value - total_investment,
        "percent_gain_loss": (current_value - total_investment) / total_investment * 100,
        "best_performer": best_performer,
        "worst_performer": worst_performer,
        "analysis_period": period
    }

def calculate_sector_allocation(stocks):
    """Calculate the percentage allocation of a portfolio by sector."""
    sector_values = {}
    total_value = 0
    
    for stock in stocks:
        sector = stock["sector"]
        stock_value = stock["shares"] * stock["current_price"]
        total_value += stock_value
        
        if sector in sector_values:
            sector_values[sector] += stock_value
        else:
            sector_values[sector] = stock_value
    
    sector_allocations = {
        "total_value": total_value,
        "sectors": {}
    }
    
    for sector, value in sector_values.items():
        sector_allocations["sectors"][sector] = {
            "value": value,
            "percentage": (value / total_value) * 100
        }
    
    return sector_allocations

def create_diversification_calculator(risk_profile):
    """Create a function that calculates allocation based on risk profile. Uses closures and nested functions."""
    # Define allocation percentages based on risk profile
    if risk_profile == "conservative":
        stocks_allocation = 30
        bonds_allocation = 50
        cash_allocation = 15
        other_allocation = 5
    elif risk_profile == "moderate":
        stocks_allocation = 50
        bonds_allocation = 35
        cash_allocation = 10
        other_allocation = 5
    elif risk_profile == "aggressive":
        stocks_allocation = 70
        bonds_allocation = 20
        cash_allocation = 5
        other_allocation = 5
    else:
        raise ValueError("Risk profile must be 'conservative', 'moderate', or 'aggressive'")
    
    # Define the nested function that captures the outer function's variables
    def calculate_allocation(investment_amount):
        """Calculate recommended investment allocation based on risk profile."""
        # Use nonlocal variables from the outer function
        nonlocal stocks_allocation, bonds_allocation, cash_allocation, other_allocation
        
        return {
            "stocks": (stocks_allocation / 100) * investment_amount,
            "bonds": (bonds_allocation / 100) * investment_amount,
            "cash": (cash_allocation / 100) * investment_amount,
            "other": (other_allocation / 100) * investment_amount,
            "risk_profile": risk_profile
        }
    
    # Return the nested function
    return calculate_allocation

# Risk Assessment Functions
def calculate_volatility(historical_prices):
    """Calculate the volatility (standard deviation) of stock prices."""
    if not historical_prices or len(historical_prices) < 2:
        return 0
    
    # Calculate returns
    returns = []
    for i in range(1, len(historical_prices)):
        returns.append((historical_prices[i] - historical_prices[i-1]) / historical_prices[i-1])
    
    # Calculate mean return
    mean_return = sum(returns) / len(returns)
    
    # Calculate variance
    variance = sum((r - mean_return) ** 2 for r in returns) / len(returns)
    
    # Return standard deviation (volatility)
    return (variance ** 0.5)

def calculate_risk_metrics(returns, risk_free_rate=0.03):
    """Calculate risk metrics including Sharpe Ratio. Uses default parameter values."""
    if not returns:
        return (0, 0, 0)
    
    avg_return = sum(returns) / len(returns)
    
    if len(returns) < 2:
        volatility = 0
    else:
        variance = sum((r - avg_return) ** 2 for r in returns) / len(returns)
        volatility = variance ** 0.5
    
    # Calculate Sharpe ratio
    sharpe_ratio = (avg_return - risk_free_rate) / volatility if volatility > 0 else 0
    
    # Return tuple of results
    return (avg_return, volatility, sharpe_ratio)

def generate_risk_report(**options):
    """Generate a risk assessment report with various options. Uses **kwargs."""
    # Default options
    default_options = {
        "include_volatility": True,
        "include_sharpe": True,
        "include_beta": False,
        "format": "summary"
    }
    
    # Merge provided options with defaults
    for key, value in default_options.items():
        if key not in options:
            options[key] = value
    
    # Create report dictionary
    report = {
        "title": "Risk Assessment Report",
        "format": options["format"],
        "metrics_included": []
    }
    
    # Add requested metrics
    if options["include_volatility"]:
        report["metrics_included"].append("volatility")
    
    if options["include_sharpe"]:
        report["metrics_included"].append("sharpe_ratio")
    
    if options["include_beta"]:
        report["metrics_included"].append("beta")
    
    # Add format-specific information
    if options["format"] == "detailed":
        report["additional_metrics"] = ["alpha", "r_squared", "standard_deviation"]
    
    return report

# Budget Analysis Functions
def categorize_transactions(*transactions):
    """Categorize transactions by type and category. Uses *args."""
    categorized = {
        "income": {},
        "expense": {},
        "total_income": 0,
        "total_expenses": 0,
        "net_cashflow": 0
    }
    
    # Process each transaction
    for transaction in transactions:
        # Skip invalid transactions
        if "type" not in transaction or "amount" not in transaction or "category" not in transaction:
            continue
        
        t_type = transaction["type"]
        amount = transaction["amount"]
        category = transaction["category"]
        
        # Add to appropriate category
        if t_type in ("income", "expense"):
            if category not in categorized[t_type]:
                categorized[t_type][category] = 0
            categorized[t_type][category] += amount
            
            # Update totals
            if t_type == "income":
                categorized["total_income"] += amount
            else:
                categorized["total_expenses"] += amount
    
    # Calculate net cash flow
    categorized["net_cashflow"] = categorized["total_income"] - categorized["total_expenses"]
    
    return categorized

def generate_savings_projection(income, expenses, years, /, *, savings_rate=0.2):
    """Generate savings projection. Uses position-only and keyword-only arguments."""
    # Validate inputs
    if income < 0 or expenses < 0 or years < 1:
        return {"error": "Invalid input values"}
    
    if savings_rate < 0 or savings_rate > 1:
        return {"error": "Savings rate must be between 0 and 1"}
    
    # Calculate monthly savings
    monthly_savings = income - expenses
    target_monthly_savings = income * savings_rate
    
    # Calculate current savings rate
    current_savings_rate = monthly_savings / income if income > 0 else 0
    
    # Generate projection
    projection = {
        "monthly_income": income,
        "monthly_expenses": expenses,
        "current_monthly_savings": monthly_savings,
        "current_savings_rate": current_savings_rate,
        "target_savings_rate": savings_rate,
        "target_monthly_savings": target_monthly_savings,
        "yearly_projection": {}
    }
    
    # Calculate yearly progression
    total_savings = 0
    for year in range(1, years + 1):
        yearly_savings = monthly_savings * 12
        total_savings += yearly_savings
        
        projection["yearly_projection"][year] = {
            "yearly_savings": yearly_savings,
            "cumulative_savings": total_savings
        }
    
    return projection

# Report Generation Functions
def format_currency(amount):
    """Format a number as a currency string."""
    return f"${amount:,.2f}"

def format_percentage(value):
    """Format a number as a percentage string."""
    return f"{value:.2f}%"

def monthly_performance_generator(data):
    """Generator function that yields monthly portfolio performance data. Uses yield."""
    previous_value = None
    
    for month, value in data.items():
        if previous_value is not None:
            percent_change = (value - previous_value) / previous_value * 100
        else:
            percent_change = 0
        
        yield (month, value, percent_change)
        previous_value = value

def main():
    """Main function demonstrating financial analysis functions."""
    print("===== FINANCIAL ANALYSIS SYSTEM =====")
    
    # Get sample data
    portfolio = get_sample_portfolio()
    transactions = get_sample_transactions()
    goals = get_sample_financial_goals()
    market_data = get_sample_market_data()
    
    # Demonstrate portfolio analysis
    print("\n----- PORTFOLIO ANALYSIS -----")
    value = calculate_portfolio_value(portfolio)
    print(f"Portfolio Value: {format_currency(value)}")
    
    performance = analyze_portfolio_performance(portfolio, period="1y")
    print(f"Gain/Loss: {format_currency(performance['total_gain_loss'])} " 
          f"({format_percentage(performance['percent_gain_loss'])})")
    
    # Demonstrate closures and nested functions
    conservative_calculator = create_diversification_calculator("conservative")
    allocation = conservative_calculator(100000)
    print(f"Conservative Allocation - Stocks: {format_currency(allocation['stocks'])}, Bonds: {format_currency(allocation['bonds'])}")
    
    # Demonstrate risk assessment and variable arguments
    print("\n----- RISK ASSESSMENT -----")
    report = generate_risk_report(format="detailed", include_beta=True)
    print(f"Risk Report Metrics: {', '.join(report['metrics_included'])}")
    
    # Demonstrate transaction analysis with *args
    print("\n----- BUDGET ANALYSIS -----")
    transaction_args = tuple(transactions)
    categorized = categorize_transactions(*transaction_args)
    print(f"Total Income: {format_currency(categorized['total_income'])}")
    print(f"Total Expenses: {format_currency(categorized['total_expenses'])}")
    
    # Demonstrate position-only and keyword-only arguments
    projection = generate_savings_projection(3000, 2000, 5, savings_rate=0.25)
    print(f"5-Year Savings: {format_currency(projection['yearly_projection'][5]['cumulative_savings'])}")
    
    # Demonstrate generator function
    print("\n----- PERFORMANCE GENERATOR -----")
    monthly_data = {"Jan": 10000, "Feb": 10500, "Mar": 10300, "Apr": 11000}
    for month, value, change in monthly_performance_generator(monthly_data):
        print(f"{month}: {format_currency(value)} ({format_percentage(change)})")

if __name__ == "__main__":
    main()