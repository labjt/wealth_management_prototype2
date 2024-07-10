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

current_assets = st.number_input("Current Assets ($)", min_value=0)
annual_income = st.number_input("Annual Income ($)", min_value=0)
annual_expenses = st.number_input("Annual Expenses ($)", min_value=0)

# Divider
st.markdown("---")

# Goal Categories
st.header("Goal Categories")
num_goals = st.number_input("Number of Goals", min_value=1, max_value=10, step=1)

goals = []
for i in range(num_goals):
    st.subheader(f"Goal {i+1}")
    goal_name = st.text_input(f"Goal {i+1} Name")
    goal_amount = st.number_input(f"Goal {i+1} Amount ($)", min_value=0)
    goal_horizon = st.number_input(f"Goal {i+1} Time Horizon (years)", min_value=0)
    goal_type = st.selectbox(f"Goal {i+1} Type", ["Lifestyle", "Aspirational", "Legacy"])
    goals.append({"name": goal_name, "amount": goal_amount, "horizon": goal_horizon, "type": goal_type})

# Divider
st.markdown("---")

# Generate Portfolio
if st.button("Generate Portfolio"):
    st.session_state.allocations = allocate_portfolio(goals)
    st.subheader("Goal Allocations")
    total_allocation = {"Cash": 0, "Bonds": 0, "Stocks": 0}

    for allocation in st.session_state.allocations:
        st.write(f"Goal: {allocation['Goal']}")
        st.write(f"Type: {allocation['Type']}")
        st.write(f"Allocation: {allocation['Allocation']}")
        st.write("---")
        for asset_class, percentage in allocation['Allocation'].items():
            total_allocation[asset_class] += percentage

    st.subheader("Total Portfolio Allocation")
    total_percentage = sum(total_allocation.values())
    for asset_class, percentage in total_allocation.items():
        st.write(f"{asset_class}: {percentage / total_percentage * 100:.2f}%")

    st.success("Portfolio generated successfully!")

# Divider
st.markdown("---")

# Display Aggregated Portfolio
st.header("Aggregated Portfolio View")
st.write("This feature will display the aggregated portfolio across multiple accounts.")

# Generate Investment Policy Statement (IPS)
if st.button("Generate IPS"):
    if st.session_state.allocations:
        ips = f"# Investment Policy Statement\n\n"
        ips += f"## Client Name: {client_name}\n"
        ips += f"## Client Age: {client_age}\n"
        ips += f"## Financial Goals: {financial_goals}\n\n"
        ips += f"## Account Types:\n"
        for account in accounts:
            ips += f"- {account[0]} ({account[1]}): ${account[2]}\n"
        ips += f"\n## Goal Allocations:\n"
        for allocation in st.session_state.allocations:
            ips += f"- Goal: {allocation['Goal']}, Type: {allocation['Type']}, Allocation: {allocation['Allocation']}\n"

        st.download_button(label="Download IPS", data=ips, file_name="investment_policy_statement.md", mime="text/markdown")
        st.success("Investment Policy Statement generated successfully!")
    else:
        st.error("Please generate the portfolio before creating the IPS.")

# Divider
st.markdown("---")

# Disclaimer
st.header("Disclaimer")
st.write("This software is for demonstration purposes only. It does not guarantee any results. Please consult with a financial advisor before making any investment decisions.")
