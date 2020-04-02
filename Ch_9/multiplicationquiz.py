import pyinputplus as pyip
import random, time

numberOfQuestions = 10
correctAnswers = 0

for questionNumber in range(numberOfQuestions):
    a = random.randint(0,9)
    b = random.randint(0,9)
    prompt = '%s: %s x %s = ' %(questionNumber,a,b)
    try:
        response = pyip.inputStr(prompt, allowRegexes=['^%s$' % (a*b)],
                blockRegexes=[('.*','Incorrect!')],
                timeout=8, limit=3)
    except pyip.TimeoutException:
            print('Out of time!')
    except pyip.RetryLimitException:
            print('Out of tries!')
    else:
        print('Correct!')
        correctAnswers += 1
    time.sleep(1)
    
print('You got %s correct.' %(correctAnswers))