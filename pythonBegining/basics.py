# in order to display something on the console, you would use the print() command
print("Hello World!");
print("This is me learning Python!!");


# to see the data types of various inputs, you would use the type() command
type("Hello World!");
type(574);
type(45.9);
type(True);

# a single comment is made with a # while multi-line is done with """ """
"""
The difference between integers and floating-point numbers is that integers are
whole numbers that do not have decimal places.
"""
float(137);
# >>> 137.0

int(596.89);
# >>> 596

int("42");
# >>> 42

float("42.97");
# >>> 42.97

int(float("45.83"));
# >>> 45

int("42.97");
# >>> Traceback (most recent call last):
# >>>   File "<stdin>", line 1, in <module>
# >>> ValueError: invalid literal for int() with base 10: '42.97'


# Instead of hard-coding variable values,
# Python also gives you the ability to collect a yet-to-be-defined input
# from the user at the time a program runs.

first_name = input("Enter your first name: ");
# this will be prompted to the user
# >>> Enter your first name: Tony

print("Hello,", first_name);
#the response from the user is set and used for the variable first_name.
# >>> Hello, Tony

dogs = int(input("Enter the number of dogs: "))

# >>> Enter the number of dogs: 30

cats = int(input("Enter the number of cats: "))

# >>> Enter the number of cats: 50

rabbits = int(input("Enter the number of rabbits: "))

# >>> Enter the number of rabbits: 0

shelter_length = int(input("Enter the shelter length: " ))

# >>> Enter the shelter length: 40

shelter_width = int(input("Enter the shelter width: " ))

# >>> Enter the shelter length: 20


# to concat multiple variables in Python, use the below format

prices = {"banana": 4,"apple": 2,"orange": 1.5,"pear": 3}

stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}

for item in prices:
  print "%s price: %s stock: %s" % (item, prices[item], stock[item])
