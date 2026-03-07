# Given numbers = [12, 7, 9, 20, 33, 14, 5], print only even numbers and store them in a new list.
numbers = [12, 7, 9, 20, 33, 14, 5]
even_num = []

for num in numbers:
    if num %2 == 0:
        even_num.append(num)
    print(even_num)

    
    #test
    fruits = ["Apple","Orange", "Lemon"]
    fruits.insert(-2)