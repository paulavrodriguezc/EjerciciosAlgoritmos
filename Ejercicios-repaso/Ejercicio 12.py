word=input("Please enter a word: ")
safeword="out"
while word!=safeword:
    print(f"-------------------> {word}")
    word=input("Please enter a word: ")
print("Thanks for playing!")