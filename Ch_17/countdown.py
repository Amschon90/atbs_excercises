import subprocess, time

timeLeft = 3

while timeLeft > 0:
    print(timeLeft, end='')
    timeLeft -= 1
    time.sleep(1)

subprocess.Popen(['start', 'alarm.wav'], shell=True)