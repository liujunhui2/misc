class Recursive(object):
    def __init__(self, data):
        # inventory
        self.inv = []
        self.end = False

        # initialize inventory
        for d in data:
            # inventory: len, cur, data
            self.inv.append([len(d), 0, d])

    def next(self):
        # will return an array of current positions
        p = []
        for i in range(len(self.inv)):
            p.append(self.inv[i][2][self.inv[i][1]])
        if self.end:
            return []

        # try increase position by 1

        for i in range(len(self.inv)):
            self.inv[i][1] += 1
            if self.inv[i][1] < self.inv[i][0]:
                break
            if i == len(self.inv)-1:
                self.end = True
            self.inv[i][1]=0

        return p

''' example code

data = [['a', 'b'], ['e', 'f', 'g'], ['c', 'd']]

r = Recursive(data)
while True:
   d = r.next()
   if len(d) == 0:
        break;
    print d
'''
