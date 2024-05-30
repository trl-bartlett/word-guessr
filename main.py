import random

# subjects
musicalInstruments = ["guitar", "bass", "drums"]
moviesFrom1995 = ["casino", "seven", "mallrats"]
videoGameCharacters = ["mario", "samus", "kirby"]

# list of subjects
subjects = [musicalInstruments, moviesFrom1995, videoGameCharacters]

# get random subject
random_subject = random.choice(subjects)

# ADDITION: subject name variable
subject_name = ""

# ADDITION: change 'subject_name' variable instead of printing 3 different subject names
if random_subject == musicalInstruments:
    subject_name = "musical instruments"
elif random_subject == moviesFrom1995:
    subject_name = "movies from 1995"
elif random_subject == videoGameCharacters:
    subject_name = "video game characters"

ascii_title = """
                        _                                  
 __      _____  _ __ __| |   __ _ _   _  ___  ___ ___ _ __ 
 \ \ /\ / / _ \| '__/ _` |  / _` | | | |/ _ \/ __/ __| '__|
  \ V  V / (_) | | | (_| | | (_| | |_| |  __/\__ \__ \ |   
   \_/\_/ \___/|_|  \__,_|  \__, |\__,_|\___||___/___/_|   
                            |___/                          
"""

print(ascii_title)

# ADDITION: print subject once
print(f"subject: {subject_name}")

# get random answer
random_answer = random.choice(random_subject).lower()

display_answer = ["_" for _ in random_answer]

print(" ".join(display_answer))

# ADDITION: variables
game_end = False
attempts_left = 6
used_letters = set()

# while loop to keep user guessing until they get the word or take more than 6 turns
while not game_end and attempts_left > 0:

    # prompt user for a letter
    user_guess = input("guess a letter: ").lower()

    # check to see if user guess has been previously used
    if user_guess in used_letters:
        print(f"you already guessed {user_guess}. try another letter...")
        continue

    # add guess to used letters set
    used_letters.add(user_guess)

    # check if guessed letter is in random answer
    if user_guess in random_answer:
        for position in range(len(random_answer)):
            if random_answer[position] == user_guess:
                display_answer[position] = random_answer[position].upper()
    else:
        # if the letter isnt in the word, decrement attempts left and print info to reflec this
        attempts_left -= 1
        print(f"that letter isn't in the word. you have {attempts_left} attempts left...")

    # print current state of letters guessed
    print(" ".join(display_answer))

    # check if the word is completely guessed
    if "_" not in display_answer:
        game_end = True

# print win or lose message
if game_end:
    print("you got the word!")
else:
    print(f"game over! The word was '{random_answer.upper()}'.")





