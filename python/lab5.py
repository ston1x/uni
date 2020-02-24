import random

def main():
    print("Select an input method \n"
          ,"1 - Keyboard input \n"
          ,"2 - Random numbers \n"
          ,"3 - Exit")
    mode = int(input())

    if mode == 1:
        keyboard_input()
    elif mode == 2:
        random_mode()
    else:
        exit(0)

def keyboard_input():
    print("Please enter a lists of items separated by a comma(,)")
    resultIsOK = True
    try:
        first_collection = set(map(str,input("First Collection : ").strip(',').split(',')))
        second_collection = set(map(str,input("Second Collection : ").strip(',').split(',')))
    except:
        print("You entered values ignoring the conditions.")
        resultIsOK = False

    if resultIsOK == True:
        calculate_collections(first_collection,second_collection)
    show_extra_menu(keyboard_input)

Mode2InvalidMessage = "You entered an invalid value, please enter the number(maximum number of items)."

def random_mode():
    print("Please enter the number of items.")
    try:
        count = int(input())
    except:
        print(Mode2InvalidMessage)
        show_extra_menu(random_mode)

    if count < 0:
        print(Mode2InvalidMessage)
        show_extra_menu(random_mode)

    calculate_collections(random_collection(count),random_collection(count))
    show_extra_menu(random_mode)

def random_collection(count):
    collection = set()
    for i in range(count):
        x = random.random() * 100
        collection.add(x)
    return collection

def calculate_collections(first_collection, second_collection):
    print("Calculations :")
    print("First collection : ", first_collection)
    print("Second collection : ", second_collection, "\n")
    print("Union: \n" ,first_collection.union(second_collection), "\n")
    print("Intersection: \n" , is_empty(first_collection.intersection(second_collection)), "\n")
    print("Difference: \n" ,is_empty(first_collection.difference(second_collection)),"\n")

def is_empty(collection):
    if len(collection) == 0:
        return "Empty"
    else:
        return collection

def show_extra_menu(function):
     print("1 - try one more time \n2 - exit to main menu")
     mode = int(input())

     if mode == 1:
        function()
     else:
        main()
     return

main()
