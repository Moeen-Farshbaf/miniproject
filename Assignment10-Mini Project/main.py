from media import Media
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

for i in range(len(title_list)):
    
    titleinf= title_list[i].split(',')
    mydict= {'name':titleinf[0], 'rate':titleinf[1], 'link':titleinf[2], 'director':titleinf[3], 'kind':titleinf[4], 'realc_or_duration_or_eps':titleinf[5]}
    titleinfos.append(mydict)
for i in range(len(titleinfos)):
    if titleinfos[i]['kind']== 'film':
        film = Film(titleinfos[i]['name'], titleinfos[i]['director'],titleinfos[i]['rate'],titleinfos[i]['link'],titleinfos[i]['kind'],titleinfos[i]['realc_or_duration_or_eps'])
        movies.append(film)

print(movies)