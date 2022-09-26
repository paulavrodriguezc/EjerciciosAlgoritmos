word=input("Please enter a word: ")
while not word.isalpha():
    word=input("Invalid answer. Please enter a word: ")
word=word.lower()
vowels=["a","e","i","o","u"]
result=""
for w in word:
    if w in vowels:
        result=w.upper()
        word=word.replace(w,result)
print(word)