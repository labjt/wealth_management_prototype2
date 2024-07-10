import streamlit as st

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

# Placeholder for future chapters and features
# ...

# Disclaimer
st.header("Disclaimer")
st.write("This software is for demonstration purposes only. It does not guarantee any results. Please consult with a financial advisor before making any investment decisions.")
