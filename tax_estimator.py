import streamlit as st


st.title("Income Tax Calculator")

st.write("### 2023-2024")

col1, col2 = st.columns(2)
Income = col1.number_input("Whole Income", min_value=0, value=0)
Age = col1.number_input("Age", min_value=18, value=100)

option = st.selectbox(
   "What is your gender?",
   ("Male", "Female", "Transgender"),
   index=None,
   placeholder="Select your gender...",
)

st.write("You selected:", option)

def tax_calculator(Income):
    if Income < 300000:
        tax_percentage = 0
        tax = 0
    elif 300000 > Income < 600000:
        tax_percentage = 5
        tax = ((Income-300000)/100) * tax_percentage
    elif 600000 > Income < 900000:
        tax_percentage = 10
        tax = ((Income-600000)/100) * tax_percentage + 15000
    elif 900000 > Income < 1200000:
        tax_percentage = 15
        tax = ((Income-900000)/100) * tax_percentage + 45000
    elif 1200000 > Income < 1500000:
        tax_percentage = 20
        tax = ((Income-1200000)/100) * tax_percentage + 95000
    else:
        tax_percentage = 30
        tax = ((Income-1500000)/100) * tax_percentage + 1500000

    return tax_percentage, tax

#interest_rate = col2.number_input("Interest Rate (in %)", min_value=0.0, value=5.5)
#loan_term = col2.number_input("Loan Term (in years)", min_value=1, value=30)



if st.button('Calculate'):
    #Calling the tax calculator function to calculate tax
    tax_percentage, tax = tax_calculator(Income)

    #Display the tax
    tax_yearly = tax
    tax_monthly = tax/12
    st.write("### Tax repayment")
    col1, col2 ,col3 = st.columns(3)
    col1.metric(label="Monthly Repayments", value=f"₹{tax_monthly:,.2f}")
    col2.metric(label="Yearly Repayments", value=f"₹{tax_yearly:,.0f}")
    col3.metric(label="Tax Percentage", value=f"{tax_percentage:,.0f}%")






