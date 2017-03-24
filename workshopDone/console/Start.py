'''
Created on 22 mar. 2017

@author: ABoanca
'''
from domain.Actor import Actor
from domain.Movie import Movie
from domain.Actor import ActorValidator
from domain.Movie import MovieValidator
from repository.ActorRepo import *
from repository.MovieRepo import *
from repository.CastRepo import *
from controller.ActorController import *
from controller.MovieController import *
from controller.CastController import *
from ui.Menu import UI


repoActor = FileActorRepository("actors.csv")
repoMovie = FileMovieRepository("movies.csv")
repoCast = FileCastRepository("cast.csv")

controllerActor = ActorController(repoActor)
controllerMovie = MovieController(repoMovie, repoCast)
controllerCast = CastController(repoCast, repoActor)

ui = UI(controllerActor, controllerMovie, controllerCast)

ui.mainMenu()