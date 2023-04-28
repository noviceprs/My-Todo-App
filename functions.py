FILEPATH = 'Todoitems.txt'


def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as todo_file:
        todos_local = todo_file.readlines()
        return todos_local


def write_todos(todos, filepath=FILEPATH):
    with open(filepath, 'w') as todo_file:
        todo_file.writelines(todos)
