import numpy as np

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
        self.orientation = 0
        self.maze_dim = maze_dim
        self.visited = np.zeros((maze_dim, maze_dim))
        self.visited[0,0] = 1
        self.goal = [[maze_dim/2, maze_dim/2], [maze_dim/2-1, maze_dim/2-1], [maze_dim/2, maze_dim/2-1], [maze_dim/2-1, maze_dim/2]]

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
        print sensors
        #print self.goal
        rotation = -90
        movement = 1
        Robot.updateHeading(self, rotation)
        Robot.updateLocation(self, movement)
        print self.heading
        #test = [6, 6]
        #self.visited[6][6] += 1
        print Robot.goalFound(self)
        
        print self.location
        print self.visited
        return rotation, movement
    
    def visited(self):
        
        return
        
    def goalFound(self):
        for i in range(4):
            if self.visited[self.goal[i][0]][self.goal[i][1]] > 0:
                return 'Found It!!'
        return
    
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
        self.visited[self.location[0]][self.location[1]] += 1
        return
        
        
