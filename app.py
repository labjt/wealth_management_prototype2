import streamlit as st
import pandas as pd

# Function to define investment strategy
def define_investment_strategy(goal_type):
    if goal_type == "Lifestyle":
        return {"Cash": 20, "Bonds": 50, "Stocks": 30}
    elif goal_type == "Aspirational":
        return {"Cash": 10, "Bonds": 30, "Stocks": 60}
    elif goal_type == "Legacy":
        return {"Cash": 5, "Bonds": 20, "Stocks": 75}
    return {"Cash": 0, "Bonds": 0, "Stocks": 0}

# Function to calculate goal amounts
def calculate_goal_amounts(goals):
    goal_amounts = []
    for goal in goals:
        strategy = define_investment_strategy(goal["type"])
        total_allocation = sum(strategy.values())
        if total_allocation == 0:
            allocation = {"Cash": 0, "Bonds": 0, "Stocks": 0}
        else:
            allocation = {k: v / total_allocation for k, v in strategy.items()}
        goal_amounts.append({
            "name": goal["name"],
            "type": goal["type"],
            "amount": goal["amount"],
            "horizon": goal["horizon"],
            "allocation": allocation
        })
    return goal_amounts

# Client Information
st.title("Goals-Based Wealth Management Prototype - Brunel's Model")
st.header("Client Information")
client_name = st.text_input("Client Name")
client_age = st.number_input("Client Age", min_value=18)
financial_goals = st.text_area("Financial Goals")
current_assets = st.number_input("Current Assets ($)", min_value=0)
annual_income = st.number_input("Annual Income ($)", min_value=0)
annual_expenses = st.number_input("Annual Expenses ($)", min_value=0)
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

st.markdown("---")

# Generate Portfolio
if st.button("Generate Portfolio"):
    goal_amounts = calculate_goal_amounts(goals)
    st.subheader("Goal Allocations")
    for goal in goal_amounts:
        st.write(f"Goal: {goal['name']}")
        st.write(f"Type: {goal['type']}")
        st.write(f"Amount: ${goal['amount']:,.2f}")
        st.write(f"Horizon: {goal['horizon']} years")
        st.write(f"Allocation: {goal['allocation']}")
        st.write("---")

# Disclaimer
st.header("Disclaimer")
st.write("This software is for demonstration purposes only. It does not guarantee any results. Please consult with a financial advisor before making any investment decisions.")
