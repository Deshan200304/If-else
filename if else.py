"""
If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5 , print Not Weird
If n is even and in the inclusive range of 6 to 20 , print Weird
If n is even and greater than 20 , print Not Weird
"""

number = int(input("Enter a number: "))

if number%2 == 1:
    print("Wired")

elif number%2 == 0 and 2 <= number <= 5:
    print("Non wired")
elif number%2 == 0 and 6 <= number <= 20:
     print("Weird")

elif number%2 == 0 and number > 20:
     print("Not Weird")



"""
new question
Write a Python program that reads a person's age and prints their life stage based on the following rules:

Age Range	Output
0–12	Child
13–19	Teenager
20–35	Young Adult
36–59	Adult
60+	Senior Citizen
Negative age	Invalid input
"""

