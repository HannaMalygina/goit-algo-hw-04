def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except ValueError:
        return "Please enter a name and a phone number with a space inbetween"

def change_contact(args, contacts):
    try:
        name, phone = args
        if name in contacts.keys():
            contacts[name] = phone
            return "Contact changed."
        else:
            contacts[name] = phone
            return f"Name {name} was not found in the contacts. I added a new contact."
    except ValueError:
        return "Please enter a name and a phone number with a space inbetween"

def phone(args, contacts):
    name = args[0]
    if name not in contacts.keys(): return f"Name {name} was not found in the contacts."
    else: return contacts[name]


def all(contacts):
    res_str = ""
    for key, item in contacts.items(): res_str += f"{key} : {item} \n"
    return res_str[:-2:] 

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(phone(args, contacts))
        elif command == "all":
            print(all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
