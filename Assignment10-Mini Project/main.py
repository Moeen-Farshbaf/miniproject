

from film import Film
from series import Series
from documentary import Documentary
from pyfiglet import Figlet
f = Figlet(font='standard')
print (f.renderText('IMDB'))

fi = open('D:\Python online class\Assignment10-Mini Project\database.txt', 'r')
big_text = fi.read()
title_list = big_text.split('\n')
titleinfos = []
movies = []
series = []
documentaries = []
reported = {}

for i in range(len(title_list)):
    
    titleinf= title_list[i].split(',')
    mydict= {'name':titleinf[0], 'rate':titleinf[1], 'link':titleinf[2], 'director':titleinf[3], 'kind':titleinf[4], 'realc_or_duration_or_eps':titleinf[5]}
    titleinfos.append(mydict)
for i in range(len(titleinfos)):
    if titleinfos[i]['kind']== 'film':
        film = Film(titleinfos[i]['name'], titleinfos[i]['director'],titleinfos[i]['rate'],titleinfos[i]['link'],titleinfos[i]['kind'],titleinfos[i]['realc_or_duration_or_eps'])
        movies.append(film)
    if titleinfos[i]['kind']== 'documentary':
        doc = Documentary(titleinfos[i]['name'], titleinfos[i]['director'],titleinfos[i]['rate'],titleinfos[i]['link'],titleinfos[i]['kind'],titleinfos[i]['realc_or_duration_or_eps'])
        documentaries.append(doc)
    if titleinfos[i]['kind']== 'series':
        serie = Series(titleinfos[i]['name'], titleinfos[i]['director'],titleinfos[i]['rate'],titleinfos[i]['link'],titleinfos[i]['kind'],titleinfos[i]['realc_or_duration_or_eps'])
        series.append(serie)
def showmenu():
    options = ['Add title', 'Remove title', 'Report title', 'Edit title', 'Download trailer', 'Show list and info','Save and exit']
    opn = 1
    for option in options:
        print(opn, option)
        opn +=1
showmenu()

def addtitle():
    kinds = ['movie', 'series', 'documentary']
    
    kn = 1

    for kind in kinds:
        print(kn, kind)
        kn += 1
    knd = input('Select a kind from the list above')
    
    if knd == '1':
        name = input('Enter the movie name: ')
        director = input('Enter the movie director: ')
        rate = input('Enter the movie imdb score: ')
        link = input('Enter the movie trailer link: ')
        thkind = kinds[0]
        duration = int(input('Enter the duration(mins): '))
        movie = Film(name, director, rate, link, thkind, duration)
        movies.append(movie)
    if knd == '2':
        name = input('Enter the series name: ')
        director = input('Enter the series director: ')
        rate = input('Enter the series imdb score: ')
        link = input('Enter the series trailer link: ')
        thkind = kinds[1]
        episodes = int(input('Enter the number of episodes: '))
        serie = Series(name, director, rate, link, thkind, episodes)
        series.append(serie)
    if knd == '3':
        name = input('Enter the doc name: ')
        director = input('Enter the doc director: ')
        rate = input('Enter the doc score: ')
        link = input('Enter the doc trailer link: ')
        thkind = kinds[2]
        real = int(input('Are you sure its real?(real/fake): '))
        doc = Documentary(name, director, rate, link, thkind, real)
        documentaries.append(doc)
