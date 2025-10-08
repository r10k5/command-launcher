from tkinter import *
import json
from tkinter import messagebox
import os
from config import *

if not os.path.exists("commands.json"):
    with open("commands.json", "w", encoding="utf-8") as file:
        json.dump({}, file, ensure_ascii=False, indent=4)

with open("commands.json", "r", encoding="utf-8") as file:
    commands = json.load(file)

def start_search():
    user_command = entry.get().strip().lower()
    try:
        filename = commands[user_command]
        os.startfile(filename)
        entry.delete(0, END)
    except:
        messagebox.showerror("Ошибка", f"Не удалось открыть: {user_command}")

def open_commands_window():
    window = Toplevel(root)
    window.title("Добавить команду")
    window.geometry(ADD_WINDOW_SIZE)
    window.configure(bg=BG_COLOR)
    window.resizable(False, False)

    Label(window, text="Укажите имя команды:", 
          bg=BG_COLOR, fg=FG_COLOR, font=FONT_NORMAL).pack(anchor='w', padx=20, pady=(20, 0))
    
    command_frame = Frame(window, bg=ENTRY_BG, highlightbackground='#555555', 
                         highlightthickness=1)
    command_frame.pack(anchor='w', pady=5, padx=20)
    entry_command = Entry(command_frame, width=50, font=FONT_NORMAL,
                         bg=ENTRY_BG, fg=ENTRY_FG, insertbackground=FG_COLOR,
                         relief='flat', borderwidth=0)
    entry_command.pack(pady=6, padx=8, ipady=3)
    entry_command.focus_set()

    Label(window, text="Введите путь к файлу:", 
          bg=BG_COLOR, fg=FG_COLOR, font=FONT_NORMAL).pack(anchor='w', padx=20, pady=(8, 0))
    
    path_frame = Frame(window, bg=ENTRY_BG, highlightbackground='#555555', 
                      highlightthickness=1)
    path_frame.pack(anchor='w', pady=5, padx=20)
    entry_path = Entry(path_frame, width=50, font=FONT_NORMAL,
                      bg=ENTRY_BG, fg=ENTRY_FG, insertbackground=FG_COLOR,
                      relief='flat', borderwidth=0)
    entry_path.pack(pady=6, padx=8, ipady=3)

    def add_command():
        new_command_name = entry_command.get().strip().lower()
        new_command_path = entry_path.get().strip()

        if new_command_name and new_command_path:
            commands[new_command_name] = new_command_path

            with open("commands.json", "w", encoding="utf-8") as file:
                json.dump(commands, file, ensure_ascii=False, indent=4)
            messagebox.showinfo("Успех", "Команда добавлена!")
            window.destroy()
        else:
            messagebox.showwarning("Внимание", "Пожалуйста, заполните оба поля!")

    Button(window, text="Добавить", command=add_command,
           bg=BUTTON_BG, fg=BUTTON_FG, font=FONT_BUTTON,
           padx=40, pady=8, cursor='hand2', relief='flat').pack(pady=15)

root = Tk()
root.title("Command Launcher")
root.geometry(MAIN_WINDOW_SIZE)
root.configure(bg=BG_COLOR)
root.resizable(False, False)

label = Label(root, text="Введите команду", 
             bg=BG_COLOR, fg=FG_COLOR, font=FONT_TITLE)
label.pack(pady=(16, 6))

search_frame = Frame(root, bg=ENTRY_BG, highlightbackground='#555555', 
                    highlightthickness=1)
search_frame.pack(pady=10, padx=30)

entry = Entry(search_frame, width=35, font=FONT_NORMAL,
             bg=ENTRY_BG, fg=ENTRY_FG, insertbackground=FG_COLOR,
             relief='flat', borderwidth=0)
entry.pack(pady=8, padx=8, ipady=5)
entry.bind("<Return>", lambda event: start_search())
entry.focus()

buttons_frame = Frame(root, bg=BG_COLOR)
buttons_frame.pack(pady=10)

Button(buttons_frame, text="Выполнить", command=start_search,
       bg=BUTTON_BG, fg=BUTTON_FG, font=FONT_BUTTON,
       padx=15, pady=5, cursor='hand2', relief='flat').pack(side=LEFT, padx=5)

Button(buttons_frame, text="Укажите имя команды", command=open_commands_window,
       bg=BUTTON_BG, fg=BUTTON_FG, font=FONT_BUTTON,
       padx=15, pady=5, cursor='hand2', relief='flat').pack(side=LEFT, padx=5)

root.mainloop()