import random

# Load the list of valid words (e.g., from a text file)
def load_words():
    with open('words.txt') as f:
        words = f.read().splitlines()
    return words

# Check the guess and provide feedback
def check_guess(word, guess):
    feedback = ['_' for _ in word]
    used_indices = set()
    # Check for correct letters in the correct position
    for i in range(len(word)):
        if guess[i] == word[i]:
            feedback[i] = guess[i]
            used_indices.add(i)
    
    # Check for correct letters in the wrong position
    for i in range(len(word)):
        if i not in used_indices and guess[i] in word:
            if guess[i] in word and guess[i] not in feedback:
                feedback[word.index(guess[i])] = guess[i]
    
    return ''.join(feedback)

def wordle():
    words = load_words()
    word = random.choice(words).upper()
    attempts = 6
    print("Welcome to Wordle!")
    
    while attempts > 0:
        guess = input(f"You have {attempts} attempts left. Enter your guess: ").upper()
        
        if len(guess) != len(word):
            print(f"Please enter a {len(word)}-letter word.")
            continue
        
        if guess == word:
            print("Congratulations! You've guessed the word!")
            return
        
        feedback = check_guess(word, guess)
        print("Feedback:", feedback)
        
        attempts -= 1
    
    print(f"Game Over! The word was: {word}")

if __name__ == "__main__":
    wordle()
