# Write a Python code that classifies items in the list as Low, Medium, or High.
# Also, do a count of items based on this classification and finally give a sum of items in each classification
   #make a classification category
sales = [ 120, 450, 800, 50, 900, 300]
for sale in sales:
 if sale <= 300:
    print("Low")
 elif sale  <= 700:
   print("Medium")
 else:
   print("High")
