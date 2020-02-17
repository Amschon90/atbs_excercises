import re
# import pyperclip which I cannot do at work :(

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                  # area code
    (\s|-|\.)?                          # separator
    (\d{3})                             # first 3
    (\s|-|\.)                           # separator
    (\d{4})                             # last 4
    (\s*(ext|x|ext.)\s*(\d{2,5}))?      #extension
)''', re.VERBOSE)

# TO DO, create email regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+                   # username
    @                                   # @ sign
    [a-zA-Z0-9.-]+                      # domain name
    (\.[a-zA-Z]{2,4})                   # dot something
)''', re.VERBOSE)

# TO DO, find matches

# TO DO, copy results
