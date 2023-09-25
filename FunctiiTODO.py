tasks = []

def main_menu():
    """Afiseaza meniul principal al aplicatiei ToDo si solicita optiunea utilizatorului.

    Ce returneaza:
        str: Optiunea utilizatorului sub forma de sir de caractere.
    """
    print("\nTODO APP")
    print("-" * 50)
    print("Menu:\n")
    print("1. Show last TODO")
    print("2. Add new TODO")
    print("3. Show all TODO")
    print("0. Exit\n")
    return input("Enter your choice and press ENTER:")

def todo_last():
    if tasks:
        last = tasks[-1]
        print(f"Last TODO: {last}")
    else:
        print("TODO list it's empty!")

def todo_new():
    todo = input("Add new TODO: ")
    tasks.append(todo)
    print(f"New TODO added: {todo}")

def all_todo():
    if tasks:
        all_tasks = tasks[:]       
        print(f"All TODO: {all_tasks}")
    else:
        print("TODO list it's empty!")