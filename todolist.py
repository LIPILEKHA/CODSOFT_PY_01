class todolist:
    def __init__(self):
        self.tasks[]
    def display(self):
        if not self.tasks:
            print("list is empty")
        else:
            print("To-do list")
            for index, task in enumerate(self.tasks , start=1):
                print(f"{index}.{task}")

