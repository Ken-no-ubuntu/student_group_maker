import tkinter as tk
from tkinter import messagebox
import random
from collections import defaultdict

# Student lists
FOURTH_YEAR = [
    "常広寿哉", "井上裕貴", "櫛田健志郎", "正木佑典", "斎藤烈", "森健士郎"
]

THIRD_YEAR = [
    "林明翔", "全輝", "妻井眞音", "鳥井信作", "片山菜津",
    "藤森貴大", "張芸馨", "文銘", "徐梓瑛"
]

ALL_STUDENTS = FOURTH_YEAR + THIRD_YEAR

# Main group function
def make_groups_gui(num_groups, absent_students):
    available_fourth = [s for s in FOURTH_YEAR if s not in absent_students]
    available_third = [s for s in THIRD_YEAR if s not in absent_students]

    random.shuffle(available_fourth)
    random.shuffle(available_third)

    groups = defaultdict(list)

    for i, student in enumerate(available_fourth):
        groups[i % num_groups].append(student)
    for i, student in enumerate(available_third):
        groups[i % num_groups].append(student)

    return dict(groups)

# GUI setup
def launch_gui():
    root = tk.Tk()
    root.title("Group Maker")

    # Entry for number of groups
    tk.Label(root, text="Number of groups:").grid(row=0, column=0, sticky='w')
    group_entry = tk.Entry(root)
    group_entry.grid(row=0, column=1)

    # Checklist for absent students
    tk.Label(root, text="Absent students:").grid(row=1, column=0, columnspan=2, sticky='w')
    check_vars = {}
    for idx, name in enumerate(ALL_STUDENTS):
        var = tk.IntVar()
        chk = tk.Checkbutton(root, text=name, variable=var)
        chk.grid(row=2 + idx // 3, column=idx % 3, sticky='w')
        check_vars[name] = var

    # Textbox for output
    output_box = tk.Text(root, height=20, width=60)
    output_box.grid(row=10, column=0, columnspan=3)

    # Button callback
    def generate_groups():
        try:
            num_groups = int(group_entry.get())
            if num_groups <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number of groups.")
            return

        absent_students = [name for name, var in check_vars.items() if var.get()]
        groups = make_groups_gui(num_groups, absent_students)

        output_box.delete("1.0", tk.END)
        for i in range(num_groups):
            members = groups.get(i, [])
            output_box.insert(tk.END, f"Group {i + 1}:\n")
            for member in members:
                output_box.insert(tk.END, f"  - {member}\n")
            output_box.insert(tk.END, "\n")

    # Generate button
    tk.Button(root, text="Generate Groups", command=generate_groups).grid(row=9, column=0, columnspan=3)

    root.mainloop()

# Run the GUI
launch_gui()
