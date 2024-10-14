import sys
from pathlib import Path
from colorama import Fore, Style


def print_directory_structure(directory, recursion):
    try:
        for item in directory.iterdir():
            indent = '    ' * recursion
            if item.is_dir():
                print(f"{indent}{Fore.BLUE}{item.name}{Style.RESET_ALL}/")
                print_directory_structure(item, recursion + 1)
            else:
                print(f"{indent}{Fore.GREEN}{item.name}")
    except PermissionError:
        print(f"{indent}{Fore.RED}No access to {item}{Style.RESET_ALL}")

def main():
    if len(sys.argv) < 2:
        print(f"{Fore.RED}Error: Directory path is not provided {Style.RESET_ALL}")
        sys.exit(1)

    directory_path = Path(sys.argv[1])

    if not directory_path.exists():
        print(f"{Fore.RED}Error: Provided path does not exist {Style.RESET_ALL}")
        sys.exit(1)
    if not directory_path.is_dir():
        print(f"{Fore.RED}Error: Provided path is not a directory {Style.RESET_ALL}")
        sys.exit(1)

    print(f"Directory structure {Fore.YELLOW}{directory_path}{Style.RESET_ALL}:")
    print_directory_structure(directory_path, 0)

if __name__ == "__main__":
    main()
