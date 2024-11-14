import argparse
import sys
import random
from termcolor import colored
from logger import logger

sys.stdout.reconfigure(encoding='utf-8')

# List of Discordian-themed palindromes
palindromes = [
    "Doc, note, I dissent: a fast never prevents a fatness. I diet on cod.",
    "Ma is as selfless as I am.",
    "No, it is open on one position.",
    "Evil is a name of a foeman, as I live.",
    "Able was I ere I saw Elba, Ma, I met a man, I came.",
    "Dennis and Edna sinned.",
    "Are we not drawn onward, we few, drawn onward to new era?",
    "Satan, oscillate my metallic sonatas!",
    "Go hang a salami, I'm a lasagna hog.",
    "Step on no pets, no step on—pets on no steps."
]

# List of Discordian-themed non-palindromes
non_palindromes = [
    "Chaos is the order of the day, but only if you blink.",
    "The universe loves you, but not today.",
    "In a world of disorder, the only constant is Eris.",
    "If everything is random, is anything really random?",
    "Confusion is the spice of life, just don't let it burn.",
    "Five tons of flax make the perfect sandwich.",
    "Why be normal when the extraordinary is more fun?",
    "Eris laughed, and the apple fell, and the world was never the same.",
    "Discord isn't chaos, it's just a misunderstood harmony.",
    "What is the sound of one hand clapping? Eris knows."
]

# Function to generate a random palindrome
def generate_random_palindrome():
    """
        Generates a random palindrome from the list of Discordian-themed palindromes and non-palindromes.
        Arguments:
        None
        Returns:
        A random palindrome
    """
    #Combine the list of palindromes and non-palindromes
    all_sentences = palindromes + non_palindromes
    return random.choice(all_sentences)

# Function to check if a sentence is a palindrome
def is_palindrome(sentence):
    """ 
        Checks if the sentence is a palindrome
        after cleaning it from non-alphanumeric characters
        and converting it to lowercase.
        Arguments:
        sentence
        Returns:
        True if the sentence is a palindrome, False otherwise
    """
    clean_sentence = ''.join(char.lower() for char in sentence if char.isalnum())

    return clean_sentence == clean_sentence[::-1]

# Main function to accept a sentence as an argument and check if it is a palindrome
def main():
    """
        Accepts a sentence as an argument and checks if it is a palindrome
        or uses a random palindrome if no argument is provided.
        Arguments:
        None
        Returns:
        None
    """
    parser = argparse.ArgumentParser(description="Accept a full sentence as one argument")
    parser.add_argument('sentence', nargs='*', help="The sentence to be accepted as one argument")
    args = parser.parse_args()
    logger.info("User input: %s", args)

    is_single_word = False
    if not args.sentence:
        sentence = generate_random_palindrome()
        logger.info("Generated sentence: %s", sentence)
    else:
        sentence = ' '.join(args.sentence)
        if len(args.sentence) == 1:
            is_single_word = True

    print(colored(f"{sentence}", "blue"))

    input_type = 'word' if is_single_word else 'sentence'
    result_type = 'is a palindrome' if is_palindrome(sentence) else 'is not a palindrome'
    color = 'green' if is_palindrome(sentence) else 'red'

    print(colored(f"The {input_type} {result_type}.", color))
    logger.info("The %s %s.", input_type, result_type)
    
if __name__ == "__main__":
    main()
