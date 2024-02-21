
import csv

pokemons = []

# https://www.w3schools.com/python/python_file_handling.asp
# https://www.w3schools.in/python/file-handling
with open('pokemon.csv', newline='') as csv_file:
    file_reader = csv.reader(csv_file, delimiter = ',', quotechar='|')

    for row in file_reader:
        pokemons.append(row[0])

# print(pokemons)

print("Pokemon list command:")

while True:
    print("1. Get pokemon by sequence number")
    print("2. Sort by A-Z")
    print("3. Sort by Z-A")
    print("4. Search by text in name")
    print("5. Search by length of name")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        pokemon_seq = int(input("Which pokemon would you like to choose?"))
        print(pokemons[pokemon_seq])
        # https://www.w3schools.com/python/python_lists_access.asp
        pass
    elif choice == '2':
        pokemons.sort()
        print(pokemons)
        # https://www.w3schools.com/python/python_lists_sort.asp
        pass
    elif choice == '3':
        pokemons.sort(reverse = True)
        print(pokemons)
        # https://www.w3schools.com/python/python_lists_sort.asp
        pass
    elif choice == '4':
        pokemon_search = str(input("By which letters would you like to search?"))
        new_list = []
        for x in pokemons:
            if pokemon_search in x:
               new_list.append(x)

        print(new_list)
        # https://www.w3schools.com/python/python_lists_comprehension.asp
        # https://www.w3schools.com/python/ref_string_startswith.asp
        pass
    elif choice == '5':
        pokemon_search2 = int(input("How many letters do you want your pokemon to be?"))
        new_list2 = [x for x in pokemons if len(x) == pokemon_search2]
        print(new_list2)
        # https://www.w3schools.com/python/python_lists_comprehension.asp
        pass
    elif choice == '6':
        print("Exiting")
        break
    else:
        print("Invalid choice, choose from 1 to 6")

    print("==========================")
