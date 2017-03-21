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
        
        print('Move count is: %s' % self.move_count)
        print('Location is: %s' % self.location)
        print('Heading is: %s' % self.heading)
        print('Sensor readings (l, f, r) are: %s' % sensors)
        print('Visits grid:')
        self.visited[self.location[0]][self.location[1]] += 1
        print self.visited
        
        # Create various move functions - random move, minimum visits, A*
        
        moves = Robot.validMoves(self, sensors)
        print('Valid moves are: %s' % moves)
        
        minVisitMove = Robot.minVisitMove(self, moves)
        print ('Min visit move is: %s' % minVisitMove)
        
        if Robot.goalFound(self) == True:
            rotation, movement = 'Reset', 'Reset'
        else:
            moveSelector = random.randint(1, len(moves)) - 1
            rotation = moves[moveSelector][0]
            movement = moves[moveSelector][1]
        
        if rotation != 'Reset':
            Robot.updateHeading(self, rotation)
            Robot.updateLocation(self, movement)
        else:
            self.location = [0, 0]
            self.heading = 'up'
            self.move_count = 0
            self.orientation = 0
            self.visited = np.zeros((self.maze_dim, self.maze_dim))

        self.move_count += 1
                
        print('Move chosen is rotation: %s, movement: %s' % (rotation, movement))
        
        return rotation, movement
        
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
        #self.visited[self.location[0]][self.location[1]] += 1
        return
        
    def goalFound(self):
        goal_bounds = [self.maze_dim/2 - 1, self.maze_dim/2]
        if self.location[0] in goal_bounds and self.location[1] in goal_bounds:
            return True
            
    def minVisitMove(self, moves):
        newLocation = []
        visits = []
        for move in moves:
            newOrientation = self.orientation + move[0]
            if newOrientation == 360:
                newOrientation = 0
            elif newOrientation == -90:
                newOrientation = 270
            
            # Need to fix this function - it's not giving a full (x,y) location right now
            # create the new location in one variable, then append it to a location list at the end of the ifs
            # then do code on that for the min
            if newOrientation == 0:
                newLocation.append(self.location[1] + move[1])
            elif newOrientation == 90:
                newLocation.append(self.location[0] + move[1])
            elif newOrientation == 180:
                newLocation.append(self.location[1] - move[1])
            elif newOrientation == 270:
                newLocation.append(self.location[0] - move[1])
            #visits.append(self.visited[newLocation[0]][newLocation[1]])
            #print(self.visited[newLocation[0]][newLocation[1]])
            print newLocation
        print('Visits for potential move spots: %s' % visits)
        #moveIndex = visits.index(min(visits))
        #return moveIndex

