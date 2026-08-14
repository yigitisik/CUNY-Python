import random


def guess():
    listOfWords = ["OhioState", "Vet", "School", "first", "SEMESTER", "OvEr"]
    livesLeft = 10
    chosenWord = random.choice(listOfWords).lower()
    listOfLettersFromChosenWord = list(chosenWord)
    displayOutput = ["_"] * len(chosenWord)
    guessedLetters = set()
    while livesLeft > 0:
        print("Word: " + " ".join(displayOutput))
        print(f"Lives left: {livesLeft}")

        letter = input("Guess a letter: ").lower()
        if not letter.isalpha() or len(letter) != 1:
            print("Invalid input! Please guess a single letter.")
            continue

        if letter in guessedLetters:
            print("You already guessed that :)")
            continue
        guessedLetters.add(letter)

        if letter in listOfLettersFromChosenWord:
            for index, char in enumerate(listOfLettersFromChosenWord):
                if char == letter:
                    displayOutput[index] = letter
            print(f"Good guess! {letter} is in the word :)")
        else:
            livesLeft -= 1
            print(f"Wrong guess! {letter} isn't in this word :(")

        if "_" not in displayOutput:
            print("Let's go!! Your guess was right: ", chosenWord)
            break
    else:
        print(f"Game over, the word was: {chosenWord}", ". Good luck next time :)")

while True:
    guess()
    replay = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if replay not in ("yes","y"):
        print("Thanks for playing! Goodbye!")
        break

