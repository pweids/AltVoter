'''
Inspired by an episode of West Wing where Josh claimed to get 6 heads in a row. I wanted to see how long it might take to do this in the real world.
'''

import random

class Flipper:

    flipCount = 0
    tally = 0
    rally = 1

    def flipper(self, n):
        while True:
            a, b = random.randint(0,n), random.randint(0,n)
            if a == b:
                self.tally += 1
                if self.flipCount < self.tally:
                    self.flipCount = self.tally
                    print('New high score: {0:2} on rally {1:,}'.format(self.tally, self.rally))
            else:
                self.tally = 0
                self.rally += 1

if __name__ == '__main__':
    flip = Flipper()
    flip.flipper(20)