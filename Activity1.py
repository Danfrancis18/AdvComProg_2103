father_name = input("Enter your father's name: ")
birthplace = input("Enter your father's birthplace: ")
birthday = input("Enter your father's birthday (YYYY-MM-DD): ")

birth_year = int(birthday.split("-")[0])
current_year = int(input("Enter the current year: "))
age = current_year - birth_year

print(f"Father's Name: {father_name}")
print(f"Birthplace: {birthplace}")
print(f"Age: {age} years")
