def view():
    print("Student ID\t\tStudent Name")
    import AddRecord.Animos_add_module
    showStd = "\n".join("{}\t\t{}".format(x, y) for x, y in zip(AddRecord.Animos_add_module.list_of_identification, AddRecord.Animos_add_module.list_of_names))
    print(str(showStd))
    input("\n\nPress any key to go back to menu . . .")
    import Animos_main_program
    Animos_main_program.menu()
    Animos_main_program.yourchoice()
