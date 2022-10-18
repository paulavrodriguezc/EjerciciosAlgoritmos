def main():
    code_introduced=input("Please enter a string (consisting of 'G', '()' or '(al)'): ")
    x=code_introduced.replace("G","G")
    y=x.replace("()","o")
    z=y.replace("(al)","al")
    print(f"Your new string is '{z}'.")
main()