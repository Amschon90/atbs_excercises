#! python3
# stopwatch.py - A simple stopwatch program.

import time, pyperclip

def stopwatch():
    # Display instructions
    print('Press ENTER to begin. Afterward, press ENTER to click the stopwatch. Press CTRL+C to quit.')
    input()
    print('Started.')
    startTime = time.time()
    lastTime = startTime
    lapNum = 1
    output = ''

    try:
        while True:
            input()
            lapTime = round(time.time()-lastTime,2)
            totalTime = round(time.time()-startTime, 2)
            lapOutput = (f'Lap #{str(lapNum).rjust(2)}: {str(lapTime).ljust(5)} (Total: {str(totalTime).ljust(5)})')
            output += lapOutput + '\n'
            print(lapOutput, end='')
            lapNum += 1
            lastTime = time.time()
    except KeyboardInterrupt:
        pyperclip.copy(str(output))
        print('\nDone')

if __name__ == '__main__':
    stopwatch()