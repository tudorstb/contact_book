import os
def intro(name):
    print("  ___________________________________________ ")
    print("                Contact book                ")
    print("  ___________________________________________ ")
    print(f"                 Name:{name}                ")
    print("  ___________________________________________ ")

def orders():
    print('-------------------------------')
    print('-Press 1 to add a new entry----')
    print('-------------------------------')
    print('-Press 2 to find a contact ----')
    print('-------------------------------')
    print('-Press 3 to delete a old entry-')
    print('-------------------------------')
    do=input(f'Command for "{name}" contact book:')
    return do

def orders_contact_book():
    print('----------------------------------------------')
    print('-Press 1 to acces an existing contact book----')
    print('----------------------------------------------')
    print('-Press 2 to create a new contact book --------')
    print('----------------------------------------------')
    print('-Press 3 to delete a old contact book---------')
    print('----------------------------------------------')
    command=input('Command:')
    return command

redo_name='r'

while redo_name=='r' or redo_name=='R':
    do_contact_book = orders_contact_book()
    if do_contact_book=='1':
        name=input('Contact book name:')
        if os.path.exists(f"{name}.txt"):
            intro(name)
            redo="r"
            while redo=="r" or redo=="R":
                do=orders()
                if do=="1":
                    entry_first_name=input('First name:')
                    entry_last_name=input('Last name:')
                    tel_nr=input('Number:')
                    with open(f'{name}.txt', 'a') as f:
                        f.write(f'{entry_first_name}-{entry_last_name}:{tel_nr}\n')
                    redo=input("If you wish to make another option press (R) key:")
                elif do=='3':
                    print('{Please enter the credentials for the entry you want to delete->}')
                    entry_first_name = input('First name:')
                    entry_last_name = input('Last name:')
                    tel_nr = input('Number:')

                    with open(f"{name}.txt", "r") as f:
                        lines = f.readlines()
                    with open(f"{name}.txt", "w") as f:
                        for line in lines:
                            if line.find(f'{entry_first_name}-{entry_last_name}:{tel_nr}') == -1:
                                f.write(line)
                    redo = input("If you wish to make another option press (R) key:")
                elif do=='2':
                    count_find=False
                    find=input('Find contact:')
                    with open(f"{name}.txt", "r") as f:
                        lines = f.readlines()
                    print(f'Search for {find}:')
                    with open(f"{name}.txt", "a") as f:
                        for line in lines:
                            if line.find(f'{find}') != -1:
                                print(f'#{line}')
                                count_find=True
                    if count_find==False:
                        print(f'There is no contact containing "{find}"')

                    redo = input("If you wish to make another option press (R) key:")
                else:
                    print("You did not select a valid option")
                    redo=input("If you wish to make another option press (R) key:")
            redo_name = input('If you wish to go back to the main menu press (R)')
                    #delete search cntent if you wish to output on the txt file
                    # with open(f"{name}.txt", "r") as f:
                    #     lines = f.readlines()
                    # with open(f"{name}.txt", "w") as f:
                    #     for line in lines:
                    #         if line.find('#') == -1 or line.find('Search') == -1:

                    #             f.write(line)

        else:
            print(f'There is no contact book named:{name}')
            redo_name=input('If you wish to add a new contact book pres (R) and the choose option "2":')
    elif do_contact_book=='2':
        name = input('New contact book name:')
        with open(f'{name}.txt', 'w') as f:
            f.write('')
        print("For the new contact book to be avalable please re-run the project")
        redo_name = input('If you wish to go back to the main menu press (R)')
    elif do_contact_book=='3':
        delete_contact_book=input(f"Enter the name of the contact book you would wish to remove:")
        os.remove(f"{delete_contact_book}.txt")
        redo_name=input('If you wish to go back to the main menu press (R)')
    else:
        print("You did not select a valid option")
        redo_name = input('If you wish to go back to the main menu press (R)')



