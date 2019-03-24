import math
import re

entry = "1+2+3-4*3"

# check for operators 
# operate right and left values of operator base on operator 
# continue 

def stringToMath(entry):
    arr = re.split('[+,\-,*,/]', entry)#'; |, |\*|\n'
    print(entry)
    print(arr)
    for char in entry:
        if char == '+':
            res = float(arr[0]) + float(arr[1])
            arr[0] = res
            del arr[1]
            print(arr)            
        if char == '-':
            res = float(arr[0]) - float(arr[1])
            arr[0] = res
            del arr[1]
            print(arr)
        if char == '*':
            res = float(arr[0]) * float(arr[1])
            arr[0] = res
            del arr[1]
            print(arr)
        if char == '/':
            res = float(arr[0]) / float(arr[1])
            arr[0] = res
            del arr[1]
            print(arr)
    


    
        

stringToMath(entry)
