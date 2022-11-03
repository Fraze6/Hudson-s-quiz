import time

score = 0

playing = input("do you want to start the quiz?").lower()

if playing != "yes":
    print("\nok bye")
    quit()
else:
    print("\nOkay, this is how it works")
    time.sleep(2)
    print("\nyou begin with a score of 0, if your score goes below that, you will lose.")
    time.sleep(3)
    print("\nget to the end of the quiz to win!")

    time.sleep(3.5)
    print("\nmake sure to answer these questions with either A, B or C ")

    time.sleep(2)

question_1_answer = input("\nWhat is my name?"
    "\n A) Hudson"
    "\n B) Alex"
    "\n C) Brennan"
    "\n Is the answer A,B or C?:").lower()


if question_1_answer != "a":
    score -= 1
    time.sleep(.2)
    print("your score is now",score)

else:
    score += 1
    time.sleep(.4)
    print("\nyour score is now", score)

if score <= 0:
    print("you lose")
    quit()

time.sleep(2)

question_2_answer = input("\nwhat is 1 + 1? this question is worth 2 points."
    "\n A) 3"
    "\n B) 42"
    "\n C) 2"
    "\n is the answer A , B or C?:").lower()
if question_2_answer != "c":
    score -= 2
    print("\nyour score is now", score)

else:
    score += 2
    time.sleep(.5)
    print("\nyour score is now", score)

if score <= 0:
    time.sleep(.3)
    print("you lose")
    quit()

time.sleep(1)

print("\nThat was just a warmup, now lets start the real test")
time.sleep(3)
print("but first I would like to introduce your abilities.")
time.sleep(3)
print("your first ability will be the 'skip' ability")
time.sleep(3)
print("if you get stuck at any question, you can say 'skip' and the question will be skipped")
time.sleep(4)
print("although, everything must come at a cost so, by doing this 2 points will be deducted from your score")
time.sleep(4)
print("now lets get back to the quiz.")
time.sleep(3)

print("\nwhat is 34,542 x 53,165?:")
time.sleep(.7)
print("A) 1,836,435,430")
time.sleep(.7)
print("B) 1,726,335,120")
time.sleep(.7)
print("C) 1,623,203,126")
time.sleep(.7)
question_3_answer = input("Is the answer A, B or C. Remember you can skip!:").lower()

if question_3_answer == "skip":
    score -= 2
    print("you have skipped this question")
    print(score)
elif question_3_answer == "a":
        score += 1000
        print("that's correct, you must be cheating!")
        time.sleep(1)
        print("anyways, theres no possible question that you cannot answer so I guess you win. Congrats!")
        print(score)
        time.sleep(4)
        quit()

else:
    print("how did you mess that up????")
    time.sleep(.8)
    print("you lose")
    time.sleep(4)
    quit()



print("that was the last question that I have and you skipped it???")
time.sleep(.5)
print("that is not fair. but theres nothing else that I can do other than let you win. congrats!")
time.sleep(4)
quit()









