
# #You are going to get input from a student. And then tell them their class of grade. Ensure that you are able to filter out wrong input

# 3.5- 4.00 – First Class Honours
# 3.0-3.49 – Second Class Honours (Upper Division)
# 2.0-2.99 – Second Class Honours (Lower Division)
# 1.0-1.99 – Third Class Honours

grade = float (input ("Enter your grade"))
if grade >= 3.5:
    print("First Class Honours")
#if grade >= 3 or :
   # print("Invalid entry")
elif grade >= 3.49:
    print("Second Class Honours (Upper Division)")
elif grade >= 2.99:
    print("Second Class Honours (Lower Division)")
else:
    print("Third class honours")
    # filter out wrong output
else:
print("Invalid grade")

#corrected version with boundaries
grade = float (input ("Enter your grade"))

if grade >=  3.5 and grade  <= 4.00:
    print("First Class Honours")
elif grade >= 3.00 and grade <= 3.49:
    print("Second Class Honours (Upper Division)")
elif grade >= 2.00 and grade  <= 2.99:
    print("Second Class Honours (Lower Division)")
elif grade >= 1.00 and grade  <= 1.99:
    print("Third class honours")
else:
   print("Invalid grade")