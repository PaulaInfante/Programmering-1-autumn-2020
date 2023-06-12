def reverseString(s):
    reverseString = ""
    """
    Denne funkjonen tar inn en string som et argument og retunerer stringen reversert.
    """
    for character in s[::-1]:
        reverseString += character

    return reverseString


print(reverseString("Hallo"))