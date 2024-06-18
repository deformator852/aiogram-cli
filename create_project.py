from project_init import keyboards, main, create_bot, states  # pyright:ignore
import os


def init_project(project_name):
    os.mkdir(project_name)
    project_path = os.path.abspath(project_name)
    os.mkdir(project_name + "/routes")
    keyboards.create_keyboards(project_path)
    main.create_main(project_path)
    create_bot.create_bot(project_path)
    states.create_states(project_path)
    with open(project_path + "/utils.py","w") as file:
        pass
    print(f"[+] {project_path} created [+]")
