movies = ["Das boot(1981)act", "Blade Runner(1982)sf", "Arrival(2016)sf",
          "Dumb & Dumber(1994)com", "Blade Runner 2049(2015)sf",
          "Three Kings(1999)act", "The green hornet(2011)com"
          ]
genres = {'act': 'Acción', 'sf': 'Ciencia Ficción', 'com': 'Comedia'}


def nameInputGenere(array, listMovies, genere):
    for value in listMovies.items():
        if value[0] == genere:
            films = ['Peliculas de '+value[1]]
    for iterator in array:
        if iterator[-3:] == genere or iterator[-2:] == genere:
            films.append('-'+str(iterator.split('(')[0]))
    for film in films:
        print(film)


def filmsYear(films, year):
    filmseErlear = 0
    for film in films:
        if year > int(film[film.find('(')+1:film.find(')')]):
            filmseErlear += 1
    print('Cantidad de estrenadas antes del año ' +
          str(year)+': '+str(filmseErlear))


def firstLetter(array, letter):
    films = []
    elmts = []
    for i in array:
        if letter == i[0]:
            films.append(i)
    for film in films:
        filmName = film[:film.find('(')]
        year = film[film.find('(')+1:film.find(')')]
        if film[-3:] == 'act' or film[-3:] == 'com':
            gen = genres[film[-3:]]
        elif film[-2:] == 'sf':
            gen = genres[film[-2:]]
        elmts.append([filmName, year, gen])
    print('Películas cuyo nombre empieza con la letra "', letter, '"')
    for element in elmts:
        print(element[0], '.', ' Año:', element
              [1], '.', 'Género: ', element[2])


def menu():
    op = ''
    while op != '4':
        if op == '':
            print('Hi, welcome to practice number 6!')
        print('What exercise do you want to see?')
        print('1) Exercise 1:')
        print('2) Exercise 2:')
        print('3) Exercise 3:')
        print('4) Exit')
        op = input()
        print('=====================')
        if op == '1':
            print('EXERCISE 1')
            nameInputGenere(movies, genres, input(
                'Input a genere: (act/sf/com) '))
            print('=====================')
        elif op == '2':
            print('EXERCISE 2')
            filmsYear(movies, int(input('Input a year please: ')))
        elif op == '3':
            print('EXERCISE 3')
            firstLetter(movies, input('Insert a letter: (D/B/A/T) '))
            print('=====================')


menu()
