#membership operator in, not in
a = "hello"
b = "hello world"

if (a in b):
    print(f"{a} is a member of {b}")
if (a not in b):
    print(f"{a} is not a member of {b}")
 
#identity operator, checking if they are the same or not   
p = 40
q = 40

if (p is q):
    print("true, they are the same")
else :
    print("false, they are not the same")
    
a = 3
b = 5
#print bitwise right shift operator
print("a >> 1= ", a >> 1)
print("b << 1= ", b << 1)

#bitwise and/or - &, |
print(a & b)
print(a|b)

#grading system
print("Enter marks of five subjects: ")
markone = int(input())
marktwo = int(input())
markthree = int(input())
markfour = int(input())
markfive = int(input())
marksix = int(input())

total = markone + marktwo + markthree + markfour + markfive + marksix
print("Your total marks are", total)

avg = total/6
print("Your average is", avg)

if avg>=91 and avg<=100:
    print("Your grade is an A1")
elif avg>=81 and avg<=91:
    print("Your grade is an A2")
elif avg>=71 and avg<=81:
    print("Your grade is an B1")
elif avg>=61 and avg<=71:
    print("Your grade is an B2")
elif avg>=51 and avg<=61:
    print("Your grade is an C1")
elif avg>=41 and avg<=51:
    print("Your grade is an C2")
elif avg>=31 and avg<=41:
    print("Your grade is an D1")
elif avg>=21 and avg<=31:
    print("Your grade is an D2")
elif avg>=11 and avg<=21:
    print("Your grade is an E1")
else :
    print("Invalid")