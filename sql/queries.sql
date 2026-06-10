-- 1. Top 5 funds by AUM
SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV
SELECT AVG(nav)
FROM fact_nav;

-- 3. Transactions by State
SELECT state, COUNT(*)
FROM fact_transactions
GROUP BY state
ORDER BY COUNT(*) DESC;

-- 4. Funds with Expense Ratio < 1%
SELECT scheme_name, expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 5. Average 1-Year Return
SELECT AVG(return_1yr_pct)
FROM fact_performance;

-- 6. Highest Sharpe Ratio
SELECT scheme_name, sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;

-- 7. Highest AUM Funds
SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 10;

-- 8. Transaction Volume by Type
SELECT transaction_type, COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;

-- 9. Average Transaction Amount
SELECT AVG(amount_inr)
FROM fact_transactions;

-- 10. Funds with Very High Risk
SELECT scheme_name
FROM fact_performance
WHERE risk_grade='Very High';
