
duplicates = []

def check_for_single_number(array):

    for element in array:
        if array.count(element) > 1:
            duplicates.append(element)

    for element in array:
        if element not in duplicates:
            return element


print(check_for_single_number([4,1,2,1,2]))