#This function takes in an int parameter and finds the sum of all positive multiples of 3 and 5 less than said parameter
#The input for this function must be a non-negative integer
#This program uses python 3.8 standard library

def sumOf(x):
    #Ensure x is an integer
    if isinstance(x, int):
        #Ensure x is a non-negative integer
        if (x >= 0):
            sum1 = 0
            sum2 = 0
            i = 2
            y = 3
            #Calculte the sum of multiples of 3 less than x
            while y < x:
                sum1 = sum1 + y
                y = 3*i 
                i += 1
            j = 2
            z = 5
            #Calculte the sum of multiples of 5 less than x
            while z < x:
                sum2 = sum2 + z 
                z = 5*j
                j += 1
            #Add sums of multiples of 3 and 5 together for final sum
            sumFinal = sum1 + sum2
            return sumFinal
        else:
            print("Invalid entry. Please enter a positive integer value.")
    else: 
        print("Invalid entry. Please enter a positive integer value.")
        


