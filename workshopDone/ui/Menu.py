'''
Created on 22 mar. 2017

@author: ABoanca
'''
from domain.Actor import Actor
from domain.Actor import ActorValidator
from domain.Movie import Movie
from domain.Movie import MovieValidator
#from domain.Movie import Movie


class UI:
    def __init__(self, actors, movies, cast):
        '''
        Constructor class for ui
        parameters: actor repo, movie repo, cast repo
        '''
        self._actors = actors
        self._movies = movies
        self._cast = cast
        
    @staticmethod
    def printMenu():
        string = '\nAvailable commands:\n'
        string += '\t 1 - Add actor\n'
        string += '\t 2 - Add movie\n'
        string += '\t 3 - Remove actor\n'
        string += '\t 4 - Remove movie\n'
        string += '\t 5 - Display actors\n'
        string += '\t 6 - Display movies\n'
        string += '\t 7 - Add actor to a movie cast\n'
        string += '\t 8 - Remove actor from movie cast\n'
        string += '\t 9 - Display cast\n'
        string += '\t 0 - Exit\n'
        print(string)
        
    def mainMenu(self):
        keepAlive = True
        while keepAlive:
            try:
                UI.printMenu()
                command = input("command:")
                if command == "0":
                    print("You exited the application\n")
                    break
                elif command == "1":
                    (id, firstName, lastName, birthday, nationality, residence, height, weigth, email, phone) = self.readActor()
                    self._actors.addActor(id, firstName, lastName, birthday, nationality, residence, height, weigth, email, phone)
                elif command == "2":
                    (id, name, year, website) = self.readMovie()
                    self._movies.addMovie(id, name, year, website)
                elif command == "3":
                    id = int(input("ID= "))
                    self._actors.removeID(id)
                    self._cast.removeActor(id)
                elif command == "4":
                    id = int(input("ID= "))
                    self._movies.removeID(id)
                    self._cast.removeMovie(id)
                elif command == "5":
                    self.printList(self._actors.getAll())
                elif command == "6":
                    self.printList(self._movies.getAll())
                elif command == "7":
                    idMovie = int(input("ID Movie= "))
                    idActor = int(input("ID Actor= "))
                    self._cast.checkAddToCast(idMovie, idActor)
                elif command == "8":
                    idMovie = int(input("ID Movie= "))
                    idActor = int(input("ID Actor= "))
                    self._cast.removeActorFromMovie(idMovie, idActor)
                elif command == "9":
                    self.printCast(self._cast.getAll(), self._movies.getAll(), self._actors.getAll())
                else:
                    print("Invalid command! Try again!\n")
            except Exception as exc:
                print("Error encountered - " + str(exc))
    
    @staticmethod
    def printCast(list, listMovies, listActors):
        if len(list) == 0:
            print("Empty list!")
        else:
            index = 0
            for entity in list:
                if index % 2 == 0:
                    for movie in listMovies:
                        if movie.getID() == entity:
                            print("\n" + movie.getName() + ":")
                else:
                    for id in list[index]:
                        for actor in listActors:
                            if actor.getID() == id:
                                print(actor.getFirstName() + " " + actor.getLastName())
                index = index + 1
    
    @staticmethod
    def printList(list):
        if len(list) == 0:
            print("Empty list!")
        else:
            for entity in list:
                print(entity)
        
    @staticmethod
    def readActor():
        try:
            id = int(input("ID= "))
        except ValueError as ve:
            print("Error encountered - " + str(ve))
            return (-1,"a","a","a","a","a","a",1,"a","a")
        firstName = input("First Name= ")
        lastName = input("Last Name= ")
        birthday = input("Enter birthday, format DD/MM/YYYY\nBirthday= ")
        nationality = input("Nationality= ")
        residence = input("Residence= ")
        height = input("Enter height, format M.CM\nHeight= ")
        try:
            weigth = int(input("Enter weigth, in kg\nWeigth= "))
        except ValueError as ve:
            print("Error encountered - " + str(ve))
            return (-1,"a","a","a","a","a","a",1,"a","a")
        email = input("Email= ")
        phone = input("Phone= ")
        actor = Actor(id, firstName, lastName, birthday, nationality, residence, height, weigth, email, phone)
        ok = ActorValidator()
        if ok.validate(actor) == True:
            return (id, firstName, lastName, birthday, nationality, residence, height, weigth, email, phone)
        print("Error encountered")
        return (-1,"a","a","a","a","a","a",1,"a","a")
    
    @staticmethod
    def readMovie():
        try:
            id = int(input("ID= "))
        except ValueError as ve:
            print("Error encountered - " + str(ve))
            return (-1,"a",1,"a")
        name = input("Name= ")
        try:
            year = int(input("Enter year\nYear= "))
        except ValueError as ve:
            print("Error encountered - " + str(ve))
            return (-1,"a",1,"a")
        website = input("Website= ")
        ok = MovieValidator()
        movie = Movie(id, name, year, website)
        if ok.validate(movie) == True:
            return (id, name, year, website)
        print("Error encountered")
        return (-1,"a",1,"a")      
    