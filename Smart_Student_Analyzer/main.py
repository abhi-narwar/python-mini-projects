import tkinter as tk
from tkinter import messagebox
from datetime import date

DATA_FILE = "expenses.txt"

# ---------- Save Expense ----------
def save_expense(amount, category, exp_date):
    f = open(DATA_FILE, "a")
    f.write(amount + "," + category + "," + exp_date + "\n")
    f.close()

# ---------- Read Expenses ----------
def read_expenses():
    expenses = []
    try:
        f = open(DATA_FILE, "r")
        for line in f:
            data = line.strip().split(",")
            expenses.append(data)
        f.close()
    except:
        pass
    return expenses

# ---------- Add Expense Window ----------
def add_expense():
    win = tk.Toplevel(root)
    win.title("Add Expense")
    win.geometry("300x280")

    tk.Label(win, text="Amount").pack()
    amount_entry = tk.Entry(win)
    amount_entry.pack()

    tk.Label(win, text="Category").pack()
    category = tk.StringVar()
    category.set("Food")

    tk.OptionMenu(
        win,
        category,
        "Food",
        "Travel",
        "Study",
        "Entertainment",
        "Other"
    ).pack()

    tk.Label(win, text="Date").pack()
    date_entry = tk.Entry(win)
    date_entry.insert(0, date.today().strftime("%d-%m-%Y"))
    date_entry.pack()

    def submit():
        if amount_entry.get() == "":
            messagebox.showerror("Error", "Please enter amount")
            return

        save_expense(
            amount_entry.get(),
            category.get(),
            date_entry.get()
        )

        messagebox.showinfo("Success", "Expense Added Successfully")
        win.destroy()

    tk.Button(win, text="Save Expense", command=submit).pack(pady=10)

# ---------- Analysis Window ----------
def show_analysis():
    win = tk.Toplevel(root)
    win.title("Expense Analysis")
    win.geometry("350x300")

    expenses = read_expenses()

    if len(expenses) == 0:
        tk.Label(win, text="No expense data available").pack()
        return

    total = 0
    category_total = {}

    for exp in expenses:
        amount = float(exp[0])
        cat = exp[1]

        total += amount

        if cat in category_total:
            category_total[cat] += amount
        else:
            category_total[cat] = amount

    tk.Label(win, text="Total Expense: ₹" + str(total)).pack(pady=5)
    tk.Label(win, text="Category Wise Expense").pack()

    for c in category_total:
        tk.Label(win, text=c + " : ₹" + str(category_total[c])).pack()

# ---------- Performance Suggestion ----------
def performance_suggestion():
    win = tk.Toplevel(root)
    win.title("Performance Suggestion")
    win.geometry("350x200")

    expenses = read_expenses()

    study = 0
    entertainment = 0

    for exp in expenses:
        if exp[1] == "Study":
            study += float(exp[0])
        if exp[1] == "Entertainment":
            entertainment += float(exp[0])

    if entertainment > study:
        msg = "Entertainment expense is high.\nTry to focus more on studies."
    else:
        msg = "Good balance in spending.\nAcademic performance looks good."

    tk.Label(win, text=msg, wraplength=300).pack(pady=20)

# ---------- Main Window ----------
root = tk.Tk()
root.title("Smart Student Expense Analyzer")
root.geometry("400x350")

tk.Label(
    root,
    text="Smart Student Expense & Performance Analyzer",
    font=("Arial", 12, "bold")
).pack(pady=10)

tk.Button(root, text="Add Expense", width=25, command=add_expense).pack(pady=5)
tk.Button(root, text="View Analysis", width=25, command=show_analysis).pack(pady=5)
tk.Button(root, text="Performance Suggestion", width=25, command=performance_suggestion).pack(pady=5)
tk.Button(root, text="Exit", width=25, command=root.destroy).pack(pady=20)

root.mainloop()
