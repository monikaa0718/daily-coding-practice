#1 odd/even
n=int(input())
if (n%2==0):
  print("Even")
else:
  print("Odd")

#2 Find the greatest of 3 numbers
a,b,c=list(map(int,input().split()))
if(a>b and a>c):
  print(f"{a} is greater")
elif (b>a and b>c):
  print(f"{b} is greater")
else:
  print(f"{c} is greater")

#3.Find the second greatest number among three numbers
a,b,c=list(map(int,input().split()))
if (a>b and a<c) or (a<b and a>c):
  print(f"{a} is the second greatest")
elif (b>a and b<c) or (b<a and b>c):
  print(f"{b} is the second greatest")
else:
  print(f"{c} is the second greatest")

#4 fibonacci
n=int(input())    
a=0
b=1
while n>0:
  print(a,end=" ")
  a,b=b,a+b
  n-=1

#5 Factorial
n=int(input())
fact=1
for i in range(n,0,-1):
  fact*=i
print(fact)

#6 print values from 0 to  15

#method 1
n=int(input())
for i in range(n+1):
  print(i)

#method 2
n=int(input())
i=0
while i<=n:
  print(i)
  i+=1

#7 print value 100 to  150 skip 120, 125
for i in range(100,151):
  if i==120 or i==125:
    continue
  print(i)

#8 print value 50 to 60 include only odd numbers 
for i in range(50,61):
  if i%2!=0:
     print(i)

#9 print daily routine of your clg days => 10 days saturday &sunday => print Holiday
n=int(input())
for i in range(1,n+1):
  if i%7==6:
    print("Saturday Holiday")
  elif i%7==0:
    print("Sunday Holiday")
  else:
    print("Daily Routine")

#10 vowel/consonant
a=input()
vowel="aeiouAEIOU"
if a in vowel:
  print("Vowel")
elif a.isalpha():
  print("Consonant")
else:
  print("Invalid Input")

#11 sum of odd numbers and sum of even numbers
n=int(input())
even=0
odd=0
for i in range(1,n+1):
  if i%2==0:
    even+=i
  else:
    odd+=i
print("Sum of even numbers:",even)
print("Sum of odd numbers:",odd)

#12 leap year or not
n=int(input())
if n%400==0 or (n%4==0 and n%100!=0):
  print("Leap year")
else:
  print("Not a leap year")

#13 check whether 3 sides can be a triangle 
a,b,c=list(map(int,input().split()))
if (a+b>c and a+c>b and b+c>a):
  print("Can form a triangle")
else:
  print("Cannot form a triangle")

#14 count no of digits and letter
a=input()
digit=0
word=0
for i in a:
  if i.isalpha():
    word+=1
  elif i.isdigit():
    digit+=1
print("Word:",word)
print("Digit:",digit)

#15 sum of digits
n=int(input())
sum=0
for i in str(n):
  sum+=int(i)
print(sum)

#16 reverse a number without using built in functions
n=int(input())
rev=0
while n>0:
  d=n%10
  rev=rev*10+d
  n=n//10
print(rev)

#17 .number palindrome or not and word palindrome or not
n=int(input())
org=n
rev=0
while n>0:
  d=n%10
  rev=rev*10+d
  n=n//10
if org==rev:
  print("Palindrome")
else:
  print("Not a Palindrome")

a=input()
rev=""
for i in a:
  rev=i+rev
if a==rev:
  print("Palindrome")
else:
  print("Not a palindrome")

#18 print 1 to 10
1:1
2:4
3:9
n=int(input())
for i in range(1,n+1):
  if (i**2<=n):
    print(i,":",i**2)
