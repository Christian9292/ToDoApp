from FunctiiTODO import main_menu, todo_last, todo_new, all_todo

u_choice = main_menu()

while u_choice != "0":
    if u_choice == "1":
        todo_last()
    elif u_choice == "2":
        todo_new()
    elif u_choice == "3":
        all_todo()
    else:
        print("ERROR!")
    u_choice = main_menu()








