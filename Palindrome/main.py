'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''


def is_palindrome(input_string):
    # We'll create two string, to compare them
    new_string = ""
    reverse_string = ""
    # Traverse through each letter of the input string
    for el in input_string:
        # Add any non-blank letters to the
        # end of one string, and to the front
        # of the other string.
        if el == " ":
            continue
        new_string = new_string + el 
        reverse_string = el + reverse_string
    # Compare the strings
    if reverse_string.lower() == new_string.lower():
        return True
    return False
 
print (is_palindrome("Never Odd or Even")) # Should be True
print (is_palindrome("abc")) # Should be False
print (is_palindrome("kayak")) # Should be True
