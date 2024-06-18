import os


def create_states(project_path):
    with open(project_path + "/states.py", "w") as file:
        file.write("""from aiogram.fsm.state import State, StatesGroup""")
