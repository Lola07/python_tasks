# Write a Python program that iterates through integers from 1 to 100. For each multiple of three, 
# print "Fizz" instead of the number; 
# for each multiple of five, print "Buzz". 
# For numbers that are multiples of both three and five, print "FizzBuzz".

for numbers in range (1,100):

    if numbers % 3 == 0 and numbers % 5 == 0:
        print("FizzBuzz")
    elif numbers % 3 == 0:
        print("fizz")
    elif numbers % 5 == 0:
        print("Buzz")
    else:
        print(numbers)