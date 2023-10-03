SCRIPT_RULES = '\nEnter array from number, type number and click "Enter"\nTo stop adding elements write anything but number'

ARRAY_TYPE_ERROR = '\t\tError. Array must include at least 3 elements'

ENTER_NEW_VALUE = '\tEnter value of array you wanna set: '

VALUE_ERROR = '\t\tError. Enter existing value: '
VALUE_TYPE_ERROR = '\t\tError. Value can by only number'
VALUE_CHANGE = '\tEnter value of array you wanna change: '

INDEX_ERROR = '\t\tError. Enter existing index: '
INDEX_TYPE_ERROR = '\t\tError. Index can by only number'
INDEX_CHANGE = '\tEnter index of array you wanna change: '

CHOICE_RULES = '\nYou can change element of array by index (i) or by value (v)\n\tChoose your route: '
CHOICE_WARNING = ' \t\tError. Enter i or v: '

MIN_ARRAY_ELEMENTS = 3
MAX_ARRAY_ELEMENTS = 10


def printArray(array):
    print('\nYour array: ', array)


def changeNumByIndex(array):
    newArray = array

    oldNum = ''
    try:
        oldNum = int(input(INDEX_CHANGE))
    except ValueError:
        print(INDEX_TYPE_ERROR)
        exit()

    while oldNum > len(newArray) or oldNum < 1:
        oldNum = ''
        try:
            oldNum = int(input(INDEX_CHANGE))
        except ValueError:
            print(INDEX_TYPE_ERROR)
            exit()

    newNum = ''
    try:
        newNum = int(input(ENTER_NEW_VALUE))
    except ValueError:
        print(INDEX_TYPE_ERROR)
        exit()

    newArray[oldNum - 1] = newNum

    printArray(newArray)
    exit()


def changeNumByValue(array):
    newArray = array
    coincidence = False
    counter = 0

    oldNum = ''
    try:
        oldNum = int(input(VALUE_CHANGE))
    except ValueError:
        print(VALUE_TYPE_ERROR)
        exit()

    while not coincidence:
        for el in newArray:
            if oldNum == el:
                coincidence = True
        if not coincidence:
            oldNum = ''
            try:
                oldNum = int(input(VALUE_CHANGE))
            except ValueError:
                print(VALUE_TYPE_ERROR)
                exit()

    newNum = ''
    try:
        newNum = int(input(ENTER_NEW_VALUE))
    except ValueError:
        print(VALUE_TYPE_ERROR)
        exit()

    for el in newArray:
        if el == oldNum:
            break
        else:
            counter += 1
    newArray.insert(counter, newNum)
    newArray.remove(oldNum)

    printArray(newArray)
    exit()


def choice(array):
    choice = input(CHOICE_RULES)
    while choice != 'i' and choice != 'v':
        choice = input(CHOICE_WARNING)

    if choice == 'i':
        changeNumByIndex(array)
    else:
        changeNumByValue(array)


def changeElementsToInt(array):
    newArray = []

    for el in array:
        newArray.append(int(el))

    printArray(newArray)
    choice(newArray)


def main():
    print(SCRIPT_RULES)
    array = []
    enterArray = True

    while enterArray:
        el = input('\tPrint array element: ')
        if not el.isnumeric():
            if len(array) < MIN_ARRAY_ELEMENTS:
                print(ARRAY_TYPE_ERROR)
                continue
            else:
                enterArray = False
        else:
            array.append(el)
            if len(array) >= MAX_ARRAY_ELEMENTS:
               break

    changeElementsToInt(array)


main()

if __name__ == '__main__':
    main()
