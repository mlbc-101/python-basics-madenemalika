"""Write a program that solves second degree equation of the form ax^2 +bx + c = 0."""
import math

def secondDegreeEquationSolver(a,b,c):
    result = []
    if(a==0):
        if(b==0):
            if(c==0):
                
            
               return "all the real numbers" 
            else:
                #c not equal to 0
                return "no solution"
        else:
          #b not equal to 0 
          return -c/b
    else:
        #a not equal to 0
        delta=b**2-4*a*c
        if(delta<0):
            return "no solution in R"
        else:
            if(delta==0):
                x=-b/(2*a)
                result.append(x)
                return result
            else:
                x1=(-b-math.sqrt(delta))/(2*a)
                x2=(-b+math.sqrt(delta))/(2*a)
                result.append(x1)
                result.append(x2)
                return result
                        
print(secondDegreeEquationSolver(2,-1,-6))
print(secondDegreeEquationSolver(1,-2,1))
print(secondDegreeEquationSolver(1,1,1))
print(secondDegreeEquationSolver(0,0,0))
print(secondDegreeEquationSolver(0,0,1))
print(secondDegreeEquationSolver(0,2,-1))

                
        
        