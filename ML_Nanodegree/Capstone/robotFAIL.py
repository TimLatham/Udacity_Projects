import numpy as np
import random

class Robot(object):
    def __init__(self, maze_dim):
        '''
        Use the initialization function to set up attributes that your robot
        will use to learn and navigate the maze. Some initial attributes are
        provided based on common information, including the size of the maze
        the robot is placed in.
        '''

        self.location = [0, 0]
        self.heading = 'up'
        self.maze_dim = maze_dim
        self.move_count = 0
        self.orientation = 0
        self.visited = np.zeros((maze_dim, maze_dim))
        self.liveRun = 0
        self.liveMoves = 0
        self.distances = np.zeros((maze_dim, maze_dim))
        Robot.calcDistances(self)
        self.positionValues = np.zeros((maze_dim, maze_dim)) + self.distances

    def next_move(self, sensors):
        '''
        Use this function to determine the next move the robot should make,
        based on the input from the sensors after its previous move. Sensor
        inputs are a list of three distances from the robot's left, front, and
        right-facing sensors, in that order.
        Outputs should be a tuple of two values. The first value indicates
        robot rotation (if any), as a number: 0 for no rotation, +90 for a
        90-degree rotation clockwise, and -90 for a 90-degree rotation
        counterclockwise. Other values will result in no rotation. The second
        value indicates robot movement, and the robot will attempt to move the
        number of indicated squares: a positive number indicates forwards
        movement, while a negative number indicates backwards movement. The
        robot may move a maximum of three units per turn. Any excess movement
        is ignored.
        If the robot wants to end a run (e.g. during the first training run in
        the maze) then returing the tuple ('Reset', 'Reset') will indicate to
        the tester to end the run and return the robot to the start.
        '''
        
        print('Search move count is: %s' % self.move_count)
        print('Live run move count is: %s' % self.liveMoves)
        print('Location is: %s' % self.location)
        x = self.location[0]
        y = self.location[1]
        print('Distance to goal is: %s' % self.distances[x][y])
        #print('Distance to goal is: %s' % self.distances[self.location[0]][self.location[1]])
        print('Heading is: %s' % self.heading)
        print('Sensor readings (l, f, r) are: %s' % sensors)
        print('Visits grid:')
        
        
        if self.liveRun == 0:
            self.visited[self.location[0]][self.location[1]] += 1
            self.positionValues = self.distances + self.visited        
        
        #self.visited[self.location[0]][self.location[1]] += 1
        #self.positionValues = self.distances + self.visited        
        
        
        print self.visited
        print self.positionValues
        
        moves = Robot.validMoves(self, sensors)
        print('Valid moves are: %s' % moves)
        
        minDistanceMove = Robot.minDistMove(self, moves, x, y)
        print('Min distance move is: %s' % minDistanceMove)
        print moves[minDistanceMove]
        
        if Robot.goalFound(self) == True:
            rotation, movement = 'Reset', 'Reset'
        else:
            rotation = moves[minDistanceMove][0]
            movement = moves[minDistanceMove][1]
        
        if rotation != 'Reset':
            Robot.updateHeading(self, rotation)
            Robot.updateLocation(self, movement)
        else:
            self.location = [0, 0]
            self.heading = 'up'
            #self.move_count = 0
            self.liveRun = 1
            self.orientation = 0
            #self.visited = np.zeros((self.maze_dim, self.maze_dim))
        
        if self.liveRun == 0:
            self.move_count += 1
        else:
            self.liveMoves += 1
                
        print('Move chosen is rotation: %s, movement: %s' % (rotation, movement))
        #dist = Robot.manhattanDistance(self) 
        #print('Manhattan distance to goal is: %s' % dist)
        
        return rotation, movement
        
    def calcDistances(self):
        lowerLeft = (self.maze_dim/2-1, self.maze_dim/2-1)
        upperLeft = (self.maze_dim/2-1, self.maze_dim/2)
        lowerRight = (self.maze_dim/2, self.maze_dim/2-1)
        upperRight = (self.maze_dim/2, self.maze_dim/2)
        goal = [lowerLeft, upperLeft, lowerRight, upperRight]
        
        for x in range(len(self.distances)):
            for y in range(len(self.distances)):
                distance = []        
                for corner in goal:
                    distance.append((np.absolute(x - corner[0]) + np.absolute(y - corner[1])))
                self.distances[x][y] = min(distance)
        return 
    
    def validMoves(self, sensors):
        moves = []
        maxMove = 1
        # change this to a loop when refactoring?
        if sensors[0] > 0:
            moves.append((-90, maxMove))
        if sensors[1] > 0:
            moves.append((0, maxMove))
        if sensors[2]>0:
            moves.append((90, maxMove))
        if sum(sensors) == 0:
            moves.append((-90, 0))
        return moves
        
    def minDistMove(self, moves, x, y):
        newLocationList = []
        distances = []
        orientation = []
        orientation.append(self.orientation)
                
        for move in moves:
            newOrientation = orientation[0] + move[0]
            if newOrientation == 360:
                newOrientation = 0
            elif newOrientation == -90:
                newOrientation = 270
            
            if newOrientation == 0:
                y += move[1]
            elif newOrientation == 90:
                x += move[1]
            elif newOrientation == 180:
                y -= move[1]
            elif newOrientation == 270:
                x -= move[1]
            newLocation = (x, y)
            newLocationList.append(newLocation)
            distances.append(self.visited[x][y])
        moveIndex = distances.index(min(distances))
        return moveIndex
    
    def updateHeading(self, rotation):
        direction = {0: 'up', 90: 'right', 180: 'down', 270: 'left'}
        #self.orientation = direction.keys()[direction.values().index(self.heading)]
        self.orientation = self.orientation + rotation
        if self.orientation == 360:
            self.orientation = 0
        elif self.orientation == -90:
            self.orientation = 270
        self.heading = direction[self.orientation]
        return

    def updateLocation(self, movement):
        if self.orientation == 0:
            self.location[1] += movement
        elif self.orientation == 90:
            self.location[0] += movement
        elif self.orientation == 180:
            self.location[1] -= movement
        elif self.orientation == 270:
            self.location[0] -= movement
        return
        
    def goalFound(self):
        goal_bounds = [self.maze_dim/2 - 1, self.maze_dim/2]
        if self.location[0] in goal_bounds and self.location[1] in goal_bounds:
            return True