"""Write a program which can compute the factorial of a given numbers."""

def factoriel(n):
    if(n==0):
        return 1
    if(n==1):
        return 1
    else:
        return n*factoriel(n-1)
    

print(factoriel(7))
    