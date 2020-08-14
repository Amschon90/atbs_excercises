# Opening other programs
import subprocess

calcProcess = subprocess.Popen('C:\\Windows\\\System32\\calc.exe')

# Two methods: poll and wait
print (calcProcess.poll() == None) # True
print (calcProcess.wait()) # Instantly returns, but other apps do not
print (calcProcess.poll())

# Specify a program
openNp = subprocess.Popen([r'C:\Windows\notepad.exe',r'C:\Users\Zig0n\Documents\helloworld.txt'])

# Use Default program
hwtxt = open('hello.txt','w')
hwtxt.write('I wrote this.')
hwtxt.close()
subprocess.Popen(['start', 'hello.txt'], shell=True)