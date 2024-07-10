import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Manually input the data
expected_returns = {
    "Cash": 1.5,
    "US Bonds": 2.0,
    "International Bonds": 2.5,
    "US Equities": 6.0,
    "International Equities": 6.5
}

volatilities = {
    "Cash": 0.5,
    "US Bonds": 3.0,
    "International Bonds": 4.0,
    "US Equities": 15.0,
    "International Equities": 16.0
}

correlations = {
    "Cash": [1, 0.1, 0.1, 0.0, 0.0],
    "US Bonds": [0.1, 1, 0.5, 0.2, 0.2],
    "International Bonds": [0.1, 0.5, 1, 0.2, 0.2],
    "US Equities": [0.0, 0.2, 0.2, 1, 0.8],
    "International Equities": [0.0, 0.2, 0.2, 0.8, 1]
}

# Convert data to DataFrames
returns_df = pd.DataFrame(list(expected_returns.items()), columns=["Asset Class", "Expected Return"])
volatilities_df = pd.DataFrame(list(volatilities.items()), columns=["Asset Class", "Volatility"])
correlations_df = pd.DataFrame(correlations, index=["Cash", "US Bonds", "International Bonds", "US Equities", "International Equities"])

st.title("Goals-Based Wealth Management Prototype - Brunel's Model")

# Chapter 1: Introduction to Goals-Based Wealth Management
st.header("Introduction to Goals-Based Wealth Management")

st.write("""
Goals-based wealth management is a financial planning approach that focuses on achieving specific, personalized financial goals rather than simply maximizing investment returns. This approach is designed to align an individual's or family's financial resources with their unique life objectives and priorities.

### Differences from Traditional Wealth Management
- **Goals-Based Approach:** Focuses on specific financial goals (e.g., retirement, education, philanthropy) and allocates resources accordingly.
- **Traditional Approach:** Primarily aims to maximize investment returns and often uses a one-size-fits-all strategy.

Goals-based wealth management considers each goal's time horizon, risk tolerance, and priority, allowing for a more tailored and effective financial plan.
""")

# Divider
st.markdown("---")

# Client Information
st.header("Client Information")
client_name = st.text_input("Client Name")
client_age = st.number_input("Client Age", min_value=18)
financial_goals = st.text_area("Financial Goals")

current_assets = st.number_input("Current Assets ($)", min_value=0, key="current_assets")
annual_income = st.number_input("Annual Income ($)", min_value=0, key="annual_income")
annual_expenses = st.number_input("Annual Expenses ($)", min_value=0, key="annual_expenses")

# Divider
st.markdown("---")

# Chapter 2: Setting Goals
st.header("Setting Financial Goals")

st.write("""
In goals-based wealth management, setting clear and specific financial goals is crucial. Goals are typically categorized into three types: Lifestyle, Aspirational, and Legacy. Each goal should have a specific amount, time horizon, and priority.
""")

# Examples of Goals Table
st.write("""
### Examples of Goals:
| Category      | Example Goal         | Amount Required | Time Horizon | Priority |
|---------------|----------------------|-----------------|--------------|----------|
| Lifestyle     | Retirement Income    | $1,000,000      | 20 years     | High     |
| Lifestyle     | Daily Living Expenses| $50,000/year    | Ongoing      | High     |
| Aspirational  | Vacation Home        | $500,000        | 10 years     | Medium   |
| Aspirational  | Luxury Car           | $100,000        | 5 years      | Low      |
| Legacy        | Estate Planning      | $2,000,000      | 30 years     | High     |
| Legacy        | Charitable Giving    | $250,000        | 15 years     | Medium   |
""")

num_goals = st.number_input("Number of Goals", min_value=1, max_value=10, step=1)

goals = []
for i in range(num_goals):
    st.subheader(f"Goal {i+1}")
    goal_name = st.text_input(f"Goal {i+1} Name", key=f"goal_name_{i}")
    goal_amount = st.number_input(f"Goal {i+1} Amount ($)", min_value=0, key=f"goal_amount_{i}")
    goal_horizon = st.number_input(f"Goal {i+1} Time Horizon (years)", min_value=0, key=f"goal_horizon_{i}")
    goal_type = st.selectbox(f"Goal {i+1} Type", ["Lifestyle", "Aspirational", "Legacy"], key=f"goal_type_{i}")
    goal_priority = st.selectbox(f"Goal {i+1} Priority", ["High", "Medium", "Low"], key=f"goal_priority_{i}")
    goals.append({"name": goal_name, "amount": goal_amount, "horizon": goal_horizon, "type": goal_type, "priority": goal_priority})

# Goal Summary Section
st.header("Goal Summary")
for goal in goals:
    st.subheader(f"Goal: {goal['name']}")
    st.write(f"Amount: ${goal['amount']:,.2f}")
    st.write(f"Time Horizon: {goal['horizon']} years")
    st.write(f"Type: {goal['type']}")
    st.write(f"Priority: {goal['priority']}")
    st.markdown("---")

# Divider
st.markdown("---")

# Chapter 3: Risk Tolerance and Capacity
st.header("Risk Tolerance and Capacity")

st.write("""
Risk tolerance is a measure of how much risk you are willing to take, while risk capacity is a measure of how much risk you can financially afford to take. Both factors are crucial in determining the appropriate investment strategy for achieving your financial goals.
""")

# Risk Tolerance Questionnaire
st.subheader("Risk Tolerance Questionnaire")

risk_tolerance_questions = [
    "How would you react if your investment portfolio lost 20% of its value in a short period?",
    "How much experience do you have with investing in stocks and bonds?",
    "What is your primary goal for investing?",
    "How long is your investment horizon?",
    "How comfortable are you with market fluctuations?"
]

risk_tolerance_responses = []
for i, question in enumerate(risk_tolerance_questions):
    response = st.radio(question, options=["Very Uncomfortable", "Uncomfortable", "Neutral", "Comfortable", "Very Comfortable"], key=f"risk_tolerance_{i}")
    risk_tolerance_responses.append(response)

# Risk Capacity Assessment
st.subheader("Risk Capacity Assessment")

income = st.number_input("Annual Income ($)", min_value=0, key="risk_capacity_income")
net_worth = st.number_input("Net Worth ($)", min_value=0, key="risk_capacity_net_worth")
investment_horizon = st.number_input("Investment Horizon (years)", min_value=0, key="risk_capacity_horizon")
liquidity_needs = st.radio("Liquidity Needs", options=["Low", "Medium", "High"], key="risk_capacity_liquidity")

# Placeholder for risk capacity calculations (detailed formulas and calculations would be added here)
risk_capacity_score = (income + net_worth) / (investment_horizon + 1)  # Simplified example calculation

# Combined Risk Profile Summary
st.header("Combined Risk Profile Summary")

st.write("""
Based on your risk tolerance and capacity assessments, here is a summary of your risk profile and recommendations:
""")

risk_tolerance_score = sum([1 if response in ["Very Comfortable", "Comfortable"] else -1 for response in risk_tolerance_responses])  # Simplified example calculation
st.write(f"Risk Tolerance Score: {risk_tolerance_score}")
st.write(f"Risk Capacity Score: {risk_capacity_score}")

# Divider
st.markdown("---")

# Chapter 4: Asset Allocation Strategies
st.header("Asset Allocation Strategies")

st.write("""
Asset allocation is a crucial part of the investment process. It involves dividing your investment portfolio among different asset categories, such as stocks, bonds, and cash. The allocation depends on your risk tolerance, risk capacity, and investment goals.
""")

# Strategic Asset Allocation
st.subheader("Strategic Asset Allocation")

st.write("Define your target percentages for each asset class in the long term:")

strategic_allocation = {
    "Cash": st.slider("Cash (%)", min_value=0, max_value=100, value=10, step=1, key="strategic_cash"),
    "US Bonds": st.slider("US Bonds (%)", min_value=0, max_value=100, value=30, step=1, key="strategic_us_bonds"),
    "International Bonds": st.slider("International Bonds (%)", min_value=0, max_value=100, value=20, step=1, key="strategic_international_bonds"),
    "US Equities": st.slider("US Equities (%)", min_value=0, max_value=100, value=30, step=1, key="strategic_us_equities"),
    "International Equities": st.slider("International Equities (%)", min_value=0, max_value=100, value=10, step=1, key="strategic_international_equities")
}

# Tactical Asset Allocation
st.subheader("Tactical Asset Allocation")

st.write("Make short-term adjustments to your asset allocation based on current market conditions:")

tactical_allocation = {
    "Cash": st.slider("Cash (%)", min_value=0, max_value=100, value=strategic_allocation["Cash"], step=1, key="tactical_cash"),
    "US Bonds": st.slider("US Bonds (%)", min_value=0, max_value=100, value=strategic_allocation["US Bonds"], step=1, key="tactical_us_bonds"),
    "International Bonds": st.slider("International Bonds (%)", min_value=0, max_value=100, value=strategic_allocation["International Bonds"], step=1, key="tactical_international_bonds"),
    "US Equities": st.slider("US Equities (%)", min_value=0, max_value=100, value=strategic_allocation["US Equities"], step=1, key="tactical_us_equities"),
    "International Equities": st.slider("International Equities (%)", min_value=0, max_value=100, value=strategic_allocation["International Equities"], step=1, key="tactical_international_equities")
}

# Visualization of Asset Allocation
st.subheader("Visualization of Asset Allocation")

st.write("Compare your strategic and tactical asset allocations:")

# Pie charts for strategic and tactical allocations
fig, ax = plt.subplots(1, 2, figsize=(10, 5))

ax[0].pie(strategic_allocation.values(), labels=strategic_allocation.keys(), autopct='%1.1f%%', startangle=90)
ax[0].set_title('Strategic Allocation')

ax[1].pie(tactical_allocation.values(), labels=tactical_allocation.keys(), autopct='%1.1f%%', startangle=90)
ax[1].set_title('Tactical Allocation')

st.pyplot(fig)

# Divider
st.markdown("---")

# Chapter 5: Portfolio Construction
st.header("Portfolio Construction")

st.write("""
Portfolio construction involves creating a diversified portfolio that aligns with your financial goals, risk tolerance, and risk capacity. Using the expected returns, volatilities, and correlations from the provided data, we can construct an efficient portfolio.
""")

# Display the Expected Returns, Volatilities, and Correlations
st.subheader("Expected Returns")
st.dataframe(returns_df)

st.subheader("Volatilities")
st.dataframe(volatilities_df)

st.subheader("Correlations")
st.dataframe(correlations_df)

# Constructing the Portfolio
st.subheader("Construct Your Portfolio")

asset_classes = list(expected_returns.keys())

portfolio_allocation = {}
for asset_class in asset_classes:
    portfolio_allocation[asset_class] = st.slider(f"{asset_class} Allocation (%)", min_value=0, max_value=100, step=1, key=f"portfolio_{asset_class}")

# Display the portfolio allocation
st.write("### Portfolio Allocation")
st.write(portfolio_allocation)

# Ensure the sum of allocations is 100%
total_allocation = sum(portfolio_allocation.values())
if total_allocation != 100:
    st.warning("The total allocation must sum up to 100%. Please adjust the allocations.")
else:
    st.success("The total allocation is 100%.")

# Calculate the expected return and volatility of the portfolio
portfolio_return = sum([portfolio_allocation[asset] * expected_returns[asset] / 100 for asset in asset_classes])
portfolio_volatility = sum([portfolio_allocation[asset] * volatilities[asset] / 100 for asset in asset_classes])

st.write(f"### Expected Portfolio Return: {portfolio_return:.2f}%")
st.write(f"### Expected Portfolio Volatility: {portfolio_volatility:.2f}%")

# Calculate the portfolio variance
correlation_matrix = pd.DataFrame(correlations).values
weights = [portfolio_allocation[asset] / 100 for asset in asset_classes]
portfolio_variance = sum([weights[i] * weights[j] * volatilities[asset_classes[i]] * volatilities[asset_classes[j]] * correlation_matrix[i, j] / 10000 for i in range(len(weights)) for j in range(len(weights))])

st.write(f"### Expected Portfolio Variance: {portfolio_variance:.2f}")

# Divider
st.markdown("---")

# Chapter 6: Implementing the Investment Strategy
st.header("Implementing the Investment Strategy")

st.write("""
Implementing the investment strategy involves putting the constructed portfolio into action. This includes monitoring the portfolio, rebalancing as needed, and making adjustments based on changes in the client's goals or market conditions.
""")

# Create Investment Policy Statement (IPS)
st.subheader("Investment Policy Statement (IPS)")

st.write("Generate the Investment Policy Statement based on the input data:")

# Define IPS sections
ips_sections = {
    "Client Information": {
        "Client Name": client_name,
        "Client Age": client_age,
        "Financial Goals": financial_goals,
        "Current Assets": current_assets,
        "Annual Income": annual_income,
        "Annual Expenses": annual_expenses
    },
    "Goals": goals,
    "Risk Profile": {
        "Risk Tolerance Score": risk_tolerance_score,
        "Risk Capacity Score": risk_capacity_score
    },
    "Strategic Asset Allocation": strategic_allocation,
    "Tactical Asset Allocation": tactical_allocation,
    "Expected Portfolio Return": portfolio_return,
    "Expected Portfolio Volatility": portfolio_volatility,
    "Expected Portfolio Variance": portfolio_variance
}

# Display the IPS
st.write("### Investment Policy Statement")
for section, content in ips_sections.items():
    st.subheader(section)
    st.write(content)

# Allow downloading the IPS as a text file
import io

ips_text = ""
for section, content in ips_sections.items():
    ips_text += f"{section}\n"
    for key, value in content.items() if isinstance(content, dict) else enumerate(content):
        ips_text += f"{key}: {value}\n"
    ips_text += "\n"

st.download_button(label="Download IPS as Text File", data=ips_text, file_name="investment_policy_statement.txt")

# Divider
st.markdown("---")

# Disclaimer
st.header("Disclaimer")
st.write("This software is for demonstration purposes only. It does not guarantee any results. Please consult with a financial advisor before making any investment decisions.")

