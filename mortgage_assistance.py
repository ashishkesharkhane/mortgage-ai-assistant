def display_menu():
    print(f"""
{"=" * 40}
       MORTGAGE LOAN SYSTEM
{"=" * 40}
1. Detect Loan Type
2. Check Credit Eligibility
3. Add Borrower
4. View Borrower
5. Exit
{"=" * 40}
""")


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
        return "Not Eligible for any product"
    elif 580 <= credit_score <= 619:
        return "Eligible for FHA and VA Loan"
    elif 620 <= credit_score <= 639:
        return "Eligible for FHA / VA and Conventional Loan"
    else:
        return "Eligible for all loan products"


borrowers = []


def add_borrower():
    name = input("Enter Borrower Name: ")
    loan = input("Enter Loan Number: ").strip().upper()
    credit = int(input("Enter Credit Score: "))

    borrower = {
        "name": name,
        "loan": loan,
        "credit": credit
    }

    borrowers.append(borrower)

    return "✅ Borrower added successfully!"


def view_borrower():
    if not borrowers:
        print("NO BORROWER FOUND")
        return

    for borrower in borrowers:
        print(f"""
========================================
        BORROWER INFORMATION
========================================
Borrower : {borrower["name"]}
Loan No  : {borrower["loan"]}
Credit   : {borrower["credit"]}
========================================
""")


def main():
    while True:

        display_menu()

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter numbers only.")
            continue

        if choice == 1:

            loan_choice = input("Enter the Loan Number: ")
            print(detect_loan_type(loan_choice))

        elif choice == 2:

            try:
                credit_score = int(input("Enter your Credit Score: "))
                print(check_credit_eligibility(credit_score))
            except ValueError:
                print("Please enter numbers only.")

        elif choice == 3:

            print(add_borrower())

        elif choice == 4:

            view_borrower()

        elif choice == 5:

            print("Thank you for using Mortgage Loan System.")
            break

        else:

            print("Incorrect Selection")


main()