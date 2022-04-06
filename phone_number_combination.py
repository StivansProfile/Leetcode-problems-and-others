import random
import time

numbers = [2,3,4,5,6,7,8,9]
letters = [
    ["a","b","c"],
    ["d","e","f"],
    ["g","h","i"],
    ["j","k","l"],
    ["m","n","o"],
    ["p","q","r","s"],
    ["t","u","v"],
    ["w","x","y","z"],
]

possible_combinations = []
len_of_comb_array = []

def possible_combination(digit1,digit2):

    i = True
    j = 0

    # Get the letters corresponding to the digits
    idx_of_digit_1 = numbers.index(digit1)
    idx_of_digit_2 = numbers.index(digit2)

    # Selecting random combinations until we have
    # all of the possible ones
    # we do that by checking if the last element of the combinations array is the
    # biggest lenght
    while i:
        choise_1 = random.choice(letters[idx_of_digit_1])
        choise_2 = random.choice(letters[idx_of_digit_2])

        comb = f"{choise_1}{choise_2}"
        possible_combinations.append(comb)

        possible_combinations_sorted = set(possible_combinations)

        len_of_comb_array.append(len(possible_combinations_sorted))

        j += 1

        if j == 50:
            if len_of_comb_array[-1] == max(len_of_comb_array):
                print(possible_combinations_sorted)
                i = False

possible_combination(2,3)