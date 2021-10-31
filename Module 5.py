#Problem 1 
#input loop 
#prints Hello 100 times 

for x in range(100):
    print("Hello")

#Problem 2
#input number list
#input line for numbers to be seperated
#prints each of the number on a new line
#input line to find the square 
#prints each number on new line and its square 


nums = (12, 10, 32, 3, 66, 17, 42, 99, 20)

for i in nums:
    print(i)

for i in nums:
    print("the square of",i,"is", i**2)

#Problem 3
#import turtle
#making turtle object
#input the number of sides
#input length of the side
#input the color of polygon
#input 'for' command
#input fill line
#print the shape and color of polygon

import turtle

s = turtle.Screen()
t = turtle.Turtle()
sides = int(input("Enter the number of sides: "))
length = int(input("Enter the length of the side: "))
col = input("Enter the color of your polygon: ")
t.fillcolor(col)
t.begin_fill()

for x in range(sides):
   t.forward(length)
   t.right(360/sides)
t.end_fill()
s.mainloop()

#Problem 4
#declaring variable p
#checking if p is divisible by 3 and 5
#when p is divisible by 3 and 5
#print Divisible by both
#checking if p is divisible by 3
#when p is divisible by 3
#print divisible by 3
#checking if p is divisible by 5
#when p is divisible by 5
#print Divisible by 5
#when number if not divisible by 3 or 5
#print number
#increment p

p=1
while p<=50:
    if p%3==0 and p%5==0:
        print("Divisible by both")
    elif p%3==0:
        print("Divisible by three")
    elif p%5==0:
        print("Divisible by both")
    else:
        print(p)
    p=p+1



