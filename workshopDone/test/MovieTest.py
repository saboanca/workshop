'''
Created on 23 mar. 2017

@author: ABoanca
'''
import unittest
from repository.MovieRepo import *
from repository.CastRepo import *
from domain.Movie import *
from controller.MovieController import *

class RepositoryTest(unittest.TestCase):
    '''
    Unit test case for repository and controller for class Movie
    '''
    def setUp(self):
        self._repo = MovieRepository()
        self._castRepo = CastRepository()
        self._controller = MovieController(self._repo, self._castRepo)
        
    def testMovie(self):
        '''
        tests add, remove, getAll, len for movie in repository
        '''
        self.assertEqual(len(self._repo), 0)
        movie = Movie(1, "ex", 2010, "www.yahoo.com")
        self._repo.add(movie)
        self.assertEqual(len(self._repo), 1)
        self.assertEqual(len(self._repo.getAll()), 1)
        self._repo.removeID(1)
        self.assertEqual(len(self._repo.getAll()), 0)
        '''
        tests add, remove, getAll, len, checkID for movie in controller
        '''
        self.assertEqual(len(self._castRepo), 0)
        self.assertEqual(len(self._controller.getAll()), 0)
        movie = Movie(1, "ex", 2010, "www.yahoo.com")
        self._controller.add(movie)
        self._controller.addMovie(11, "ex", 2010, "www.yahoo.com")
        self.assertEqual(len(self._controller.getAll()), 2)
        '''
        if id doesn't exist, returns 1
        '''
        self.assertEqual(self._controller.checkID(0), 1)
        '''
        if id exists, returns 0
        '''
        self.assertEqual(self._controller.checkID(1), 0)
        self._controller.removeID(1)
        self.assertEqual(len(self._castRepo), 2)
        self.assertEqual(len(self._controller.getAll()), 1)
        self._controller.addMovie(1, "ex", 2010, "www.yahoo.com")
        self.assertEqual(len(self._controller.getAll()), 2)
        self.assertEqual(len(self._castRepo), 4)
        self.assertEqual(self._controller.addMovie(2, "asc", 1212, "www.qqq.com"), 1)
        self.assertEqual(self._controller.addMovie(1, "asc", 1212, "www.qqq.com"), -1)
        
        '''
        test domain
        '''
        movie1 = Movie("a", "#", 216, "moonlight.com")
        ok = MovieValidator()
        self.assertEqual(movie1.getID(), "a")
        self.assertEqual(ok.idValidator(movie1.getID()), False)
        self.assertEqual(movie1.getName(), "#")
        self.assertEqual(ok.nameValidator(movie1.getName()), False)
        self.assertEqual(movie1.getYear(), 216)
        self.assertEqual(ok.yearValidator(movie1.getYear()), False)
        self.assertEqual(movie1.getWebsite(), "moonlight.com")
        self.assertEqual(ok.websiteValidator(movie1.getWebsite()), False)
        self.assertEqual(ok.validate(movie1), False)
        
        movie2 = Movie(1, "f!? ,rwf", 2016, "www.moonlight.com")
        ok = MovieValidator()
        self.assertEqual(movie2.getID(), 1)
        self.assertEqual(ok.idValidator(movie2.getID()), True)
        self.assertEqual(movie2.getName(), "f!? ,rwf")
        self.assertEqual(ok.nameValidator(movie2.getName()), True)
        self.assertEqual(movie2.getYear(), 2016)
        self.assertEqual(ok.yearValidator(movie2.getYear()), True)
        self.assertEqual(movie2.getWebsite(), "www.moonlight.com")
        self.assertEqual(ok.websiteValidator(movie2.getWebsite()), True)
        self.assertEqual(ok.validate(movie2), True)