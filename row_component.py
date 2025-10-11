from tkinter import *
import json_manager
from style import *

commands = json_manager.read_commands()
rows = []

def create_row(command_name, command_path, root):
    row = Frame(root, bg=BG_COLOR, highlightbackground='#555555', highlightthickness=1)
    row.pack(pady=10, padx=30)

    command_name_label = Label(row, text=command_name, bg=BG_COLOR, fg=FG_COLOR, font=FONT_NORMAL)
    command_name_label.pack(side=LEFT, padx=10)

    command_path_label = Label(row, text=command_path, bg=BG_COLOR, fg=FG_COLOR, font=FONT_NORMAL)
    command_path_label.pack(side=LEFT, padx=10)

    delete_row_button = Button(row, text="Удалить", bg=BUTTON_BG, fg=BUTTON_FG, font=FONT_BUTTON, command=delete_row(row, command_name))
    delete_row_button.pack(side=LEFT, padx=10)

    rows.append(row)

def delete_row(row, command_name):
    def habdler_delete_row():
        commands.pop(command_name)
        json_manager.write_commands(commands)
        rows.remove(row)
        row.destroy()
    
    return habdler_delete_row

