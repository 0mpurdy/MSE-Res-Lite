import sys
import codecs
import os

#¶Ö are shown instead of broken bar and another character on mac

# ˆ - 136
# • - 149
# œ - 156
# ° - 179
# ½ - 189

def findCharacters(authCode, volumeNumber):
    print('Volume: ' + str(volumeNumber))
    with open('source/%s/%s%d.txt' % (authCode, authCode, volumeNumber), 'r+', encoding='ISO-8859-1') as f:
        content = f.read()
        content = content.replace('¬',"'")
        content = content.replace('¦','^')
        content = content.replace(str(chr(145)),"'")
        content = content.replace(str(chr(146)),"'")
        content = content.replace(str(chr(147)),'"')
        content = content.replace(str(chr(148)),'"')
        content = content.replace(str(chr(149)),'.')
        content = content.replace(str(chr(133)),'...') 
        content = content.replace(str(chr(150)),'-') 
        content = content.replace(str(chr(180)),"'") # ´
        lines = content.split('\n')
        printNonAsciiChars(content, lines)
        writeNewSource(authCode, volumeNumber, content)
        
def printNonAsciiChars(s, lines):
    lineNumber = 0
    colNumber = 0
    for c in s:
        colNumber += 1
        if c == '\n':
            lineNumber += 1
            colNumber = 0
        if ord(c) > 128:
            if not (c in 'àäÉéèÏïÔôâöòóêëÚüûç£§î'):
                print(str(lineNumber) + ':' + str(colNumber) + ' - ' + c + ': ' + str(ord(c)))
                print(lines[lineNumber] + '\n')

def writeNewSource(authCode, volumeNumber, content):
    directory = 'new/%s' % (authCode)
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(directory + '/%s%d.txt' % (authCode, volumeNumber), 'w', encoding='ISO-8859-1') as f:
        f.write(content)
                
for i in range(1,24):
    findCharacters('smc', i)
