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
    print('\tVolume: ' + str(volumeNumber))
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
        content = content.replace(str(chr(151)),'-') 
##        content = content.replace(str(chr(156)),'oe')
##        content = content.replace(str(chr(153)),'') # as far as I could see this character was empty?
##        content = content.replace(str(chr(157)),'') # same for this one
##        content = content.replace(str(chr(160)),'') # same for this one
        content = content.replace(str(chr(180)),"'") # ´
        content = content.replace(str(chr(183)),".") # ·
        content = content.replace(str(chr(226)),"'")
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
            if not ((c in 'ÂàäÉéèÏïîÔôâöòóêëÚüûç£§°½†') or (ord(c) == 134) or (ord(c) == 136)): # 134 is † 136 is ^ variant
                print(str(lineNumber+1) + ':' + str(colNumber) + ' - ' + c + ': ' + str(ord(c)))
                print(lines[lineNumber] + '\n')

def writeNewSource(authCode, volumeNumber, content):
    directory = 'new/%s' % (authCode)
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(directory + '/%s%d.txt' % (authCode, volumeNumber), 'w', encoding='ISO-8859-1') as f:
        f.write(content)

def procressAllAuthors(authors):
    for author in authors:
        processSingleAuthor(author)
           
def processSingleAuthor(author):
    print('Processing: ' + author.code)
    for i in range(1,author.numBooks + 1):
       findCharacters(author.code, i)
    

class Author:
    def __init__(self, code, numBooks):
        self.code = code
        self.numBooks = numBooks

authors = [Author("ajg", 11),
           Author("cac", 37),
           Author('chm', 18),
           Author('fer', 21),
           Author('grc', 88),
           Author('jbs', 17),
           Author('jnd', 52),
           Author('jt', 103),
           Author('misc', 27),
           Author('smc', 10),
           Author('wjh', 23)]
           
processSingleAuthor(authors[8])
