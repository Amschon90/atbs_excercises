import subprocess, time

timeLeft = 60

print('Starting countdown. Press CTRL+C to end early.')
try:
    while timeLeft > 0:
        print(timeLeft)
        timeLeft -= 1
        time.sleep(1)

except KeyboardInterrupt:
    print('Done.')

subprocess.Popen(['start', 'alarm.wav'], shell=True)