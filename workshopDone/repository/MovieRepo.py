'''
Created on 15 mar. 2017

@author: ABoanca
'''

from domain.Movie import Movie


class MovieRepository:
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
    
    def add(self, movie):
        """
        Add a movie to the repository
        movie - Movie to be added
        """
        self._data.append(movie)
    
    def removeID(self, id):
        '''
        remove movie by id
        id - movie id
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
    
class FileMovieRepository(MovieRepository):
    def __init__(self, filename):
        """
        Constructor for repository with file class
        filename - name of the file containing data
        loadFromFile - method - loads data into the application
        """
        MovieRepository.__init__(self)
        self.__fName = filename
        self.__loadFromFile()
        
    def __loadFromFile(self):
        '''
        loadsdata from file
        '''
        f = open(self.__fName, "r")
        #except IOError:
            #print("Error while opening " + self.__fName)
        line = f.readline().strip()
        while line != "":
            attrs = line.split(",")
            self._data.append(Movie(int(attrs[0]), attrs[1], int(attrs[2]), attrs[3]))
            line = f.readline().strip()
        f.close()
        
    def add(self, movie):
        """
        Add a movie to the repository
        movie - Movie to be added
        """
        MovieRepository.add(self, movie);
        self.__storeToFile()
        
    def removeID(self, id):
        '''
        remove movie by id
        id - movie id
        '''
        MovieRepository.removeID(self, id)
        self.__storeToFile()
        
    def __storeToFile(self):
        '''
        stores data to file
        '''
        f = open(self.__fName, "w")
        #f.write()
        movies = MovieRepository.getAll(self)
        for movie in movies:
            line = str(movie.getID()) + "," + movie.getName() + "," + str(movie.getYear()) + "," + movie.getWebsite() + "\n"
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

            