def income():
    salary=int(input("Enter The Monthly Salary(i.e. Fixed Income) ->"))
    othr_source=int(input("Enter The Monthly Income From Any Other Sources ->"))
    income = salary+othr_source
    return [f"Income:-\nMonthly Salary(i.e. Fixed Income) -> {salary}\nMonthly Income From Any Other Sources -> {othr_source}\nTotal Income -> {income}",income]
def expenses():
    print("\n\n\nEnter Every Expense On Monthly Basis.\n")
    rent=int(input("Rent / Home loan (EMI) Amount ->"))
    bills=int(input("Amount Paid As Bills (eg. Electricity, water etc.) ->"))
    groceries=int(input("Amount For Groceries And Food ->"))
    transport=int(input("Transportation Amount ->"))
    emi=int(input("Amount For EMI or Loan Payments ->"))
    lifestyle=int(input("Lifestyle Expenses->"))
    misc=int(input("Misclleneous Expenses ->"))
    expense=rent+bills+groceries+transport+emi+lifestyle+misc
    return [f"Expense:-\nRent / Home loan (EMI) -> {rent}\nBills (eg. Electricity, water etc.) -> {bills}\nGroceries And Food -> {groceries}\nTransportation -> {transport}\nEMI or Loan Payments -> {emi}\nLifestyle Expenses -> {lifestyle}\nMisclleneous Expenses -> {misc}\nTotal Expenses -> {expense}",expense]
def savings(income,expense):
    saving = income - expense
    if saving>0:
        return f"Savings:-\nHurrayy!! You Saved {saving} This Month Keep Going."
    elif saving<0:
        return f"Savings:-\n🚨 Budget alert: You’re spending {-(saving)} more than you earn.\nYour budget shows a deficit. Focus on needs first, then wants.\nEvery month is a fresh start. Next month, you’ll do even better."
    else:
        return f"Savings:-\nYou are On Zero Savings This Month But It's Ok Reducing Some Simple Expenses can make some savings. Keep Going!!"
def main():
    inc = income()
    expense= expenses()
    saving = savings(inc[1],expense[1])
    with open("budget.txt","w") as f :
        f.write(f"{inc[0]}\n\n\n{expense[0]}\n\n\n{saving}")

main()