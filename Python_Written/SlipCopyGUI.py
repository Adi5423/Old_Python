import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('400x250')
root.title('Mark Slip')

style = tk.ttk.Style()
style.configure("TLabel", font=("Arial", 12), anchor="w")

label_title = tk.Label(root, text="Avadh Collegiate RG CAMPUS", font=("Arial", 16, "bold"))
label_title.grid(row=0, column=0, columnspan=4, pady=(20, 10))

label_exam = tk.Label(root, text="Mark slip of exam ( class XI COMM C.B.S.E", anchor="w")
label_exam.grid(row=1, column=0, columnspan=4, pady=(0, 5))

label_session = tk.Label(root, text="Academic session:2023 24", anchor="w")
label_session.grid(row=2, column=0, columnspan=4, pady=(0, 5))

label_class = tk.Label(root, text="Class & Sec Cz", anchor="w")
label_class.grid(row=3, column=0, columnspan=4, pady=(0, 5))

label_mm = tk.Label(root, text="M.M Marks obtained", anchor="w")
label_mm.grid(row=4, column=0, columnspan=4, pady=(10, 5))

ttk.Separator(root, orient="horizontal").grid(row=5, column=0, columnspan=4, padx=20, pady=(0, 10), sticky="ew")

subjects = [
    ("1", "ENGLISH", 40, 30),
    ("2", "HINDI", 40, 38),
    ("3", "ACCOUNTS", 40, 38),
    ("4", "B.STUDIES", 50, "-"),
    ("5", "ECONOMICS / EP", 40, 30),
    ("6", "P.ed / IP", 30, 30),
]

subject_var = tk.StringVar(root)
subject_combobox = ttk.Combobox(root, state="readonly", textvariable=subject_var)
subject_combobox.grid(row=6, column=0, padx=(20, 5), pady=(0, 5))

total_label = tk.Label(root, text="TOTAL", font=("Arial", 14, "bold"), anchor="w")
total_label.grid(row=6, column=1, padx=(20, 5), pady=(0, 5))

percentage_label = ttk.Label(root, text="PERCENTAGE", font=("Arial", 14, ("bold"), anchor=("w") ))
percentage_label.grid(row=6, column=2, padx=(20, 5), pady=(0, 5))

for i, (subject_number, subject_name, max_marks, marks_obtained) in enumerate(subjects, start=7):
    ttk.Separator(root, orient="horizontal").grid(row=i, column=0, columnspan=4, padx=20, pady=(0, 2), sticky="ew")

    ttk.Separator(root, orient="vertical").grid(row=i, column=0, rowspan=12, padx=15, pady=10, sticky="ns")

    tk.Label(root, text=subject_number, anchor="w").grid(row=i, column=0, pady=(0, 5))
    tk.Label(root, text=subject_name, anchor="w").grid(row=i, column=1, pady=(0, 5))
    tk.Label(root, text=f"{max_marks}", anchor="w").grid(row=i, column=2, pady=(0, 5))
    tk.Label(root, text=f"{marks_obtained}", anchor="w").grid(row=i, column=3, pady=(0, 5))

label_total = tk.Label(root, text="TOTAL", anchor="w")
label_total.grid(row=12, column=0, padx=(20, 0), pady=(10, 5))

label_percentage = tk.Label(root, text="PERCENTAGE", anchor="w")
label_percentage.grid(row=12, column=1, padx=(20, 0), pady=(10, 5))

label_total_value = tk.Label(root, text="230", anchor="w")
label_total_value.grid(row=12, column=2, padx=(20, 0), pady=(10, 5))

label_percentage_value = tk.Label(root, text="89.56%", anchor="w")
label_percentage_value.grid(row=12, column=3, padx=(20, 0), pady=(10, 5))

class_teacher_label = tk.Label(root, text="Sign of class Teacher", anchor="w")
class_teacher_label.grid(row=13, column=0, padx=20, pady=(0, 10), columnspan=4)

root.mainloop()