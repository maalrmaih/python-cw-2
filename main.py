# write your code here
my_name = input("what is your name")
my_age = input("how old are you")
print(f"my name is {my_name} and i am {my_age}")

first_number = 388
second_number = 787
operation = input("enter operation")
if operation == "+":
    print(first_number + second_number)
elif operation == "-":
    print(first_number - second_number)    
elif operation == "*":
     print(first_number * second_number) 
elif operation == "/":
    print(first_number / second_number) 
else:
    print("the operation is not valid")  



number_1_12 = input("inter a number from 1 to 12")
noun = input("enter a noun")
name = input("enter a name")
sentence = input("enter a sentence ")
verb = input("enter a verb")

print(f"It was {number_1_12} o'clock when I heard a knock at the door.I opened the door and there was a box full of {noun} with a note saying From Mr. {name}.Just as I closed the door I heard a scream {sentence}.I froze in place and all I could do was {verb}.")
