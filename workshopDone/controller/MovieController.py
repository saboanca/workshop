'''
Created on 22 mar. 2017

@author: ABoanca
'''
from domain.Movie import Movie
from repository.CastRepo import CastRepository

class MovieController:
    def __init__(self, repo, repoCast):
        """
        initialize controller
        """
        self.__repo = repo
        self.__repoCast = repoCast
    
    def getAll(self):
        """
        Gets all items in the repository
        """
        return self.__repo.getAll()
    
    def add(self, movie):
        """
        Adds movie
        movie - movie to be added
        """
        self.__repo.add(movie)
    
    def removeID(self, id):
        '''
        removes movie by id
        id - movie id
        '''
        self.__repo.removeID(id)
            
    def checkID(self, id):
        '''
        ckecks if id exists
        id - the given id
        return  0 if id exists, 1 otherwise
        '''
        for actor in self.__repo.getAll():
            if actor.getID() == id:
                return 0
        return 1
    
    def addMovie(self, id, name, year, website):
        '''
        checks if movie is valid and creates it if so
        parameters: movie characteristics: id, name, year, website
        if error: prints message
        '''
        if id != -1 and self.checkID(id) == 1:
            movie = Movie(id, name, year, website)
            self.add(movie)
            self.__repoCast.addMovie(id)
            return 1
        return -1      
    

class ControllerException(Exception):
    """
    Exception class for controller errors
    """
    def __init__(self, message):
        """
        Constructor for controller exception class
        message - A string representing the exception message
        """
        self.__message = message

    def __str__(self):
        return self.__message