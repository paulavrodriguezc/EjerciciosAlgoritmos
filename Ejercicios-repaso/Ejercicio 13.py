x=input("Please enter a word or number: ")
y=x[::1]
if x==y:
    print(f"{x} is a palindrome.")
else:
    print(f"{x} is NOT a palindrome.")