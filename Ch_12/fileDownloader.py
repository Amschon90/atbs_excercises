# You can learn about the requests module’s other features from https://requests.readthedocs.org
import requests

# call requests to download the file
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# this is a fake file for testing when needed
fakeres = requests.get('https://inventwithpython.com/page_that_does_not_exist')

menuOption = int(input('Which of the following would you like to do?\n1) Inspect the text\n2) Download the text\n'))

if menuOption == 1:
    print(type(res))
    # this checks if it was successful
    print(res.status_code == 200)
    print(len(res.text))
    print(res.text[0:250])
    print("\n")
    try:     # put this try block in so it won't crash
        fakeres.raise_for_status()
    except Exception as exc:     # throws exception
        print('Oh no! It broke...\n%s' % (exc))

if menuOption == 2:
    res.raise_for_status()
    # creates file with 'wb' write binary mode
    playFile = open('RomeoAndJuliet.txt', 'wb')
    # takes 100k bytes at a time
    for chunk in res.iter_content(100000):
        playFile.write(chunk)
    playFile.close()