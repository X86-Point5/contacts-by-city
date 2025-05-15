#InputHandler.py
"""
Console Input Operations Handler (InputHandler.py)

Provides a range of functions meant for dealing with console inputs

Features:
-Validates Integer, Floating Point, String, and Single Character Input
-Includes Bounds Checking On Input
-Validates Date Input
-Includes the Option to Allow Only for Certain Characters
-Includes the Option to Only Allow for Selected Strings
"""

__author__ = "Maximus Barraza (Github: X86-Point5)"
__verison__ = "1.1.0"
__date__ = "2025-05-15"

#used for validating date input
import datetime




def input_integer(prompt: str = "\n\tEnter an integer: ",
                  lower_bound: int = 0,
                  upper_bound: int = 32767,
                  inclusion: bool = True) -> int:
    """
    Prompts the user to enter an integer and validates it against specified bounds.

    The function continuously prompts the user until a valid integer within the
    defined range (inclusive or exclusive) is entered. It handles non-integer
    inputs by displaying an error message and re-prompting.

    Args:
        prompt (str, optional): The message displayed to the user when asking for input.
            Defaults to "\\n\\tEnter an integer: ".
        lower_bound (int, optional): The lower limit for the integer value.
            Defaults to 0.
        upper_bound (int, optional): The upper limit for the integer value.
            Defaults to 32767.
        inclusion (bool, optional): Determines if the bounds are inclusive or exclusive.
            If True, the range includes `lower_bound` and `upper_bound` (<=, >=).
            If False, the range excludes `lower_bound` and `upper_bound` (<, >).
            Defaults to True.

    Returns:
        int: The validated integer value entered by the user that falls within
             the specified bounds.

    Raises:
        None
    """

    #Loops continuously until a an integer with in range is given
    while True:

        #Attempts to cast the console input to an integer.
        #If this fails the loop repeats
        try:

            #Casts a prompt entry to an integer
            return_val = int(input(prompt))

            if inclusion:
                #If inclusion is on the bounds then input must be in between
                #the bounds inclusive
                condition = lower_bound <= return_val <= upper_bound
                #Sets the error output to inclusive
                bound_type = "inclusive"
            else:
                #If there is no inclusion on the bounds then the input must
                #be in between the bounds exclusive
                condition = lower_bound < return_val < upper_bound
                #Sets the error output to be exclusive
                bound_type = "exclusive"

            #If the return_val is with in range then it is returned, other wise
            #an error message is outputed regarding the bounds
            if condition:
                return return_val
            else:
                print(f"\tERROR - Value must be in between {lower_bound} and {upper_bound} {bound_type}")

        except ValueError:
            #Incase the user did not input an integer convertible value
            print("\tERROR - Only integer values can be entered")




def input_float(prompt: str = "\n\tEnter a decimal value: ", lower_bound: float = 0.0, 
                upper_bound: float = 32767.0, inclusion: bool = True) -> float:
    """
    Prompts the user to enter a float and validates it against specified bounds.

    The function continuously prompts the user until a valid float within the
    defined range (inclusive or exclusive) is entered. It handles non-float
    inputs by displaying an error message and re-prompting.

    Args:
        prompt (str, optional): The message displayed to the user when asking for input.
            Defaults to a prompt suitable for float input (e.g., "\\n\\tEnter a decimal value: ").
        lower_bound (float, optional): The lower limit for the float value.
            Defaults to 0.0.
        upper_bound (float, optional): The upper limit for the float value.
            Defaults to 32767.0.
        inclusion (bool, optional): Determines if the bounds are inclusive or exclusive.
            If True, the range includes `lower_bound` and `upper_bound` (<=, >=).
            If False, the range excludes `lower_bound` and `upper_bound` (<, >).
            Defaults to True.

    Returns:
        float: The validated float value entered by the user that falls within
               the specified bounds.

    Raises:
        None
    """

    #Loops until the user inputs a string that is within the range of the bounds
    #and convertible to a floating point
    while True:

        #Attempts to cast the console input to a float.
        #If this fails the loop repeats.
        try:

            #Casts the prompt entry to a float
            return_val = float(input(prompt))

            if inclusion:
                #If inclusion is on the bounds then input must be in between
                #the bounds inclusive
                condition = lower_bound <= return_val <= upper_bound
                #Sets the error output to inclusive
                bound_type = "inclusive"
            else:
                #If there is no inclusion on the bounds then the input must
                #be in between the bounds exclusive
                condition = lower_bound < return_val < upper_bound
                #Sets the error output to be exclusive
                bound_type = "exclusive"

            #If the return_val is with in range then it is returned, other wise
            #an error message is outputed regarding the bounds
            if condition:
                return return_val
            else:
                print(f"\tERROR - Value must be in between {lower_bound} and {upper_bound} {bound_type}")

        except ValueError:
            #Incase the user did not input a float convertible value
            print("\tERROR - Only floating point values can be entered")


def input_char(prompt: str = "\n\tEnter a character: ", valid_chars: str = "", 
               to_caps: bool = True) -> str:
    """
    Prompts the user to enter a single character and optionally validates it.

    The function continuously prompts the user until a valid character is entered.
    It takes the first character of the user's input. If `valid_chars` is provided,
    the input character must be one of them (case-insensitively if `to_caps` is True).
    The returned character can also be forced to uppercase.

    Note: If the user provides an empty input (e.g., presses Enter), they will be
    re-prompted without the original `prompt` message until a non-empty string is entered.
    Only the first character of the non-empty string is processed.

    Args:
        prompt (str, optional): The message displayed to the user.
            Defaults to "\\n\\tEnter a character: ".
        valid_chars (str, optional): A string containing all valid characters.
            If empty, any character is considered valid. Defaults to "".
        to_caps (bool, optional): If True, the input character and `valid_chars`
            are converted to uppercase for comparison, and the returned character
            will be uppercase. If False, comparisons are case-sensitive and the
            returned character retains its original case (unless it was among
            originally uppercase `valid_chars`). Defaults to True.

    Returns:
        str: The validated single character entered by the user.

    Raises:
        None
    """
    #Incase the input is meant to be uppercased then the library
    #of valid characters will also be uppercased
    if to_caps:
        valid_chars = valid_chars.upper()

    #Loops until the user inputs the correct character value
    while True:

        #gets the string input from the user
        base_input = input(prompt)

        #if the user presses enter the user is forced to still input a character
        while base_input == "":
            base_input = input()

        #parses only for the first character in the inputted string
        return_val = base_input[0]

        #capitalizes the return value if necessary
        if to_caps:
            return_val = return_val.upper()

        #Checks if the return value has a requirement or if it suffices that
        #requirement. If not then an error message is produced and loop starts over.
        if not valid_chars or return_val in valid_chars:
            return return_val
        else:
            print(f'\tERROR - Character must be one of these "{valid_chars}" characters\n')




def input_string_date(prompt: str = "\n\tEnter a data in the format (MM/DD/YYYY): ") -> str:
    """
    Prompts the user to enter a date string in MM/DD/YYYY format and validates it.

    The function continuously prompts the user until a string that represents a
    valid date in the "MM/DD/YYYY" format is entered. If the input string
    cannot be parsed into a valid date (e.g., incorrect format, invalid day/month),
    an error message is displayed, and the user is re-prompted.

    Args:
        prompt (str, optional): The message displayed to the user when asking for input.
            Defaults to "\\n\\tEnter a data in the format (MM/DD/YYYY): ".

    Returns:
        str: The validated date string as entered by the user in MM/DD/YYYY format.

    Raises:
        None
    """

    #Loops until a date in proper format is given
    while True:

        #Gets the input from the user
        input_string = input(prompt)
        try:
            #Attempts to construct a date from the string
            datetime.datetime.strptime(input_string, "%m/%d/%Y")

            #If a date can be constructed then the string is returned
            return input_string

        except ValueError:
            #If a date can not be constructed then an error is outputed
            #and the loop repeats
            print("\tERROR - Invalid date format or value. Please use MM/DD/YYYY and enter a valid date.\n")




def input_tuple_date(prompt: str = "\n\tEnter a data in the format (MM/DD/YYYY): ") -> tuple[int, int, int]:
    """
    Prompts the user for a date string, validates it, and returns components as a tuple.

    The function continuously prompts the user to enter a date string in the
    "MM/DD/YYYY" format. If the input is a valid date, its month, day, and year
    are returned as a tuple of integers. If the input string cannot be parsed
    into a valid date (e.g., incorrect format, invalid day/month values), an
    error message is displayed, and the user is re-prompted.

    Args:
        prompt (str, optional): The message displayed to the user when asking for input.
            Defaults to "\\n\\tEnter a data in the format (MM/DD/YYYY): ".

    Returns:
        tuple[int, int, int]: A tuple containing the month, day, and year
        (in that order) as integers, extracted from the validated date string.
        For example, (5, 15, 2025) for May 15, 2025.

    Raises:
        None
    """

    #Loops until a date in proper format is given
    while True:

        #Gets the input from the user
        input_string = input(prompt)
        try:

            #Attempts to construct a date object from the string
            date_obj = datetime.datetime.strptime(input_string, "%m/%d/%Y")

            #If the object can be constructed then the tuple containing
            #the date's member data is returned
            return(date_obj.month, date_obj.day, date_obj.year)

        except ValueError:
            #If a date can not be constructed then an error is outputed
            #and the loop repeats
            print("\tERROR - Invalid date format or value. Please use MM/DD/YYYY and enter a valid date.\n")
  
            


def input_string(prompt: str = "\n\tEnter a string: ", banned_strings: list = [],
                error_output: str = "\tERROR - Input not allowed.\n") -> str:

    """Gets a string input from the user, with an option to ban certain strings.

    This function will continuously prompt the user for input until a string is
    entered that is not in the `banned_strings` list.

    Args:
        prompt (str, optional): The message displayed to the user when asking for input.
            Defaults to "\n\tEnter a string: ".
        banned_strings (list, optional): A list of strings that are not allowed as input.
            If the user enters a string from this list, the `error_output` message
            will be displayed, and they will be prompted again. Defaults to an empty list,
            meaning no strings are banned.
        error_output (str, optional): The message displayed to the user if they enter
            a banned string. Defaults to "\tERROR - Input not allowed.\n".

    Returns:
        str: The string entered by the user that is not in the `banned_strings` list.
    """

    #loops until the string given is correct
    while True:

        #takes the string from the user
        return_string = input(prompt)

        #Checks to make sure there is no banned string or that return_string
        #is not a banned string. If the return_string is banned then the error
        #message is outputted.
        if not banned_strings or not return_string in banned_strings:
            return return_string
        else:
            print(error_output)



