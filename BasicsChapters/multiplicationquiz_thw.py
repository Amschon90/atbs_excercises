import random, time

numberOfQuestions = 10
correctAnswers = 0

for questionNumber in range(1,numberOfQuestions+1):
    a = random.randint(0,9)
    b = random.randint(0,9)
    start = time.time()
    attempts = 1
    while True:
        response = input('%s: %s x %s = ' % (questionNumber, a, b))
        now = time.time()
        if response.isdigit() == False:
            print("That's not a number.")
            attempts += 1
        elif attempts < 3 and now-start < 8:
            if int(response) == a*b:
                print("Correct.")
                correctAnswers += 1
                break
            else:
                print("Incorrect!")
                attempts += 1
        elif attempts == 3:
            print("Out of tries!")
            break
        else:
            print("Out of time!")
            break

    
print('You got %s correct.' %(correctAnswers))