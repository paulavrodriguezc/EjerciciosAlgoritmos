number=input("Please enter an integer number: ")
digits=[]
for x in number:
    digits.append(x)
while len(digits)>1:
    sum=0
    for i in digits:
        i=int(i)
        sum+=(i**2) 
    number=str(sum)
    digits=[]
    for x in number:
        digits.append(x)
if int(digits[0])==1:
    print("The number is happy.")
else:
    print("The number is not happy.")