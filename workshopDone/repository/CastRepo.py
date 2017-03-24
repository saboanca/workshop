'''
Created on 23 mar. 2017

@author: ABoanca
'''

class CastRepository:
    def __init__(self):
        '''
        Constructor for repository class
        '''
        self._data = []
        
    def __len__(self):
        """
        Overriding the len() built-in function
        """
        return len(self._data)
    
    def addMovie(self, idMovie):
        '''
        adds to the repository the id of the movie(parameter)
        then, adds the list of actors corresponding to the movie
        '''
        listActors = []
        self._data.append(idMovie)
        self._data.append(listActors)
        
    def lengthList(self, idMovie):
        '''
        returns the length of the actors' list for movie havinf idMovie(parameter)
        '''
        for index in range(0, len(self._data)):
            if index % 2 == 1:
                return len(self._data[index])
        
    def addActor(self, idMovie, idActor):
        '''
        searches in the repo for the movie having idMovie(parameter)
        when it finds the movie, it goes to the list associated with the movie, containing the actors
        appends in the list of actors, idActor(parameter)
        '''
        for index in range(0, len(self._data)):
            if index % 2 == 0 and self._data[index] == idMovie:
                index = index + 1
                self._data[index].append(idActor)
    
    def removeActor(self, idActor):
        '''
        searches in every the list of actor ids the idActor(parameter)
        when it finds the idActor in a list it removes it
        '''
        for index in range(0, len(self._data)):
            if index % 2 == 1:
                position = 0
                for id in self._data[index]:
                    if id == idActor:
                        self._data[index].pop(position)
                    position = position + 1
                    
    def removeActorFromMovie(self, idMovie, idActor):
        '''
        searches in movie list the ids the idActor(parameter)
        when it finds the idActor in a list it removes it
        '''
        for index in range(0, len(self._data)):
            if index % 2 == 0 and self._data[index] == idMovie:
                index = index + 1
                position = 0
                for id in self._data[index]:
                    if id == idActor:
                        self._data[index].pop(position)
                    position = position + 1
                    
    def removeMovie(self, idMovie):
        '''
        searches for the idMovie(parameter) in the repo
        when it finds it, it removes it, together with the list of actors associated to it
        '''
        for index in range(0, len(self._data)):
            if index % 2 == 0 and self._data[index] == idMovie:
                self._data.pop(index)
                self._data.pop(index)
                
    def checkID(self, idMovie, idActor):
        '''
        searches if an idActor(parameter) has already been added for a idMovie(parameter)
        return 1 if so, 0 otherwise
        '''
        for index in range(0, len(self._data)):
            if index % 2 == 0 and self._data[index] == idMovie:
                for id in self._data[index + 1]:
                    if id == idActor:
                        return 1
        return 0
    
    def getAll(self):
        """
        Return all repository data
        Returns the live list of the repository
        """
        return self._data

class FileCastRepository(CastRepository):
    def __init__(self, filename):
        """
        Constructor for repository with file class
        filename - name of the file containing data
        loadFromFile - method - loads data into the application
        """
        CastRepository.__init__(self)
        self.__fName = filename
        self.__loadFromFile()
        
    def __loadFromFile(self):
        '''
        loadsdata from file
        '''
        f = open(self.__fName, "r")
        line = f.readline().strip()
        while line != "":
            attrs = line.split(",")
            self._data.append(int(attrs[0]))
            list = []
            for index in range(1, len(attrs)):
                list.append(int(attrs[index]))
            self._data.append(list)
            line = f.readline().strip()
        f.close()
        
    def addActor(self, idMovie, idActor):
        """
        Add a movie to the repository
        movie - Movie to be added
        """
        CastRepository.addActor(self, idMovie, idActor);
        self.__storeToFile()
        
    def addMovie(self, idMovie):
        """
        Add a movie to the repository
        movie - Movie to be added
        """
        CastRepository.addMovie(self, idMovie);
        self.__storeToFile()
        
    def removeActor(self, idActor):
        '''
        remove movie by id
        id - movie id
        '''
        CastRepository.removeActor(self, idActor)
        self.__storeToFile()
        
    def removeMovie(self, idMovie):
        '''
        remove movie by id
        id - movie id
        '''
        CastRepository.removeMovie(self, idMovie)
        self.__storeToFile()
        
    def removeActorFrommovie(self, idMovie, idActor):
        '''
        remove actor by id from movie list
        isMovie - movie id
        idActor - actor id
        '''
        CastRepository.removeActorFromMovie(self, idMovie, idActor)
        self.__storeToFile()
        
    def __storeToFile(self):
        '''
        stores data to file
        '''
        f = open(self.__fName, "w")
        castList = CastRepository.getAll(self)
        entry = 0
        for index in range(0, len(castList)):
            if index % 2 == 0:
                line = str(castList[index])
                entry = entry + 1
            else:
                for id in castList[index]:
                    line += "," +  str(id)
                line += "\n"
                entry = entry + 1
            if entry == 2:
                f.write(line)
                entry = 0
        f.close()