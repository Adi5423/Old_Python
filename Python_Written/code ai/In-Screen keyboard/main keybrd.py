import tkinter as tk
root = tk.Tk()
root.title("On-Screen Keyboard")
def insert_char(char):
    input_field.insert(tk.END, char)
input_field = tk.Entry(root, width=100)
input_field.pack()
keyboard_frame = tk.Frame(root)
keyboard_frame.pack()
letters = "qwertyuiopasdfghjklzxcvbnm"
for i, letter in enumerate(letters):
    button = tk.Button(keyboard_frame, text=letter, command=lambda: insert_char(letter))
    button.grid(row=int(i / 10), column=i % 10)
root.mainloop()