import streamlit as st

st.set_page_config(page_title="Mortgage AI Assistant", page_icon="🏦")

# Store borrowers
if "borrowers" not in st.session_state:
    st.session_state.borrowers = []

# -----------------------------
# Functions
# -----------------------------
def detect_loan_type(loan_choice):
    loan_choice = loan_choice.strip().upper()

    if loan_choice.startswith("VA"):
        return "VA Loan"
    elif loan_choice.startswith("FHA"):
        return "FHA Loan"
    elif loan_choice.startswith("CONV"):
        return "Conventional Loan"
    else:
        return "Incorrect Loan Number"


def check_credit_eligibility(credit_score):
    if credit_score < 580:
        return "❌ Not Eligible for any product"
    elif credit_score <= 619:
        return "✅ Eligible for FHA and VA Loan"
    elif credit_score <= 639:
        return "✅ Eligible for FHA / VA / Conventional Loan"
    else:
        return "✅ Eligible for all loan products"


# -----------------------------
# UI
# -----------------------------

st.title("🏦 Mortgage AI Assistant")
st.write("Simple Mortgage Eligibility Prototype")

menu = st.sidebar.selectbox(
    "Select Option",
    (
        "Detect Loan Type",
        "Check Credit Eligibility",
        "Add Borrower",
        "View Borrowers",
    ),
)

# -----------------------------
# Detect Loan Type
# -----------------------------
if menu == "Detect Loan Type":

    loan = st.text_input("Loan Number")

    if st.button("Detect Loan"):

        st.success(detect_loan_type(loan))

# -----------------------------
# Credit Eligibility
# -----------------------------
elif menu == "Check Credit Eligibility":

    score = st.number_input(
        "Credit Score",
        min_value=300,
        max_value=900,
        step=1,
    )

    if st.button("Check Eligibility"):

        st.success(check_credit_eligibility(score))

# -----------------------------
# Add Borrower
# -----------------------------
elif menu == "Add Borrower":

    name = st.text_input("Borrower Name")
    loan = st.text_input("Loan Number")
    credit = st.number_input(
        "Credit Score",
        min_value=300,
        max_value=900,
        step=1,
    )

    if st.button("Add Borrower"):

        st.session_state.borrowers.append(
            {
                "Name": name,
                "Loan": loan.upper(),
                "Credit": credit,
            }
        )

        st.success("Borrower added successfully!")

# -----------------------------
# View Borrowers
# -----------------------------
elif menu == "View Borrowers":

    if st.session_state.borrowers:

        st.table(st.session_state.borrowers)

    else:

        st.warning("No borrower found.")


