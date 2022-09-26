phrase=input("Please enter a sentence: ")
letter=input("Please enter a letter: ")
count=0
for i in phrase:
    if i==letter:
        count+=1
print(f"The letter {letter} appears {count} times in the sentence.")