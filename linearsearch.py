numbers=[20,30,40,50,60]
target=int(input("Enter the number to be searched: "))
found=False

for i in range(len(numbers)):
    if numbers[i]==target:
        print("Found at index",i)
        found=True
        break

if not found:
    print("Not found")

  



        