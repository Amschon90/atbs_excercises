import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
fakeres = requests.get('https://inventwithpython.com/page_that_does_not_exist')

menuOption = int(input('Which of the following would you like to do?\n1) Inspect the text\n2) Download the text\n'))

if menuOption == 1:
    print(type(res))
    print(res.status_code == 200)
    print(len(res.text))
    print(res.text[0:10])
    print("\n")

    try:
        fakeres.raise_for_status()
    except Exception as exc:
        print('Oh no! It broke...\n%s' % (exc))

if menuOption == 2:
    res.raise_for_status()
    playFile = open('RomeoAndJuliet.txt', 'wb')
    for chunk in res.iter_content(100000):
        playFile.write(chunk)