#enter 1 row num
#find odd & even
#total odd & even

num1 = int(input("Please enter first number: "))
num2 = int(input("Please enter second number: "))

oddNum = []
evenNum = []
tongOddNum = 0
tongEvenNum = 0

for i in range(num1,num2+1):
    if i%2==0:
        evenNum.append(i)
    else:
        oddNum.append(i)

for i in evenNum:
    tongEvenNum += i

for i in oddNum:
    tongOddNum += i

print("List even number: " , evenNum)
print("List odd number: " , oddNum)
print("Total even number is " + str(tongEvenNum))
print("Total odd number is " + str(tongOddNum))