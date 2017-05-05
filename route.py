import numpy as np



class Route:
    
    def __init__(self, actual_position, route_coordinates):
        # order the route_coordinates based on the actual_position
        # The closes should be the first element, etc
        distances = [actual_position.distanceTo(visitable_coordinate) for visitable_coordinate in route_coordinates]
        min_idx = np.argmin(distances)
        
        self.ordered_coordinates = route_coordinates[min_idx:] + route_coordinates[0:min_idx]
        None
        
    def getCurrentGoal(self):
        return self.ordered_coordinates[0]
    
    def markCurrentGoalVisited(self):
        self.ordered_coordinates = self.ordered_coordinates[1:]
        