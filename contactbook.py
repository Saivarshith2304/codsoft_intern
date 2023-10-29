contact = {}

def display():
    print("name \t\t contact number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))

while True:
    print("\n.....................CONTACT BOOK....................\n1.ADD CONTACT \n2.SEARCH CONTACT \n3.DISPLAY CONTACT \n4.EDIT CONTACT \n5.DELETE \n6.EXIT")
    print(".....................................................")
    choice = int(input("ENTER YOUR CHOICE : "))
    if choice == 1:
        name = input("enter name of contact: ")
        phno = int(input("enter phone number: "))
        contact[name]=phno

    elif choice == 2:
        search =input("enter the contact number: ")
        if search in contact:
            print(search,"'s contact no is ",contact[search])
        else:
            print("name not found...!")

    elif choice == 3:
        if not contact:
            print("empty contact book")
        else:
            display()
    elif choice == 4:
        edit_cont=input("enter the contact to be edited: ")
        if edit_cont in contact:
            phno = int(input("enter mobile number: "))
            contact[edit_cont]=phno
            print("contact updated...")
            display()

    elif choice==5:
        delete=input("enter contact to be deleted: ")
        if delete in contact:
            confirm = input("do u want to delete this contact (y/n):")
            if confirm=='y' or confirm=='Y':
                contact.pop(delete)
            display()
        else:
            print("name is not found...!")

    else:
        break
