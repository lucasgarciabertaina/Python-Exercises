from json import loads, dumps
read = open('pelis.json', 'r')

# Forma 1

films = []
title = ''
actors = ''
rating = ''
boxOffice = ''
for i in range(1, 123):
    line = read.readline().split(': ')
    value = line[0][8:]
    if value == '"Title"':
        title = line[1][1:-3]
    elif value == '"Actors"':
        actors = line[1][1:-3]
    elif value[8:] == '"Source"' and line[1][1:-3] == 'Rotten Tomatoes':
        line = read.readline().split(': ')
        rating = line[1][1:-2]
    elif value == '"BoxOffice"':
        boxOffice = line[1][1:-3]
    elif title != '' and actors != '' and rating != '' and boxOffice != '':
        films.append([title, actors, rating, boxOffice])
        title = ''
        actors = ''
        rating = ''
        boxOffice = ''

table = open('pelis.csv', 'w')
table.write('Nombre; Actor; Raiting; Recaudación\n')
for i in range(3):
    table.writelines(films[i][0]+'; '+films[i][1] +
                     '; '+films[i][2]+'; '+films[i][3]+'\n')

"""
# Forma 2

jsonRead = read
data = loads(jsonRead.read())
films = []
for i in data:
    films.append([i['Title'], i['Actors'], i['Ratings']
                 [1]['Value'], i['BoxOffice']])
table = open('pelis.csv', 'w')
table.write('Nombre; Actor; Raiting; Recaudación\n')
for i in range(3):
    table.writelines(films[i][0]+'; '+films[i][1] +
                     '; '+films[i][2]+'; '+films[i][3]+'\n')
"""
