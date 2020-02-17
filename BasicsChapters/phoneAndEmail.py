import re
# import pyperclip which I cannot do at work :(

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                  # area code
    (\s|-|\.)?                          # separator
    (\d{3})                             # first 3
    (\s|-|\.)                           # separator
    (\d{4})                             # last 4
    (\s*(ext|x|ext.)\s*(\d{2,5}))?      # extension
)''', re.VERBOSE)

# TO DO, create email regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+                   # username
    @                                   # @ sign
    [a-zA-Z0-9.-]+                      # domain name
    (\.[a-zA-Z]{2,4})                   # dot something
)''', re.VERBOSE)

text = "Hello, my name is Andy Schon! My number is 330-774-2211, or you can reach me at work at (602)-453-5030." \
       "Of course, if you're shy, email is fine too. I can be reached at Amschon90@gmail.com"

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':                 # checks to see if theres an extension on the phone number
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

print(matches)
