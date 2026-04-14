import random

words = ["python", "hangman", "computer", "keyboard", "monitor", "network", "security"]

secret_word = random.choice(words)
guessed_letters = []
attempts = 6

print("Welcome to Hangman!")
print(f"The word has {len(secret_word)} letters.")
print("You have 6 attempts before the man hangs!\n")

while attempts > 0:
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
            
    print(f"Word: {display}")
    print(f"Guessed letters: {guessed_letters}")
    print(f"Attempts remaining: {attempts}\n")
    
    if "_" not in display:
        print(f" You guessed it! The word was {secret_word}! less gooo!")
        break
        
    guess = input("Guess a letter: ").lower().strip()
    
    if len(guess) != 1:
        print("One letter at a time!\n")
        continue
        
    guessed_letters.append(guess)
    
    if guess in secret_word:
        print(f"Nice, {guess} is in the word!\n")
    else:
        attempts -= 1
        print(f"Wrong! {attempts} attempts remaining.\n")
        
if attempts == 0:
    print(f"Game over! The word was {secret_word}.  Too bad man lets try again queen!")
    