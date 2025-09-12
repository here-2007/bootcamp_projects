### Budget Calculator (CLI)

### Overview
This script is a simple command-line budget calculator. It interactively asks for your monthly income and expenses, computes savings or deficit using $$ \text{savings} = \text{income} - \text{expenses} $$, and writes a human-readable summary to a file named budget.txt.

### What it does
- Prompts for monthly income details (fixed salary and other sources).
- Prompts for monthly expenses (rent/EMI, bills, groceries, transport, loan EMIs, lifestyle, miscellaneous).
- Calculates:
  - Total income
  - Total expenses
  - Savings or deficit for the month
- Writes a formatted report to budget.txt in the current working directory, overwriting any existing file.

### How it works
- income():
  - Collects two integer inputs: salary and other monthly income.
  - Returns a pair: a formatted summary string and the numeric total income.
- expenses():
  - Collects seven integer inputs for expense categories.
  - Returns a pair: a formatted summary string and the numeric total expenses.
- savings(income, expense):
  - Computes the difference and returns a formatted message:
    - Positive: congratulatory message with saved amount.
    - Negative: budget alert with the overspending amount.
    - Zero: neutral message about zero savings.
- main():
  - Calls the functions above in sequence and writes the combined summary to budget.txt.
  - The script runs immediately because main() is invoked at the bottom of the file.

### Inputs collected
- Income
  - Monthly Salary (Fixed Income)
  - Monthly Income From Any Other Sources
- Expenses
  - Rent / Home loan (EMI)
  - Bills (Electricity, water, etc.)
  - Groceries And Food
  - Transportation
  - EMI or Loan Payments
  - Lifestyle Expenses
  - Miscellaneous Expenses

All inputs are read using input() and converted to integers. Entering non-integer values will raise an error.

### Output
- File name: budget.txt
- Location: current working directory
- Content: a readable report with three sections—Income, Expense, and Savings—separated by blank lines.

Example budget.txt:
```
Income:-
Monthly Salary(i.e. Fixed Income) -> 45000
Monthly Income From Any Other Sources -> 5000
Total Income -> 50000


Expense:-
Rent / Home loan (EMI) -> 12000
Bills (eg. Electricity, water etc.) -> 2500
Groceries And Food -> 8000
Transportation -> 2000
EMI or Loan Payments -> 3000
Lifestyle Expenses -> 4000
Misclleneous Expenses -> 1500
Total Expenses -> 35000


Savings:-
Hurrayy!! You Saved 15000 This Month Keep Going.
```

### Requirements
- Python 3.x
- No external dependencies

### How to run
- Save the script as budget.py.
- Run from a terminal:
```
python budget.py
```
- Follow the on-screen prompts. The script will create or overwrite budget.txt when finished.

### Example session
```
Enter The Monthly Salary(i.e. Fixed Income) -> 45000
Enter The Monthly Income From Any Other Sources -> 5000


Enter Every Expense On Monthly Basis.

Rent / Home loan (EMI) Amount -> 12000
Amount Paid As Bills (eg. Electricity, water etc.) -> 2500
Amount For Groceries And Food -> 8000
Transportation Amount -> 2000
Amount For EMI or Loan Payments -> 3000
Lifestyle Expenses-> 4000
Misclleneous Expenses -> 1500
```
