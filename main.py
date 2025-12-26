my_contacts = {}
def add_info(name,phone):
  my_contacts[name] = phone
  print(f"Contact has been updated!")
def show_info():
    if name not in my_contacts:
        print("your list is empty!")
    else:
        for key, value in my_contacts.items():
            print(f"Your Contacts is ")
            print(f" Name :{key} | Phone: {value}")
            print(f" ------------------------\n")
def search_contacts():
  name = input("write a name to search")
  if name in my_contacts:
    print(f"heres your search resluts: {name} ==> {my_contacts[name]}")
def main():
    print("Welcome, what do you want to do? \n")
    Is_running = True
    while Is_running:
        
        print("For adding info type (add), For showing exisitng info (show), For quitting the program (quit) or (q)")
        user_input = input(">")
        if user_input.lower() == "quit":
            print("goodbye")
            Is_running = False
        if user_input.lower() == "add":
            while True:
                user_name = input("Enter your name: ").strip()
                if not user_name.isalpha():
                    print("only alphapetics")
                    continue
                else:
                    break
            while True:
                user_phone = input("Enter your phone: ")
                if not user_phone.isdigit():
                    print("only digits")
                    continue
                if len(user_phone) != 11:
                    print("please enter a valid phone number of 11")
                    continue
                else:
                    break
            add_info(user_name, user_phone)
        if user_input.lower() == "show":
            show_info()
        elif user_input == "search":
            
            search_contacts()
            


      
  
if __name__ == '__main__':
  main()
