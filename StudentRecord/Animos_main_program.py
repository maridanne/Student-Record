import os
from sys import path
path.append('C:\\Users\\Blessy Ardie\\Desktop\\StudentRecord\\AddRecord\\Animos_add_module.py')
path.append('C:\\Users\\Blessy Ardie\\Desktop\\StudentRecord\\ViewRecord\\Animos_view_module.py')
path.append('C:\\Users\\Blessy Ardie\\Desktop\\StudentRecord\\ExitProgram\\Animos_exit_module.py')

def menu():
   print('''STUDENT RECORD MENU
  [1] - ADD
  [4] - VIEW
  [5] - EXIT
  ''')
def yourchoice():
    try:
        ch = int(input("Please Enter your choice: "))
    except ValueError:
        print("\nPlease select from the options above.")
        menu()
    else:
        print("\n") 
        if (ch == 1):
            import AddRecord.Animos_add_module
            AddRecord.Animos_add_module.add()
        elif (ch == 4):
            import ViewRecord.Animos_view_module
            ViewRecord.Animos_view_module.view()
        elif (ch == 5):
            import ExitProgram.Animos_exit_module
            ExitProgram.Animos_exit_module.EXIT()
        else:
            print("Please select from the options above.")
            menu()

menu()
yourchoice()
