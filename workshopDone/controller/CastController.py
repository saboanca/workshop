'''
Created on 24 mar. 2017

@author: ABoanca
'''
from repository.ActorRepo import *

class CastController:
    def __init__(self, repo, repoActor):
        '''
        Constructor for cast
        '''
        self.__repo = repo
        self.__repoActor = repoActor
        
    def getAll(self):
        '''
        Gets all items in the repository
        '''
        return self.__repo.getAll()
    
    def lengthList(self, idMovie):
        '''
        Returns the length of a given movie cast list
        parameters: idMovie - movie id
        '''
        return self.__repo.lengthList(idMovie)
    
    def addMovie(self, idMovie):
        '''
        Adds a movie id 
        parameters: idMovie - movie id
        '''
        self.__repo.addMovie(idMovie)
    
    def removeMovie(self, idMovie):
        '''
        Removes a movie by id 
        parameters: idMovie - movie id
        '''
        self.__repo.removeMovie(idMovie)
    
    def addActor(self, idMovie, idActor):
        '''
        adds an actor to movie cast
        parameters: idMovie - movie id, idActor - actor id
        '''
        self.__repo.addActor(idMovie, idActor)
        
    def removeActor(self, idActor):
        '''
        parameters: idActor - actor id
        removes actor by id
        '''
        self.__repo.removeActor(idActor)
        
    def checkID(self, idMovie, idActor):
        '''
        Performn the repository check if idActor already exists in id movie
        parameters: idMovie - movie id, idActor - actor id
        '''
        return self.__repo.checkID(idMovie, idActor)
    
    def checkAddActor(self, idMovie, idActor):
        '''
        checks if actor id is a valid id (there actually is an actor with that id)
        if yes, it adds it, otherwise, no
        parameters: idMovie - movie id, idActor - actor id
        '''
        for actor in self.__repoActor.getAll():
            if actor.getID() == idActor:
                self.addActor(idMovie, idActor)
        return -1
    
    def checkAddToCast(self, idMovie, idActor):
        '''
        Checks if id actor already exists in movie list
        if it does not, it adds it
        parameters: idMovie - movie id, idActor - actor id
        '''
        index = 0
        castList = self.__repo.getAll()
        for index in range(0, len(castList)):
            if index % 2 == 0 and castList[index] == idMovie:
                index = index + 1
                for id in castList[index]:
                    if id == idActor:
                        return -1
        self.checkAddActor(idMovie, idActor) 
        
    def removeActorFromMovie(self, idMovie, idActor):
        '''
        removes actor from movie
        parameters: idMovie - movie id, idActor - actor id
        '''
        self.__repo.removeActorFromMovie(idMovie, idActor)