#!/usr/bin/env python

#import gps
#import motor
#import path
from position import Position
import positioning_service

# constants need to be refined according to experience
MIN_DISTANCE_BETWEEN_POSITIONS = 1
MAX_DISTANCE_BETWEEN_POSITIONS = 10
MIN_MOVEMENT_DISTANCE = 2


class Robocar:
	
	
	def __init__(self):
		self.milestones = []
		self.milestones.extend(Position(47.47280197178266, 19.06173124909401))
		self.milestones.extend(Position(47.47157893570410, 19.061355739831924))
		self.milestones.extend(Position(47.471540474988444, 19.06233474612236))
		self.milestones.extend(Position(47.47172508616688, 19.063498824834824))
		self.milestones.extend(Position(47.47303529409086, 19.06308576464653))
		
#		self.refinedPositions = self.calculateRefinedPositions(MAX_DISTANCE_BETWEEN_POSITIONS)

	
	def main(self):
		print("Starting route")
		positioning_service = PositioningService()
		
		
		actualPosition = positioning_service.getActualPosition()
		route = Route(actualPosition, positions) # meghatározzuk az utat (köztes pontokkal vagy anélkül), ahol positions az input koordináták
		 
		while len(self.milestones) > 0: # Megnézzük, van-e még érintendő pont
		    previousPosition = actualPosition # később használjuk
		    actualPosition = PositioningService.getActualPosition()
		 
		    if (actualPosition.distanceTo(previousPosition) < MINIMUM_DISTANCE_TO_OTHER_COORD): # ha "egy helyben maradtunk" baj van
		        MotorFunctions.dodge() # random kitérés valamerre, úgysem látjuk mit kerülünk ki
		        continue
		 
		    closestVisitable = route.getCurrentGoal() # nem kell mindig kiszámolni, elég ha egy lista k. elemét adjuk mindig vissza
		    distanceToGoal = actualPosition.distanceTo(closestVisitable)
		   
		    if distanceToGoal < MINIMUM_DISTANCE_TO_OTHER_COORD:
		        route.markCurrentGoalVisited() # Elértük a célt, ezért töröljük a lista első elemét/léptetjük az indexet
		    # nem kell else ág, ha a következő célt nézzük, akkor arra korrigálunk majd, ha nem akkor a jelenlegire
		 
		    # Kiszámoljuk, hogy a jelenlegi irány jó-e, ha nem, korrigálunk
		    actualAngleToNorth = previousPosition.bearingTo(actualPosition) # most is fokot ad vissza, nem kell új függvény rá
		    desiredAngleToNorth = actualPosition.bearingTo(route.getCurrentGoal()) # most is fokot ad vissza, nem kell új függvény rá
		    angleDifference = actualAngleToNorth - desiredAngleToNorth # így ez is egyszerűsödik
		       
		    if abs(angle_difference) > MINIMUM_ANGLE: # Elég nagy-e az eltérés?
		        # Ha igen, negatív szögnél balra, pozitívnál jobbra korrigálunk
		        if angle_difference < 0:
		            MotorFunctions.TurnLeft()
		        else:
		            MotorFunctions.TurnRight()
		 
		    # végül mindenképp előre haladunk valamennyit
		    MotorFunctions.moveForward()
		print("Finished route")

