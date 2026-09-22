# 🇰🇪 Stima SACCO Loan Evaluator & Digital Inclusion Framework

An interactive Streamlit application and digital inclusion framework designed to convert informal financial statements (M-PESA cash flows, FOSA/PRIME accounts, Alpha Deposits, and Share Capital) into automated credit eligibility assessments based on Stima SACCO regulations.

---

## 📌 Features

- **Automated Credit Readiness Engine**: Evaluates loan requests against SACCO regulations:
  - **3x Alpha Multiplier Rule**: Total borrowing limit capped at 3 times active non-withdrawable Alpha Deposits.
  - **90% Self-Guarantee Rule**: Evaluates whether a loan can be self-guaranteed without external guarantors (if requested amount <= 90% of Alpha Deposits).
  - **Debt Service Ratio (1/3 Rule)**: Ensures monthly loan repayments do not exceed allowable net disposable income limits.
  - **Membership & Share Capital Compliance**: Verifies minimum 6 months active membership and KES 25,000 Share Capital requirements.
- **Statement CSV Parsing**: Upload and analyze combined member financial activity (M-PESA + SACCO ledgers).
- **Digital Inclusion Stack**: Demonstrates how low-barrier tools (Google Workspace, M-PESA SMS parsers, Gemini AI) convert basic mobile phones into financial management hubs for MSMEs, Boda Boda riders, and Jua Kali artisans.

---

## 🛠️ Repository Structure

```text
stima-sacco-loan-evaluator/
├── app.py                      # Main Streamlit web application
├── requirements.txt            # Python environment dependencies
├── sacco_client_statement.csv  # Sample member financial statement dataset
└── README.md                   # Project documentation
