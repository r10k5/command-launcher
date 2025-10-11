import json

def read_commands():
    with open("commands.json", "r", encoding="utf-8") as file:
        commands = json.load(file)
    return commands
    
def write_commands(commands):
    with open("commands.json", "w", encoding="utf-8") as file:
        json.dump(commands, file, ensure_ascii=False, indent=4)