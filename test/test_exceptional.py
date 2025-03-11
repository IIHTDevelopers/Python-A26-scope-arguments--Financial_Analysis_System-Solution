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

class TestExceptional:
    """Test class for exception handling tests of the Financial Analysis System."""
    
    def test_error_handling(self):
        """Consolidated test for error handling of financial analysis functions"""
        try:
            # Test invalid portfolio data
            invalid_portfolio = "not a list"
            incomplete_portfolio = [{"ticker": "AAPL"}]  # Missing required fields
            
            # Test invalid transaction data
            invalid_transaction = "not a list"
            incomplete_transaction = [{"type": "income"}]  # Missing amount and category
            
            # Test portfolio value calculation with invalid inputs
            try:
                calculate_portfolio_value(invalid_portfolio)
                assert False, "Should raise an exception with non-list input"
            except (TypeError, AttributeError):
                pass  # Expected exception
                
            # Test portfolio value with incomplete portfolio data
            try:
                value = calculate_portfolio_value(incomplete_portfolio)
                # May handle gracefully by skipping bad items, or raise exception
            except (KeyError, AttributeError):
                pass  # Expected exception
            
            # Test portfolio performance with invalid period
            valid_portfolio = [
                {"ticker": "AAPL", "shares": 10, "purchase_price": 150.0, "current_price": 175.0, "sector": "Technology"}
            ]
            
            try:
                analyze_portfolio_performance(valid_portfolio, period="invalid")
                assert False, "Should raise ValueError with invalid period"
            except ValueError:
                pass  # Expected exception
            
            # Test diversification calculator with invalid risk profile
            try:
                create_diversification_calculator("invalid_profile")
                assert False, "Should raise ValueError with invalid risk profile"
            except ValueError:
                pass  # Expected exception
            
            # Test risk metrics with invalid data types
            try:
                calculate_risk_metrics("not a list")
                assert False, "Should raise exception with non-list input"
            except (TypeError, AttributeError):
                pass  # Expected exception
                
            # Test risk metrics with invalid returns
            try:
                calculate_risk_metrics([1, "not a number", 3])
                assert False, "Should handle non-numeric returns appropriately"
            except (TypeError, ValueError):
                pass  # Expected exception
            
            # Test formatting functions with invalid inputs
            try:
                format_currency("not a number")
                assert False, "Should raise TypeError with non-numeric input"
            except (TypeError, ValueError):
                pass  # Expected exception
                
            try:
                format_percentage("not a number")
                assert False, "Should raise TypeError with non-numeric input"
            except (TypeError, ValueError):
                pass  # Expected exception
            
            # Test generator with invalid data types
            try:
                list(monthly_performance_generator("not a dict"))
                assert False, "Should raise TypeError with non-dict input"
            except (TypeError, AttributeError):
                pass  # Expected exception
            
            # Test savings projection with invalid inputs
            # Either it should raise an exception or handle it gracefully
            try:
                result = generate_savings_projection(-1000, 500, 5, savings_rate=0.2)
                # If no exception, check that it handled the negative value appropriately
                assert result.get("error") or result.get("current_monthly_savings") <= 0, "Should handle negative income appropriately"
            except ValueError:
                pass  # Exception is also acceptable
                
            # Either it should raise an exception or handle it gracefully
            try:
                result = generate_savings_projection(1000, 500, -5, savings_rate=0.2)
                # If no exception, check that it handled the negative years value appropriately
                assert result.get("error"), "Should handle negative years appropriately"
            except ValueError:
                pass  # Exception is also acceptable
            
            # Either it should raise an exception or handle it gracefully
            try:
                result = generate_savings_projection(1000, 500, 5, savings_rate=2.0)
                # If no exception, check that it handled the invalid savings rate appropriately
                assert result.get("error"), "Should handle savings_rate > 1 appropriately"
            except ValueError:
                pass  # Exception is also acceptable
            
            # Test transaction categorization with invalid inputs
            try:
                categorize_transactions("not a transaction")
                # May handle gracefully by skipping bad items
            except (TypeError, AttributeError, KeyError):
                pass  # Expected exception
                
            # Test with None values
            try:
                calculate_portfolio_value(None)
                assert False, "Should raise TypeError with None input"
            except (TypeError, AttributeError):
                pass  # Expected exception
                
            # Instead of expecting an exception, check if the function handles None gracefully
            result = calculate_volatility(None)
            assert result == 0, "Should handle None input gracefully or raise TypeError"
            
            # Test sector allocation with invalid data
            try:
                calculate_sector_allocation(invalid_portfolio)
                assert False, "Should raise TypeError with non-list input"
            except (TypeError, AttributeError):
                pass  # Expected exception
            
            # Test risk report with invalid options
            try:
                report = generate_risk_report(format=123)  # Invalid format type
                # Might handle gracefully or raise exception
            except (TypeError, ValueError):
                pass  # Expected exception
            
            TestUtils.yakshaAssert("TestErrorHandling", True, "exception")
        except Exception as e:
            TestUtils.yakshaAssert("TestErrorHandling", False, "exception")
            pytest.fail(f"Error handling test failed: {str(e)}")

    def test_invalid_inputs(self):
        """Test various invalid inputs across financial functions"""
        try:
            # Test None values
            assert calculate_portfolio_value([]) == 0, "Empty portfolio should have zero value"
            assert calculate_volatility([]) == 0, "Empty price history should have zero volatility"
            assert calculate_risk_metrics([]) == (0, 0, 0), "Empty returns should have zeros for metrics"
            
            # Test invalid financial values
            negative_portfolio = [
                {"ticker": "NEG", "shares": -5, "purchase_price": 100.0, "current_price": 120.0, "sector": "Test"}
            ]
            
            try:
                value = calculate_portfolio_value(negative_portfolio)
                # May handle gracefully by using absolute values or raise exception
            except ValueError:
                pass  # Expected exception
            
            # Test NaN and infinity handling
            import math
            nan_portfolio = [
                {"ticker": "NAN", "shares": 10, "purchase_price": math.nan, "current_price": 100.0, "sector": "Test"}
            ]
            
            inf_portfolio = [
                {"ticker": "INF", "shares": 10, "purchase_price": 100.0, "current_price": math.inf, "sector": "Test"}
            ]
            
            try:
                nan_value = calculate_portfolio_value(nan_portfolio)
                # May handle gracefully or raise exception
            except (ValueError, TypeError):
                pass  # Expected exception
                
            try:
                inf_value = calculate_portfolio_value(inf_portfolio)
                # May handle gracefully or raise exception
            except (ValueError, TypeError, OverflowError):
                pass  # Expected exception
            
            # Test income/expense edge cases
            zero_income = generate_savings_projection(0, 0, 1, savings_rate=0.2)
            assert zero_income["current_monthly_savings"] == 0, "Zero income should have zero savings"
            
            # Test with invalid transaction types
            invalid_type_transaction = [{"type": "invalid", "amount": 100, "category": "Other"}]
            categorized = categorize_transactions(*invalid_type_transaction)
            assert "invalid" not in categorized, "Invalid transaction types should be ignored"
            
            TestUtils.yakshaAssert("TestInvalidInputs", True, "exception")
        except Exception as e:
            TestUtils.yakshaAssert("TestInvalidInputs", False, "exception")
            pytest.fail(f"Invalid input test failed: {str(e)}")


if __name__ == '__main__':
    pytest.main(['-v'])