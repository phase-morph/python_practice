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