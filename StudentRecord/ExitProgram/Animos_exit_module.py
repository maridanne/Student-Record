def EXIT():
    ex = input("Are you sure you want to Exit (Y/N): ")
    if (ex == "Y" or ex == 'y'):
        import sys
        print("\nThank you for using my program")
        sys.exit()
    else:
        import Animos_main_program
        Animos_main_program.menu()
        Animos_main_program.yourchoice()
