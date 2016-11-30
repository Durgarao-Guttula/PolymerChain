
import numpy as np
import matplotlib.pyplot as plt

class PolymerChain(object):
    
    def up(self):
        self.poly = [[self.head[0], self.head[1] + 1]] + self.poly
        self.poly = self.poly[:-1]
        return self.poly
    
    def down(self):
        self.poly = [[self.head[0], self.head[1] -1 ]] + self.poly
        self.poly = self.poly[:-1]
        return self.poly
        
    def right(self): 
        self.poly = [[self.head[0] + 1, self.head[1]]] + self.poly
        self.poly = self.poly[:-1]
        return self.poly
    
    def left(self):
        self.poly = [[self.head[0] - 1, self.head[1]]] + self.poly
        self.poly = self.poly[:-1]
        return self.poly
        
    def random(self):
        self.head = self.poly[0]
        [x,y] = self.head
        a = np.random.randint(0, 4)
        if a == 0 and not([x+1, y] in self.poly):
            self.poly = self.right()
        elif a == 1 and not([x-1, y] in self.poly):
            self.poly = self.left()
        elif a == 2 and not([x, y+1] in self.poly):
            self.poly = self.up()
        elif a == 3 and not([x, y-1] in self.poly):
            self.poly = self.down()
        else:
            self.poly = self.random()
        return self.poly

    def change(self):
        N = len(self.poly)
        change = []
        for i in xrange(0, N):
            change.append(self.poly[N-1-i])
        return change
    
    def occupied(self):
        self.head = self.poly[0]
        [x,y] = self.head
        if (([x+1, y] in self.poly) and ([x-1, y]in self.poly) and ([x, y+1]in self.poly) and ([x, y-1] in self.poly)):
            return True
        else:
            return False
    
    def endtoend(self):
        self.head = np.array(self.poly[0])
        self.tail = np.array(self.poly[-1])
        self.diff = self.head-self.tail
        self.dist = np.sqrt(np.sum(self.diff**2))
        return self.dist
    
    def update(self):
        if self.occupied():
            polymer = self.change()
        else:
            polymer = self.random()
        return polymer

    def plot(self,N, i = 0):
        self.dist = self.endtoend()
        self.distances.append(self.dist)
        self.mean = np.average(np.array(self.distances))
        self.head = np.array(self.poly[0])
        self.tail = np.array(self.poly[-1])
        plt.xlim(0,N)
        plt.ylim(0,N)
#        plt.axis('off')
        
        self.ax.plot(np.array(self.poly)[:, 0], np.array(self.poly)[:, 1], '-')
        self.ax.plot(self.head[0], self.head[1], 'ro')
        self.ax.plot(self.tail[0], self.tail[1], 'bo')

        
    distances = []
    fig = plt.figure()
    ax = fig.add_subplot(111)
    poly = []
    head = 0
    tail = 0
    diff = 0
    dist = 0
    mean = 0
    def final(self, T = 10, N = 50):
        for i in range(0, N):
            self.poly.append([ i+ N/2, N/2])
        for t in range(T): 
            self.poly = self.update()
            self.ax.clear()
            self.plot(N, t)
            plt.pause(0.1)
            print len(self.distances)


if __name__ == "__main__":
    sim = PolymerChain()
#    sim.final(100, 50)
    sim.final(500,100)


