from tkinter import *
import json
from tkinter import messagebox
import os

with open("commands.json", "r", encoding="utf-8") as file:
    commands = json.load(file)

def start_search():
    user_command = entry.get().strip().lower()
    try:
        filename = commands[user_command]
        os.startfile(filename)
    except:
        messagebox.showerror("Ошибка", f"Не удалось открыть: {user_command}")

def open_commands_window():
    window = Toplevel(root)
    window.title("Добавить команду")
    window.geometry("400x200")

    Label(window, text="Введите команду:").pack(pady=5)
    entry_command = Entry(window, width=40)
    entry_command.pack(pady=5)

    Label(window, text="Введите путь к файлу:").pack(pady=5)
    entry_path = Entry(window, width=40)
    entry_path.pack(pady=5)

    def add_command():
        new_command_name = entry_command.get().strip().lower()
        new_command_path = entry_path.get().strip()

        if new_command_name and new_command_path:
            commands[new_command_name] = new_command_path

            with open("commands.json", "w", encoding="utf-8") as file:
                json.dump(commands, file, ensure_ascii=False, indent=4)
            messagebox.showinfo("Успех", "Команда добавлена!")
            entry_command.delete(0, END)
            entry_path.delete(0, END)
        else:
            messagebox.showwarning("Внимание", "Пожалуйста, заполните оба поля!")

    Button(window, text="Добавить", command=add_command).pack(pady=5)

root = Tk()
root.title("Assistant")
root.geometry("400x150")

label = Label(root, text="Привет! Что открыть?.")
label.pack(pady=10)

entry = Entry(root, width=40)
entry.pack(pady=5)
entry.bind("<Return>", lambda event: start_search())

Button(root, text="Добавить команду", command=open_commands_window).pack(pady=5)
root.mainloop()
