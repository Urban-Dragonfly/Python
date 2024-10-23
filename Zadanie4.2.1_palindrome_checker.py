import random
import sys
sys.stdout.reconfigure(encoding='utf-8')

# List of polish palindromes and simmilar words
palindromes = ["kajak", "potop", "anna", "zakaz", "oko", "radar", "mam", "sedes"]
simm_words = ["łódka", "powódź", "ewa", "zakazy", "około", "sonar", "tata", "toaleta"]
# Adding all palindromes and simmilar words to one list
all_words = palindromes + simm_words
# Mixing words
random.shuffle(all_words)

# Function to check if a single word is a palindrome
def is_palindrome(word):
    """ 
        Checks if the word is a palindrome
        Arguments:
        word
        Returns:
        True if the word is a palindrome, False otherwise
    """
    return word == word[::-1]

# Apply the function to each word and print the result
for word in all_words:
    result = is_palindrome(word)
    print(f"{word}: {result}, to słowo to palindrom" if result else f"{word}: {result}, to słowonie jest palindromem")

