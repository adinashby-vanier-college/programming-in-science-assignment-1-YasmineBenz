# Function 1: Using Python built-in functions
# This function should take three numbers as input and return their max.
import math
def built_in_functions_max(num1, num2, num3):
    num1=int(num1)
    num2=int(num2)
    num3=int(num3)
    return(max(num1,num2,num3))

# Function 2: Using Python built-in functions
# This function should take three numbers as input and return their min.
def built_in_functions_min(num1, num2, num3):
    num1=int(num1)
    num2=int(num2)
    num3=int(num3)
    return min(num1,num2,num3)

# Function 3: Conditional Statements – The If Statement
# This function should check if a number is positive, negative, or zero and return the corresponding message.
def check_number(number):
    number= int(number)
    if number>0:
        return('Positive')
    elif number==0:
        return('Zero')
    else:
        return('Negative')
  

# Function 4: For Loop – Making a Star Shape
# This function should return a string representing a star shape.
def star_shape(rows):
    star='*'
    shape= ''
    for x in range(rows):
        shape+= star +'\n'
        star +='*'
    return shape.rstrip()
    


# Function 5: While Loop – Counting Multiples of 3
# This function should return a list of numbers from 1 to limit, replacing multiples of 3 with "Multiple of 3".
def count_multiples_of_3(limit):
    x=1
    list=''
    while x <=limit:
        if x%3==0:
            list+=("Multiple of 3\n")
        else:
           list+=str(x)+'\n'
        x+=1 
    return list.rstrip()


# Function 6: Sum of Even Numbers in a Range
# This function should calculate and return the sum of even numbers within a given range.
def sum_of_even_numbers(start, end):
    sum=0
    for i in range(start,end+1): 
        if i%2==0:
            sum+=i
    return(sum)
