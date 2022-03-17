# with open('readme.txt', 'a') as f:
#     f.write(name)

def intro(name):
    print("  ___________________________________________ ")
    print("                Contact book                ")
    print("  ___________________________________________ ")
    print(f"                 Name:{name}                ")
    print("  ___________________________________________ ")


def orders():
    print('-Press 1 to add a new entry-')
    print('-Press 2 to find a contact-')
    print('-Press 3 to delete a old entry-')
    command=input('Command:')
    return command

print('If you dont have a contact book it will automaticly be created for you when you enter a name')
name=input('Contact book name:')
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
        print('{Please enter the credentials for the entry you want to delete}')
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
        #delete search cntent if you wish to output on the txt file
        # with open(f"{name}.txt", "r") as f:
        #     lines = f.readlines()
        # with open(f"{name}.txt", "w") as f:
        #     for line in lines:
        #         if line.find('#') == -1 or line.find('Search') == -1:
        #             f.write(line)
