def add_again():
    ur_choice_2_add = input("\nDo you want to add again? (Y/N): ")
    if (ur_choice_2_add == "Y" or ur_choice_2_add == "y"):
        add()
    else:
        import Animos_main_program
        Animos_main_program.menu()
        Animos_main_program.yourchoice()

list_of_identification = []
list_of_names = []
def add():
    print("\nYou are Adding A Student Record\nPlease provide Information")
    list_of_identification.append(input("Student ID: "))
    list_of_names.append(input("Student Name: "))
    print("\nSuccessfully Saved")
    add_again()
