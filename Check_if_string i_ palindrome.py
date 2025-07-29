word = input("Enter a word for checking : ")
word1 = word[::-1]
if(word == word1):
    print(f"{word} is a palindrome word.")
else:
    print(f"{word} is not a palindrome word.")
