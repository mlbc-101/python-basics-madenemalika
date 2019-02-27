"""
Write a program which will find and display all such numbers which 
are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
"""

def solutionProblemOne(n1,n2,start,end):
    count=0 
    for x in range(start,end+1):
        if(n1%7==0 and x%n2!=0):
            count+=1
    return count
            
            
print(solutionProblemOne(7,5,2000,3200))

           
    
    
    
    
    