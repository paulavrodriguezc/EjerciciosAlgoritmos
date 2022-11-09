def validate_str():
    word=input("Please enter the word you wish to have backwards: ")
    while not word.isalpha or len(word)<1:
        word=input("Invalid input. Please enter the word you wish to have backwards: ")
    return word
def backwards(word: str, index): 
    if index==0:
        return word[index]
    else:
        return word[index]+backwards(word, index-1)
def main():
    word=validate_str()
    print(f"The new word is {backwards(word, (len(word)-1))}.")
main()