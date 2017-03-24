'''
Created on 22 mar. 2017

@author: ABoanca
'''
from domain.Actor import Actor

class ActorController:
    def __init__(self, repo):
        """
        initialize controller
        """
        self.__repo = repo
    
    def getAll(self):
        """
        Gets all items in the repository
        """
        return self.__repo.getAll()
    
    def add(self, actor):
        """
        adds an actor to the repository
        actor - actor to be added
        """
        #self.__undo = self.__repo.getAll()[:]
        self.__repo.add(actor)
    
    def removeID(self, id):
        '''
        removes actor by id
        id - actor's id
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
    
    def addActor(self, id, firstName, lastName, birthday, nationality, residence, height, weigth, email, phone):
        '''
        checks if actor is valid and creates it if so
        parameters: actor characteristics: id, firstName, lastName, birthday, nationality, residence, height, weigth, email, phone
        if error: prints message
        '''
        if id != -1 and self.checkID(id) == 1:
            actor = Actor(id, firstName, lastName, birthday, nationality, residence, height, weigth, email, phone)
            self.add(actor)
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