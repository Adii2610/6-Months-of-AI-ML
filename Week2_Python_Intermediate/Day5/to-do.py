with open(r'D:\I Can Do\6-Months-of-AI-ML\Week2_Python_Intermediate\Day5\to-do.txt','r') as f:
    print(f.read())


def add_task(a):
    with open(r'D:\I Can Do\6-Months-of-AI-ML\Week2_Python_Intermediate\Day5\to-do.txt','a') as f:
        f.write(f"\n{a}")

def show_task():
    with open(r'D:\I Can Do\6-Months-of-AI-ML\Week2_Python_Intermediate\Day5\to-do.txt','r') as f:
        tasks = f.readlines()
        number = 1

        for task in tasks:
            print(number, task,end='')
            number += 1
    print("\n")

    
def delete_task():
    with open(r'D:\I Can Do\6-Months-of-AI-ML\Week2_Python_Intermediate\Day5\to-do.txt', 'r') as f:
        tasks = f.readlines()

    if len(tasks) == 0:
        print("No tasks available!")
        return

    for i in range(len(tasks)):
        print(f"{i + 1}. {tasks[i]}", end="")

    print()

    n = int(input("Enter task number to delete: "))

    if n < 1 or n > len(tasks):
        print("Invalid task number!")
        return

    tasks.pop(n - 1)

    with open(r'D:\I Can Do\6-Months-of-AI-ML\Week2_Python_Intermediate\Day5\to-do.txt', 'w') as f:
        for task in tasks:
            f.write(task)

    print("Task deleted successfully!")
    
    

while True:
    print("==================== TO DO LIST ====================")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Show Task")
    print("4. Exit")


    choice = int(input("Choice is yours: "))

    if choice == 1:
        a = input(f"Add task: ")
        add_task(a)

    elif choice == 2:
         delete_task()


    elif choice == 3:
         show_task()

    elif choice == 4:
         print(f"Thank you for using my application!! ")
         print(f"Goodbye")
         break

    else:
        print("Invalid input choice from the menu")