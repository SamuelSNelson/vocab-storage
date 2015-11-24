import requests
from bs4 import BeautifulSoup
import wikipedia
r = requests.get('http://samuelsnelson.github.io/lhs-homework/')
soup = BeautifulSoup(r.content)
murk = 0
rat = 'class'
mouse = int(1)
f = open('rekt.html','w')
f.write("""<html>
<head>
    <link rel="stylesheet" type="text/css" href="doob.css">
</head>
<body>
""")
for murk in range(20):
    spans = soup.find_all('p', {rat : mouse})
    for p in spans:
            dog = p.text
            frog = wikipedia.page(dog)
            cat = frog.url
            mouse += 1
            b = requests.get(cat)
            crap = BeautifulSoup(b.content)
            booty = crap.p
            goop = wikipedia.summary(dog, sentences=1).encode('ascii', 'ignore').decode('ascii')
            kobe = wikipedia.summary(dog).encode('ascii', 'ignore').decode('ascii')
            krabs = booty.text 
            chicken = kobe.split(".")[2:3]#:1 is used to get defintion #2:3 is used to get sentence* [1:]*
            horse = ''.join(chicken)
            horse = horse.encode('ascii', 'ignore').decode('ascii')
            f.write("<div>")
            f.write('<h2>' + frog.title + '</h2>' + '<hr class = "title">')
            if len(str(goop)) <= 20:
                print goop
                homie = raw_input("Wikipedia screwed up. Write your own defintion here:") 
                f.write ('<b>' + 'Sentence:' +'</b>' + "%s" % homie + '\n')
            elif len(str(goop)) >= 100:
                tubby = goop.split(".")[:1]
                mustard = ''.join(tubby)
                f.write ('\t' + '<p>' + '&nbsp' + '<b>' + "Defintion: " +'</b>' + mustard + '<hr class ="line-splitter">' + '&nbsp') 
            else:
                f.write ('\t' + '<p>' + '&nbsp' + '<b>' + "Defintion: " +'</b>' + goop + '<hr class ="line-splitter">' + '&nbsp') 
            if len(str(chicken)) <= 11:
                print goop
                homie = raw_input("Wikipedia screwed up. Write your own sentence here:") 
                f.write ('<b>' + 'Sentence:' +'</b>' + "%s" % homie + '\n')
            else:
                f.write ('<b>' + 'Sentence:' +'</b>' + horse + "." '</p>' + '\n')
            f.write(""" 
                            </div>""")
f.write ('</body>' + '\n')
f.write ('</html>')
f.close()
