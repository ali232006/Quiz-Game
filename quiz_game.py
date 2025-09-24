import random

# greetings
print("Welcome to the Quiz Game!")

# asking player
Playing = input("Do you want to play the game? (yes/no) :- ").lower().strip()

if Playing != "yes":
    quit()

print("Okay! Let's play the Game :-)\n")

score = 0

# ------------------ Question Blocks ------------------
def q1():
    global score
    answer = input("Question1: What is the capital of India? Options\n A)Mumbai\n B)Delhi\n C)Chennai\n D)Kolkata? ").lower().strip()
    if answer == "b":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

def q2():
    global score
    answer = input("Question2: Which is the largest planet in our solar system? Options\n A)Earth\n B)Mars\n C)Neptune\n D)Jupiter? ").lower().strip()
    if answer == "d":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

def q3():
    global score
    answer = input("Question3: Which President is called the People's President? Options\n A)Dr Rajendra Prasad\n B)Dr APJ Abdul Kalam\n C)Dr Zakir Husain\n D)V.V. Giri? ").lower().strip()
    if answer == "b":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

def q4():
    global score
    answer = input("Question4: In which year did India win their first ODI World Cup? Options\n A)1983\n B)2004\n C)1999\n D)2011? ").lower().strip()
    if answer == "a":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

def q5():
    global score
    answer = input("Question5: Who was the First President of America? Options\n A)Obama\n B)Andrew Jackson\n C)Trump\n D)George Washington? ").lower().strip()
    if answer == "d":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

def q6():
    global score
    answer = input("Question6: Red Sea is located in which region? Options\n A)Indian Ocean\n B)Pacific Ocean\n C)Middle East\n D)Europe? ").lower().strip()
    if answer == "c":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

def q7():
    global score
    answer = input("Question7: Who is the most famous F1 driver? Options\n A)Lewis Hamilton\n B)Max Verstappen\n C)Sebastian Vettel\n D)Charles Leclerc? ").lower().strip()
    if answer == "a":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

def q8():
    global score
    answer = input("Question8: In which year was the Indian Constitution formed? Options\n A)1947\n B)1950\n C)1952\n D)1949? ").lower().strip()
    if answer == "d":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

def q9():
    global score
    answer = input("Question9: Who is the supreme commander of all Indian armed forces? Options\n A)PM\n B)President\n C)Vice President\n D)Deputy PM? ").lower().strip()
    if answer == "b":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

def q10():
    global score
    answer = input("Question10: How many World Cups did Australia win? Options\n A)7\n B)8\n C)6\n D)4? ").lower().strip()
    if answer == "c":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

def q11():
    global score
    answer = input("Question11: Who is the national animal of India? Options\n A)Lion\n B)Tiger\n C)Peacock\n D)Elephant ").lower().strip()
    if answer == "b":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

def q12():
    global score
    answer = input("Question12: Which is the fastest land animal? Options\n A)Lion\n B)Cheetah\n C)Horse\n D)Leopard ").lower().strip()
    if answer == "b":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

def q13():
    global score
    answer = input("Question13: Which is the smallest ocean in the world? Options\n A)Indian Ocean\n B)Atlantic Ocean\n C)Arctic Ocean\n D)Pacific Ocean ").lower().strip()
    if answer == "c":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

def q14():
    global score
    answer = input("Question14: Who is known as the Father of Computers? Options\n A)Alan Turing\n B)Charles Babbage\n C)Bill Gates\n D)Steve Jobs ").lower().strip()
    if answer == "b":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

def q15():
    global score
    answer = input("Question15: Which country invented tea? Options\n A)India\n B)Japan\n C)China\n D)England ").lower().strip()
    if answer == "c":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

# ------------------ Run only 5 random questions ------------------
all_questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15]
selected = random.sample(all_questions, 5)

for func in selected:
    func()

# Final result
print("\nQuiz completed! Your final score is:", score, "out of", len(selected))