import pytest
import inspect
import sys
import math
from test.TestUtils import TestUtils
from financial_analysis_system import *

class TestFunctional:
    """Enhanced test class to verify financial analysis functions match requirements"""
    
    def test_risk_metrics_calculation(self):
        """Test the sharpe ratio calculation logic specifically"""
        try:
            # Test sharpe ratio calculation
            returns = [0.05, 0.06, 0.04, 0.07]
            risk_free_rate = 0.03
            
            # Calculate metrics
            avg_return, volatility, sharpe_ratio = calculate_risk_metrics(returns, risk_free_rate)
            
            # Calculate expected values
            expected_avg = sum(returns) / len(returns)
            expected_variance = sum((r - expected_avg) ** 2 for r in returns) / len(returns)
            expected_volatility = expected_variance ** 0.5
            
            # Correct Sharpe ratio formula: (return - risk_free_rate) / volatility
            expected_sharpe = (expected_avg - risk_free_rate) / expected_volatility
            
            assert round(sharpe_ratio, 6) == round(expected_sharpe, 6), "Sharpe ratio calculation is incorrect"
            
            # Test with different risk-free rates
            for rate in [0.01, 0.02, 0.04, 0.05]:
                metrics = calculate_risk_metrics(returns, rate)
                expected = (expected_avg - rate) / expected_volatility
                assert round(metrics[2], 6) == round(expected, 6), f"Sharpe ratio incorrect with risk-free rate {rate}"
            
            TestUtils.yakshaAssert("TestRiskMetricsCalculation", True, "functional")
        except Exception as e:
            TestUtils.yakshaAssert("TestRiskMetricsCalculation", False, "functional")
            pytest.fail(f"Risk metrics calculation test failed: {str(e)}")
    
    def test_net_cashflow_calculation(self):
        """Test the net cashflow calculation specifically"""
        try:
            # Create test transactions with various income and expenses
            transactions = [
                {"date": "2023-01-15", "type": "expense", "amount": 100, "category": "Groceries"},
                {"date": "2023-01-20", "type": "income", "amount": 1000, "category": "Salary"},
                {"date": "2023-01-25", "type": "expense", "amount": 200, "category": "Utilities"},
                {"date": "2023-01-30", "type": "expense", "amount": 50, "category": "Groceries"},
                {"date": "2023-02-05", "type": "income", "amount": 500, "category": "Bonus"},
                {"date": "2023-02-10", "type": "expense", "amount": 300, "category": "Rent"}
            ]
            
            # Calculate net cashflow via the function
            categorized = categorize_transactions(*transactions)
            
            # Calculate the expected values manually
            total_income = 1000 + 500  # 1500
            total_expenses = 100 + 200 + 50 + 300  # 650
            expected_net_cashflow = total_income - total_expenses  # 850
            
            # Verify the correct net cashflow calculation
            assert categorized["total_income"] == total_income, "Total income calculation is incorrect"
            assert categorized["total_expenses"] == total_expenses, "Total expenses calculation is incorrect"
            assert categorized["net_cashflow"] == expected_net_cashflow, "Net cashflow calculation is incorrect"
            
            # Test another case with only expenses (negative net cashflow)
            expense_only = [
                {"date": "2023-01-15", "type": "expense", "amount": 100, "category": "Groceries"},
                {"date": "2023-01-25", "type": "expense", "amount": 200, "category": "Utilities"}
            ]
            
            expense_categorized = categorize_transactions(*expense_only)
            assert expense_categorized["total_income"] == 0, "Total income should be 0 with expense-only transactions"
            assert expense_categorized["total_expenses"] == 300, "Total expenses should be 300"
            assert expense_categorized["net_cashflow"] == -300, "Net cashflow should be -300 with expense-only transactions"
            
            # Test with only income (positive net cashflow)
            income_only = [
                {"date": "2023-01-20", "type": "income", "amount": 1000, "category": "Salary"},
                {"date": "2023-02-05", "type": "income", "amount": 500, "category": "Bonus"}
            ]
            
            income_categorized = categorize_transactions(*income_only)
            assert income_categorized["total_income"] == 1500, "Total income should be 1500"
            assert income_categorized["total_expenses"] == 0, "Total expenses should be 0 with income-only transactions"
            assert income_categorized["net_cashflow"] == 1500, "Net cashflow should be 1500 with income-only transactions"
            
            TestUtils.yakshaAssert("TestNetCashflowCalculation", True, "functional")
        except Exception as e:
            TestUtils.yakshaAssert("TestNetCashflowCalculation", False, "functional")
            pytest.fail(f"Net cashflow calculation test failed: {str(e)}")
    
    def test_monthly_performance_generator(self):
        """Test the monthly performance generator percentage calculation"""
        try:
            # Test with ascending values
            ascending_data = {"Jan": 100, "Feb": 110, "Mar": 121, "Apr": 133.1}
            
            # Generate performance data
            months = list(monthly_performance_generator(ascending_data))
            
            # Check first month (should have 0% change since no previous month)
            assert months[0][0] == "Jan", "First month should be Jan"
            assert months[0][1] == 100, "First month value should be 100"
            assert months[0][2] == 0, "First month should have 0% change"
            
            # Check Feb (should be 10% increase from Jan)
            expected_feb_change = ((110 - 100) / 100) * 100
            assert months[1][0] == "Feb", "Second month should be Feb"
            assert months[1][1] == 110, "Feb value should be 110"
            assert round(months[1][2], 2) == round(expected_feb_change, 2), "Feb should show 10% change from Jan"
            
            # Check Mar (should be 10% increase from Feb)
            expected_mar_change = ((121 - 110) / 110) * 100
            assert months[2][0] == "Mar", "Third month should be Mar"
            assert months[2][1] == 121, "Mar value should be 121"
            assert round(months[2][2], 2) == round(expected_mar_change, 2), "Mar should show 10% change from Feb"
            
            # Test with descending values
            descending_data = {"Jan": 100, "Feb": 90, "Mar": 81, "Apr": 72.9}
            
            # Generate performance data
            desc_months = list(monthly_performance_generator(descending_data))
            
            # Check Feb (should be -10% change from Jan)
            expected_feb_change = ((90 - 100) / 100) * 100
            assert desc_months[1][0] == "Feb", "Second month should be Feb"
            assert desc_months[1][1] == 90, "Feb value should be 90"
            assert round(desc_months[1][2], 2) == round(expected_feb_change, 2), "Feb should show -10% change from Jan"
            
            # Test with fluctuating values
            fluctuating_data = {"Jan": 100, "Feb": 110, "Mar": 99, "Apr": 109}
            
            # Generate performance data
            fluct_months = list(monthly_performance_generator(fluctuating_data))
            
            # Check Mar (should be -10% change from Feb)
            expected_mar_change = ((99 - 110) / 110) * 100
            assert fluct_months[2][0] == "Mar", "Third month should be Mar"
            assert fluct_months[2][1] == 99, "Mar value should be 99"
            assert round(fluct_months[2][2], 2) == round(expected_mar_change, 2), "Mar should show negative change from Feb"
            
            # Check Apr (should be 10.1% change from Mar)
            expected_apr_change = ((109 - 99) / 99) * 100
            assert fluct_months[3][0] == "Apr", "Fourth month should be Apr"
            assert fluct_months[3][1] == 109, "Apr value should be 109"
            assert round(fluct_months[3][2], 2) == round(expected_apr_change, 2), "Apr should show positive change from Mar"
            
            TestUtils.yakshaAssert("TestMonthlyPerformanceGenerator", True, "functional")
        except Exception as e:
            TestUtils.yakshaAssert("TestMonthlyPerformanceGenerator", False, "functional")
            pytest.fail(f"Monthly performance generator test failed: {str(e)}")
    
    def test_savings_projection_calculation(self):
        """Test the savings projection calculation logic"""
        try:
            # Test basic savings projection
            income = 5000
            expenses = 3000
            years = 5
            savings_rate = 0.25
            
            # Generate projection
            projection = generate_savings_projection(income, expenses, years, savings_rate=savings_rate)
            
            # Expected calculations
            expected_monthly_savings = income - expenses  # 2000
            expected_target_savings = income * savings_rate  # 1250
            expected_yearly_savings = expected_monthly_savings * 12  # 24000
            
            # Verify projection calculations
            assert projection["monthly_income"] == income, "Income in savings projection is incorrect"
            assert projection["monthly_expenses"] == expenses, "Expenses in savings projection is incorrect"
            assert projection["current_monthly_savings"] == expected_monthly_savings, "Monthly savings calculation is incorrect"
            assert projection["target_monthly_savings"] == expected_target_savings, "Target savings calculation is incorrect"
            
            # Check each year's projection
            total_savings = 0
            for year in range(1, years + 1):
                yearly_key = year
                total_savings += expected_yearly_savings
                
                assert projection["yearly_projection"][yearly_key]["yearly_savings"] == expected_yearly_savings, f"Year {year} yearly savings incorrect"
                assert projection["yearly_projection"][yearly_key]["cumulative_savings"] == total_savings, f"Year {year} cumulative savings incorrect"
            
            # Test edge case where income = expenses (no savings)
            zero_savings = generate_savings_projection(3000, 3000, 3, savings_rate=0.2)
            assert zero_savings["current_monthly_savings"] == 0, "Monthly savings should be 0 when income equals expenses"
            assert zero_savings["yearly_projection"][3]["cumulative_savings"] == 0, "Cumulative savings should be 0 for all years"
            
            # Test case where income is less than target savings rate
            low_income = generate_savings_projection(1000, 900, 2, savings_rate=0.2)
            assert low_income["current_monthly_savings"] == 100, "Monthly savings should be 100"
            assert low_income["target_monthly_savings"] == 200, "Target monthly savings should be 200"
            assert low_income["current_savings_rate"] == 0.1, "Current savings rate should be 0.1 (10%)"
            
            TestUtils.yakshaAssert("TestSavingsProjectionCalculation", True, "functional")
        except Exception as e:
            TestUtils.yakshaAssert("TestSavingsProjectionCalculation", False, "functional")
            pytest.fail(f"Savings projection calculation test failed: {str(e)}")
    
    

if __name__ == '__main__':
    pytest.main(['-v'])