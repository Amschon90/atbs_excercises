from bs4 import BeautifulSoup
import re, requests, os.path

# Ask the user what they want to search for
search = input("What would you like me to download images for?\n")
mainpath = os.path.join(os.environ["USERPROFILE"], f"Pictures\\imgurstuff\\{search}")

# Create the folder for the images if it doesn't exist
if not os.path.exists(mainpath):
    os.makedirs(mainpath)

# Get the URL for each image from imgur
html = requests.get(f'https://imgur.com/search/score?q={search}')
bs = BeautifulSoup(html.text, 'html.parser')
imagegallery = bs.find_all('img', {'src':re.compile('.jpg')})

# Counter for file names
i = 1

for image in imagegallery: 
    r = requests.get('http:'+image['src'])
    if r.status_code == 200:
        # If the request was successful..
        dlfile = open(os.path.join(mainpath,f'pic{i}.jpg'), 'wb')
        # Takes 100k bytes at a time
        for chunk in r.iter_content(100000):
            dlfile.write(chunk)
        dlfile.close()
        print(f'{i} image successfully downloaded..')
        i += 1
print("\nAll images downloaded!")