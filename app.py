import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Stima SACCO & Digital Inclusion Toolkit",
    page_icon="🇰🇪",
    layout="wide"
)

st.title("🇰🇪 Digital Inclusion & Stima SACCO Loan Evaluation Tool")
st.markdown("""
This platform demonstrates digital financial inclusion by converting M-PESA and SACCO transactional statements 
(FOSA/PRIME, Alpha Deposits, Share Capital) into automated credit readiness and loan qualification assessments.
""")

st.sidebar.header("Member Parameters")
member_name = st.sidebar.text_input("Member Name", "Gikonyo Ndugu")
member_no = st.sidebar.text_input("Member Number", "STIMA-884920")
membership_months = st.sidebar.number_input("Membership Duration (Months)", min_value=1, value=18)

st.sidebar.subheader("Account Balances (KES)")
alpha_balance = st.sidebar.number_input("Alpha Deposits Balance", min_value=0.0, value=175000.0, step=5000.0)
share_capital = st.sidebar.number_input("Share Capital Balance", min_value=0.0, value=25000.0, step=1000.0)
gross_income = st.sidebar.number_input("Monthly Gross Income (M-PESA/PRIME)", min_value=0.0, value=120000.0, step=5000.0)
monthly_expenses = st.sidebar.number_input("Monthly Living Expenses", min_value=0.0, value=38000.0, step=2000.0)

tab1, tab2, tab3 = st.tabs(["📊 Loan Qualification Engine", "📜 Statement CSV Analyzer", "💡 Digital Inclusion Framework"])

with tab1:
    st.subheader("Stima SACCO Rule Evaluation")
    
    # Core Logic
    max_borrowing_3x = alpha_balance * 3.0
    self_guarantee_90pct = alpha_balance * 0.90
    net_disposable = gross_income - monthly_expenses
    max_allowed_deduction = gross_income * (2/3) # Must retain 1/3
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Alpha Deposits", f"KES {alpha_balance:,.2f}")
    col2.metric("Max Capacity (3x Alpha)", f"KES {max_borrowing_3x:,.2f}")
    col3.metric("Self-Guarantee Limit (90%)", f"KES {self_guarantee_90pct:,.2f}")
    
    st.divider()
    
    requested_loan = st.number_input("Enter Desired Business Loan Amount (KES)", min_value=10000.0, value=157500.0, step=10000.0)
    repayment_period = st.slider("Repayment Period (Months)", min_value=6, max_value=36, value=36)
    interest_rate = 0.14 # 14% p.a.
    
    # EMI Calculation
    r = interest_rate / 12
    emi = (requested_loan * r * ((1 + r)**repayment_period)) / (((1 + r)**repayment_period) - 1)
    
    st.write(f"**Estimated Monthly Installment (EMI):** KES {emi:,.2f}")
    
    # Qualification Checks
    st.markdown("### Qualification Criteria Checklist")
    
    check_membership = membership_months >= 6
    check_shares = share_capital >= 25000.0
    check_capacity = emi <= max_allowed_deduction and emi <= net_disposable
    check_guarantor = requested_loan <= self_guarantee_90pct
    
    st.write(f"- **Membership Duration (>= 6 Months):** {'✅ PASS' if check_membership else '❌ FAIL'}")
    st.write(f"- **Share Capital Target (>= KES 25,000):** {'✅ PASS' if check_shares else '❌ FAIL'}")
    st.write(f"- **Repayment Capacity (1/3 Net Income Rule):** {'✅ PASS' if check_capacity else '❌ FAIL'}")
    st.write(f"- **90% Self-Guarantee Threshold:** {'✅ PASS (No Guarantors Required)' if check_guarantor else '⚠️ REQUIRES EXTERNAL GUARANTORS'}")
    
    overall_status = check_membership and check_shares and check_capacity
    
    if overall_status:
        st.success(f"**LOAN QUALIFIED!** The member qualifies for KES {requested_loan:,.2f}.")
    else:
        st.error("**LOAN REJECTED / ACTION REQUIRED:**")
        if not check_membership:
            st.write("• Minimum membership requirement of 6 months not met.")
        if not check_shares:
            st.write("• Share capital is below the KES 25,000 required threshold.")
        if not check_capacity:
            st.write("• Monthly repayment exceeds allowable debt-service limits based on cashflow.")

with tab2:
    st.subheader("Parse & Analyze Member Statements")
    uploaded_file = st.file_uploader("Upload Member CSV Statement", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)
    else:
        st.info("Upload `sacco_client_statement.csv` to run dynamic batch parsing.")

with tab3:
    st.subheader("Mobile-First Digital Inclusion Architecture")
    st.markdown("""
    - **Google Workspace Ecosystem:** Low-barrier entry using Drive and Sheets.
    - **Gemini AI Integration:** Natural language processing for receipt scanning and Swahili/Sheng price discovery.
    - **M-PESA Parsing Engine:** Conversions of SMS receipts directly into structured accounting ledgers.
    """)
