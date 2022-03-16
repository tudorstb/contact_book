def intro(name):
    print("  ___________________________________________ ")
    print("                Contact book                ")
    print("  ___________________________________________ ")
    print(f"                 Owner:{name}                ")
    print("  ___________________________________________ ")

name=input('To open a new contact book:')
intro(name)
with open('readme.txt', 'a') as f:
    f.write(name)