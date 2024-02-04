from pathlib import Path

users_input = input("Enter the string: ")
counter = 0

src_root = Path(__file__).parent
file_name = src_root / "rockyou.txt"

with open(file_name, mode="rt", encoding="latin-1") as file:
    content = file.readlines()
    for i in content:
        if users_input == i.strip("\n"):
            counter += 1

print(f"You've entered: {users_input}, it appears {counter} times in rockyou.txt file")
