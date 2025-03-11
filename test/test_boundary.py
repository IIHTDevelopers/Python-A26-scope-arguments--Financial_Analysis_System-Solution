import pytest
from test.TestUtils import TestUtils
from financial_analysis_system import (
    calculate_portfolio_value,
    analyze_portfolio_performance,
    calculate_sector_allocation,
    create_diversification_calculator,
    calculate_volatility,
    calculate_risk_metrics,
    generate_risk_report,
    categorize_transactions,
    generate_savings_projection,
    format_currency,
    format_percentage,
    monthly_performance_generator
)

class TestBoundary:
    """Boundary tests for financial analysis functions."""
    
    def test_boundary_scenarios(self):
        """Consolidated test for boundary scenarios across all functions"""
        try:
            # Test portfolio with extreme values
            min_portfolio = [
                {"ticker": "MIN", "shares": 1, "purchase_price": 0.01, "current_price": 0.01, "sector": "Test"}
            ]
            max_portfolio = [
                {"ticker": "MAX", "shares": 1000000, "purchase_price": 9999.99, "current_price": 10000.00, "sector": "Test"}
            ]
            
            # Test empty portfolio
            empty_portfolio = []
            
            # Test min/max value calculations
            min_value = calculate_portfolio_value(min_portfolio)
            max_value = calculate_portfolio_value(max_portfolio)
            empty_value = calculate_portfolio_value(empty_portfolio)
            
            assert min_value == 0.01, "Min portfolio should have value of $0.01"
            assert max_value == 10000000000.0, "Max portfolio should have correct large value"
            assert empty_value == 0, "Empty portfolio should have zero value"
            
            # Test sector allocation with single sector
            sector_allocation = calculate_sector_allocation(min_portfolio)
            assert len(sector_allocation["sectors"]) == 1, "Should have exactly one sector"
            assert "Test" in sector_allocation["sectors"], "Should contain Test sector"
            assert sector_allocation["sectors"]["Test"]["percentage"] == 100.0, "Single sector should be 100%"
            
            # Test empty sector allocation
            empty_sector = calculate_sector_allocation(empty_portfolio)
            assert empty_sector["total_value"] == 0, "Empty portfolio should have zero total value"
            assert len(empty_sector["sectors"]) == 0, "Empty portfolio should have no sectors"
            
            # Test risk diversification calculator with boundary values
            conservative = create_diversification_calculator("conservative")
            aggressive = create_diversification_calculator("aggressive")
            
            min_investment = conservative(1)
            max_investment = aggressive(1000000)
            
            assert min_investment["stocks"] == 0.3, "Conservative allocation for $1 should have $0.3 in stocks"
            assert max_investment["stocks"] == 700000.0, "Aggressive allocation for $1M should have $700K in stocks"
            
            # Test volatility with boundary values
            empty_history = []
            single_price = [100.0]
            stable_prices = [100.0, 100.0, 100.0, 100.0]
            volatile_prices = [100.0, 150.0, 75.0, 200.0]
            
            empty_vol = calculate_volatility(empty_history)
            single_vol = calculate_volatility(single_price)
            stable_vol = calculate_volatility(stable_prices)
            volatile_vol = calculate_volatility(volatile_prices)
            
            assert empty_vol == 0, "Empty price history should have zero volatility"
            assert single_vol == 0, "Single price should have zero volatility"
            assert stable_vol == 0, "Stable prices should have zero volatility"
            assert volatile_vol > 0, "Volatile prices should have positive volatility"
            
            # Test risk metrics with boundary values
            empty_returns = []
            single_return = [0.05]
            varied_returns = [-0.1, 0.0, 0.2, 0.05]
            
            empty_metrics = calculate_risk_metrics(empty_returns)
            single_metrics = calculate_risk_metrics(single_return)
            varied_metrics = calculate_risk_metrics(varied_returns)
            
            assert empty_metrics == (0, 0, 0), "Empty returns should have zeros for all metrics"
            assert single_metrics[0] == 0.05, "Single return should have mean of 0.05"
            assert single_metrics[1] == 0, "Single return should have zero volatility"
            assert round(varied_metrics[0], 4) == 0.0375, "Multiple returns should have correct mean"
            assert varied_metrics[1] > 0, "Multiple returns should have positive volatility"
            
            # Test transactions with boundary values
            empty_transactions = []
            income_only = [{"type": "income", "amount": 1000, "category": "Salary"}]
            expense_only = [{"type": "expense", "amount": 500, "category": "Rent"}]
            
            empty_categories = categorize_transactions(*empty_transactions)
            income_categories = categorize_transactions(*income_only)
            expense_categories = categorize_transactions(*expense_only)
            
            assert empty_categories["total_income"] == 0, "Empty transactions should have zero income"
            assert empty_categories["total_expenses"] == 0, "Empty transactions should have zero expenses"
            assert income_categories["total_income"] == 1000, "Income only should have $1000 income"
            assert income_categories["total_expenses"] == 0, "Income only should have zero expenses"
            assert expense_categories["total_income"] == 0, "Expense only should have zero income"
            assert expense_categories["total_expenses"] == 500, "Expense only should have $500 expenses"
            
            # Test savings projection with boundary values
            min_projection = generate_savings_projection(1, 0, 1, savings_rate=0.01)
            balanced_projection = generate_savings_projection(1000, 1000, 5, savings_rate=0.2)
            max_projection = generate_savings_projection(10000, 5000, 10, savings_rate=1.0)
            
            assert min_projection["current_monthly_savings"] == 1, "Min projection should save $1/month"
            assert balanced_projection["current_monthly_savings"] == 0, "Balanced should save $0/month"
            assert max_projection["current_monthly_savings"] == 5000, "Max projection should save $5000/month"
            
            # Test formatting functions with boundary values
            zero_currency = format_currency(0)
            small_currency = format_currency(0.01)
            large_currency = format_currency(1000000)
            
            zero_percent = format_percentage(0)
            small_percent = format_percentage(0.01)
            large_percent = format_percentage(100)
            
            assert zero_currency == "$0.00", "Zero should format as $0.00"
            assert small_currency == "$0.01", "Small amount should format as $0.01"
            assert large_currency == "$1,000,000.00", "Large amount should format correctly"
            assert zero_percent == "0.00%", "Zero should format as 0.00%"
            assert small_percent == "0.01%", "Small percentage should format as 0.01%"
            assert large_percent == "100.00%", "Large percentage should format as 100.00%"
            
            # Test generator with boundary values
            empty_data = {}
            single_month = {"Jan": 1000}
            flat_data = {"Jan": 1000, "Feb": 1000, "Mar": 1000}
            
            empty_gen = list(monthly_performance_generator(empty_data))
            single_gen = list(monthly_performance_generator(single_month))
            flat_gen = list(monthly_performance_generator(flat_data))
            
            assert len(empty_gen) == 0, "Empty data should yield no months"
            assert len(single_gen) == 1, "Single month should yield one item"
            assert len(flat_gen) == 3, "Flat data should yield three items"
            assert flat_gen[1][2] == 0, "Flat data should show 0% change"
            
            TestUtils.yakshaAssert("TestBoundaryScenarios", True, "boundary")
        except Exception as e:
            TestUtils.yakshaAssert("TestBoundaryScenarios", False, "boundary")
            pytest.fail(f"Boundary scenarios test failed: {str(e)}")


if __name__ == '__main__':
    pytest.main(['-v'])