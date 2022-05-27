i=1
while i<=10:
    print("Enter your marks-:")
    marks=int(input())
    if marks<25:
        print("your Grade is F")
    if 25<=marks<45:
        print("your Grade is E")
    if 45<=marks<50:
        print("your Grade is D")
    if 50<=marks<60:
        print("your Grade is C")
    if 60<=marks<80:
        print("your Grade is B")
    if marks>=80:
        print("your Grade is A")
    i =i+1
print(" you can enter your marks only 10 times ")
print(" ")

#QUESTION NO.2

x1=int(input("Enter the digits of any year of your choice -:"))
if (x1)%100==0and(x1)%400!=0:
    print("No it is not a leap year")
elif var1%4==0:
    print("yes it is a leap year")
else :
    print("No it is not a leap year")
print(" ")
#QUESTION No.3

from random import randint

print("This is a multiplication game program for kids")
i=1
while i<=10:
    x = randint(0, 15)
    y = randint(0, 15)
    print("question no.",str(i),", ",str(x),"X",str(y),"is")
    z= int(input("Enter your answer:-"))
    if z==x*y:
        print("Right!,Answer")
    else:
        print("your answer is wrong!,learn tables properly")
    i=i+1
print("There were only 10 questions ,thank you for attempting")
print(" ")

# QUESTION No.4

for i in range(200):
    if i % 5 == 2:
        if i % 6 == 3:
            if i % 7 == 2:
                print("There are " + str(i) + " candies in total")
