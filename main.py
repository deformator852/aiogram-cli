from create_project import init_project  # pyright:ignore
import argparse


def main():
    try:
        parser = argparse.ArgumentParser(description="Arguments parser")
        parser.add_argument("-cp", "--project_name", type=str, help="Create project")
        parser.add_argument("-cr", "--router_name", type=str, help="Create router")
        args = parser.parse_args()
        if args.project_name:
            init_project(args.project_name)
    except Exception as e:
        print(f" [-] {e} [-] ")


if __name__ == "__main__":
    main()
