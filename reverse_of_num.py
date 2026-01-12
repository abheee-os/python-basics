num=int(input("Enter the number: "))
n=num
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10


print("Reversed number of", num, "is", rev)

  




    