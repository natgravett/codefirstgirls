#print is an in-built function - you can tell something is a function as it is followed immediately by ()
print('this is a function')

#highlight and right click RUN to run a line of code
#there are 2 number types in python (1) integer, whole numbers (2) float, decimal numbers
#you can code in the file or the terminal --> best to code numbers after >>> in the terminal

# 7+2 is addition
# 7-2 is subtraction
# 7*2 is multiplication
# 7/2 is division
# 5%2 is modulo where the first number is divided by the second number and then it returns what is left over
# ** is exponentiation --> **2 squares something e.g. 2**2 = 4

#string datatype is for text and characters, and the info needs to be in " or '
"blue" + "bell"
#this is a concatenation where the 2 words are combined with no space
"blue" * 3
#this will return blue 3x in a row with no spaces

"cat".upper()
#this will return CAT
"cat".lower()
#this will return cat

#you can run 2 strings or 2 integers, but not combine them
print("cat" + str(3))
#str(3) will convert the number to a string, so strings and integers can be combined --> cat3

#a variable is a reusable label for a data value --> to enable automation
#3 steps to create a variable (1) name it (2) = sign (3) value it references
print('pasta')
food = 'pasta'
print(food)
#using print(food) will return pasta

oranges = 12
cost_per_orange = 0.5
total_cost = oranges * cost_per_orange
print(str(oranges) + "oranges")
print("costs" + str(total_cost))

cat_no = 3
cat_cans = 2
total_cans = cat_no * cat_cans
print("cans " + str(total_cans))
#cans 6
weekly_cans = (cat_no * cat_cans)*7
print("cans" + str(weekly_cans))
#cans 42
output = str(cat_no) + " cats eat " + str(weekly_cans) + " cans "
print(output)
3 cats eat 42 cans
total_cans = cat_no * cat_cans * days
msg = str(cat_no) + " cats eat " + str(total_cans) + " cans in " + str(days) + " days "
print(msg)
3 cats eat 42 cans in 7 days

#formatting
my_string = "hi my name is {}".format("Natalie")
print(my_string)
my_string2 = "my name is {}".format("NAT")
print(mystring2)
