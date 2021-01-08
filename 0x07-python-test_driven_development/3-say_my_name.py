#!/usr/bin/python3
"""Define function say_my_name"""

def say_my_name(first_name, last_name=""):
    """
    Prints My name is <first name> <last name>
    Parameters:
        first_name (str)
        last_name (str): For default is a empty string.
    Return: None
    Raises:
        TypeError: When first_name is not a string.
        TypeError: When last_name is not a string.
    """

    #Validated inputs
    msg1 = "first_name must be a string"
    msg2 = "last_name must be a string"

    if type(first_name) != str:
        raise TypeError(msg1)
    if type(last_name) != str:
        raise TypeError(msg2)

    print("My name is {} {}".format(first_name, last_name))