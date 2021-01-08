#!/usr/bin/python3
"""Define function text_indentation"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :
    Parameters:
        text (str)
    Return: None
    Raises:
        TypeError: When text is not a string.
    """

    # Validated inputs
    msg1 = "text must be a string"

    if type(text) != str:
        raise TypeError(msg1)

    # Print
    separartors = [".", "?", ":", "\n"]
    indtext = ""
    c = 0

    while (c != len(text)):
        # Clean spaces at start
        for i in text[c:]:
            if i == " ":
                c += 1
            else:
                break
        # Indent text
        for i in text[c:]:
            if i in separartors:
                if i == '\n':
                    # Remove spaces before new line
                    spaces = 0
                    for j in indtext[::-1]:
                        if j == " ":
                            spaces -= 1
                        else:
                            if spaces == 0:
                                spaces = len(indtext)
                            break
                    indtext = indtext[:spaces]
                    indtext += i
                else:
                    indtext += i + '\n' + '\n'
                c += 1
                break
            else:
                indtext += i
                c += 1

    print(indtext, end="")
