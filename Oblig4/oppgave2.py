import math
def pythagoras(a,b):
    """ 
    Denne funksjonen regner ut og retunerer hypotenusen i en trekant og tar inn katet1 og katet2 som argumenter.
    """
    return math.sqrt(math.pow(a,2) + math.pow(b,2))

#Test
print(pythagoras(10,5))