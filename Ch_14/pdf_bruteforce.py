import PyPDF2, os

os.chdir('C:\\Users\\Zig0n\\Documents\\VSCode Projects\\atbs_excercises\\Ch_14')

bfWords = []

# Open dictionary file
txtFile = open('dictionary.txt', 'r')

# Import each row into a list
for key in txtFile:
    bfWords.append(key.rstrip())

# Loop through the list
pdfCracker = PyPDF2.PdfFileReader(open('AmSchonResume_encrypted.pdf', 'rb'))
for pw in bfWords:
    # Check if it returns ok
    if pdfCracker.decrypt(pw) == 1:
        print('Success! The password was %s!' % (pw))
        crackedPw = pw
        break
    else:
        print('The password was not %s...' % (pw))

# Save the decrypted file and password
pdfCracker.decrypt(crackedPw)
pdfWriter = PyPDF2.PdfFileWriter()
pdfOutput = open('AmSchonResume.pdf','wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()