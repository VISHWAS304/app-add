# streamlit_app.py

import streamlit as st
from calculator import add_numbers  # Import the add_numbers function

st.title("Simple Addition App")

# Get input numbers
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Calculate sum using the function from calculator.py
sum_result = add_numbers(num1, num2)

# Display result
st.write(f"The sum of {num1} and {num2} is {sum_result}")
