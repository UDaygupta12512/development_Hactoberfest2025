num = int(input("Enter a number: "))
original = num
sum = 0
n = len(str(num))
 
while num > 0:
    digit = num % 10
    sum += digit ** n
    num //= 10
 
if sum == original:
    print(f"{original} is an Armstrong Number.")
else:
    print(f"{original} is not an Armstrong Number.")
