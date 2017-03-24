'''
Created on 15 mar. 2017

@author: ABoanca
'''
from domain.Actor import Actor

class ActorRepository:
    def __init__(self):
        """
        Constructor for repository class
        """
        self._data = []
    
    def __len__(self):
        """
        Overriding the len() built-in function
        """
        return len(self._data)
    
    def add(self, actor):
        """
        Add an actor to the repository
        actor - Actor to be added
        """
        self._data.append(actor)
    
    def removeID(self, id):
        '''
        remove actor by id
        id - Actor's id
        '''
        i = 0
        for actor in self._data:
            if actor.getID() == id:
                self._data.pop(i)
            i = i + 1
    
    def getAll(self):
        """
        Return all repository data
        Returns the live list of the repository
        """
        return self._data
    
class FileActorRepository(ActorRepository):
    def __init__(self, filename):
        """
        Constructor for repository with file class
        filename - name of the file containing data
        loadFromFile - method - loads data into application
        """
        ActorRepository.__init__(self)
        self.__fName = filename
        self.__loadFromFile()
        
    def __loadFromFile(self):
        '''
        loads data into application
        '''
        f = open(self.__fName, "r")
        line = f.readline().strip()
        while line != "":
            attrs = line.split(",")
            self._data.append(Actor(int(attrs[0]), attrs[1], attrs[2], attrs[3], attrs[4], attrs[5], attrs[6], int(attrs[7]), attrs[8], attrs[9]))
            line = f.readline().strip()
        f.close()
        
    def add(self, actor):
        """
        Add an actor to the repository
        actor - Actor to be added
        """
        ActorRepository.add(self, actor);
        self.__storeToFile()
        
    def removeID(self, id):
        '''
        remove actor by id
        id - Actor's id
        '''
        ActorRepository.removeID(self, id)
        self.__storeToFile()
        
    def __storeToFile(self):
        '''
        stores data into application
        '''
        f = open(self.__fName, "w")
        actors = ActorRepository.getAll(self)
        for actor in actors:
            line = str(actor.getID()) + "," + actor.getFirstName() + "," + actor.getLastName() + "," + actor.getBirthday() + "," + actor.getNationality() + "," + actor.getResidence() + "," + actor.getHeight() + "," + str(actor.getWeight()) + "," + actor.getEmail() + "," + actor.getPhone() + "\n"
            f.write(line)
        f.close()
        
class RepositoryException(Exception):
    """
    Exception class for repository errors
    """
    def __init__(self, message):
        """
        Constructor for repository exception class
        message - A string representing the exception message
        """
        self.__message = message

    def __str__(self):
        return self.__message

            