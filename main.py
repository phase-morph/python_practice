# Regular Python EDABIT practice #


# 40 (VH): A subtle switcheroo


# Examples:

# switcheroo("The elephants in France were chased by ants!") ➞ "The elephance in Frants were chased by ance!"

# switcheroo("While he rants, I fall into a trance...") ➞ "While he rance, I fall into a trants..."

# switcheroo("Bounced over the fence!") ➞ "Bounced over the fents!"

input_strings = ["ThNTSe elephaNTS in FraNCE were cNCEhased by aNTS!", "The elephaNTS in FraNCE were chased by aNTS!",
                 "While he raNTS, I fall into a traNCE...", "BouNCEd over the feNCE!"]


def switcheroo(inp: str) -> str:
    lst = [word for word in inp.split(" ")]

    substring_1 = "NTS"
    substring_2 = "NCE"

    for i in range(len(lst)):

        # if substring_1 IS contained in the string lst[i] AND if the last character in the string == the last character
        # in substring_1 OR the string does NOT end with either a letter OR a number => True
        if (substring_1 in lst[i]
                and (lst[i][-1] == substring_1[-1] or (not lst[i][-1].isalpha() and not lst[i][-1].isnumeric()))):
            lst[i] = lst[i].replace(substring_1, substring_2)

        # if substring_2 IS contained in the string lst[i] AND if the last character in the string == the last character
        # in substring_2 OR the string does NOT end with either a letter OR a number => True
        elif (substring_2 in lst[i]
              and (lst[i][-1] == substring_2[-1] or (not lst[i][-1].isalpha() and not lst[i][-1].isnumeric()))):
            lst[i] = lst[i].replace(substring_2, substring_1)

        else:
            pass

    return " ".join(lst)


[print(switcheroo(phrase)) for phrase in input_strings]


# 41 (VH): Matrix Multiplication


# Examples:

# matrix_mult([[4, 2],[3, 1]], [[5, 6], [3, 8]]) ➞ [[26, 40], [18, 26]]

# matrix_mult([[3, 6],[4, 5]], [[8, 1], [7, 2]]) ➞ [[66, 15], [67, 14]]

# matrix_mult([[7, 5],[2, 2]], [[6, 7], [3, 2]]) ➞ [[57, 59], [18, 18]]

input_values = [[[4, 2], [3, 1]], [[5, 6], [3, 8]]]


def matrix_mult(lst: list):
    import numpy as np
    array_lst = []

    for matrix in lst:
        array_lst.append(np.array(matrix))

    return np.dot(array_lst[0], array_lst[1])


print(matrix_mult(input_values), type(matrix_mult(input_values)))


# 42 (VH): Identity Matrix


# Examples:

# id_mtrx(2) ➞ [
#   [1, 0],
#   [0, 1]
# ]

# id_mtrx(-2) ➞ [
#   [0, 1],
#   [1, 0]
# ]

# id_mtrx(0) ➞ []


def id_mtrx(input_int: int) -> list:
    id_matrix = []
    if input_int == 0:
        return []

    for i in range(abs(input_int)):

        child_matrix = []
        for j in range(abs(input_int)):
            if j == i:
                child_matrix.append(1)
            else:
                child_matrix.append(0)
        id_matrix.append(child_matrix)

    return id_matrix if input_int > 0 else list(reversed(id_matrix))


print(id_mtrx(-7))


# 43 (VH): Maximum and Minimum Product Triplets


# Examples:

# max_product([-8, -9, 1, 2, 7]) ➞ 504
#
# max_product([-8, 1, 2, 7, 9]) ➞ 126
#
# min_product([1, -1, 1, 1]) ➞ -1
#
# min_product([-5, -3, -1, 0, 4]) ➞ -15


def max_product(input_list: list, n: int) -> int:
    if n < 3:
        return -1

    _max_product = 0

    for i in range(0, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                _max_product = max(_max_product, input_list[i] * input_list[j] * input_list[k])

    return _max_product


for sample in [[-8, -9, 1, 2, 7], [-8, 1, 2, 7, 9]]:
    print(max_product(sample, len(sample)))


# (Misc.) Find the longest common prefix in a list of words


list_of_words = ["flower", "flow", "flight"]


def longest_common_prefix(input_list: list):
    import sys
    min_length = sys.maxsize
    index_of_min_length = 0

    for word in input_list:
        if len(word) < min_length:
            min_length = len(word)
            index_of_min_length = input_list.index(word)

    min_length_word = input_list[index_of_min_length]
    input_list.remove(min_length_word)
    longest_prefix = ""

    for char_pos in range(len(min_length_word)):
        is_common = True
        for word in input_list:
            if min_length_word[char_pos] != word[char_pos]:
                is_common = False
        if is_common:
            longest_prefix += min_length_word[char_pos]
        else:
            if longest_prefix == "":
                return "There is no common prefix between these words."
    return longest_prefix


print(longest_common_prefix(list_of_words))


# (Misc.) Find the first double occurring character


word = "appointment"


for char_pos in range(len(word)):
    if char_pos == 0:
        if word[char_pos] == word[char_pos + 1]:
            print("{} is the first character occurring twice".format(word[char_pos]))
            break
    else:
        if word[char_pos] == word[char_pos - 1]:
            print("{} is the first character occurring twice".format(word[char_pos]))
            break


# 44 (EXP): SUBSTRINGS


# longest_substring("225424272163254474441338664823") ➞ "272163254"
# substrings = 254, 272163254, 474, 41, 38, 23
#
# longest_substring("594127169973391692147228678476") ➞ "16921472"
# substrings = 94127, 169, 16921472, 678, 476
#
# longest_substring("721449827599186159274227324466") ➞ "7214"
# substrings = 7214, 498, 27, 18, 61, 9274, 27, 32
# 7214 and 9274 have same length, but 7214 occurs first.


def build_substring_list(string: str) -> list:

    # Helper inner utility function
    def extract_substring(sliced_string: str) -> tuple:
        substring = sliced_string[0]

        # Handling edge cases
        if len(sliced_string) == 2 or len(sliced_string) == 3:
            return sliced_string, len(sliced_string)
        else:
            for _char_pos, _char in enumerate(sliced_string[1:]):
                if (int(sliced_string[_char_pos]) + int(sliced_string[_char_pos + 1])) % 2 != 0:
                    substring += sliced_string[_char_pos + 1]
                else:
                    return substring, len(substring)

    working_string = string[:]
    list_of_substrings = []
    iteration = 0

    for char_pos, char in enumerate(working_string):
        iteration += 1
        try:
            if (int(working_string[char_pos]) + int(working_string[char_pos + 1])) % 2 != 0:
                returned_tuple = extract_substring(working_string[char_pos:])
                list_of_substrings.append(returned_tuple[0])
                working_string = working_string[returned_tuple[1] - 1:]
            else:
                continue
        except IndexError:
            return list_of_substrings


print([
    build_substring_list(case) for case in ["225424272163254474441338664823",
                                            "594127169973391692147228678476",
                                            "721449827599186159274227324466"]
])
