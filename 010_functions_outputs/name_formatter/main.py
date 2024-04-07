def format_name(first_name, last_name):
    first_name = first_name.strip()
    last_name = last_name.strip()
    if not first_name or not last_name:
        return "You didn't provide valid inputs."
    return f"{first_name.title()} {last_name.title()}"

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")

print(format_name(first_name, last_name))

