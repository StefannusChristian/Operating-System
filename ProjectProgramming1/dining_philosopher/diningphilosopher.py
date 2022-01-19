import threading
import time
import argparse


class Philosopher(threading.Thread):

    is_all_eat = True

    def __init__(self, index, forkOnLeft, forkOnRight, capacity):
        threading.Thread.__init__(self)
        self.index = index
        self.forkOnLeft = forkOnLeft
        self.forkOnRight = forkOnRight
        self.capacity = capacity

    def run(self):
        while (self.is_all_eat):
            if self.capacity != 0:
                self.capacity -= 1
            else:
                break

            time.sleep(3)
            print('Philosopher %s is hungry.' % self.index)
            self.eat()

    def eat(self):
        fork1, fork2 = self.forkOnLeft, self.forkOnRight

        while self.is_all_eat:
            fork1.acquire()
            locked = fork2.acquire(False)
            if locked:
                break
            fork1.release()
        else:
            return

        self.dining()

        fork2.release()
        fork1.release()

    def dining(self):
        print('Philosopher %s starts eating. ' % self.index)
        time.sleep(3)
        print('Philosopher %s finishes eating and leaves to think.' % self.index)


def main(filsuf, makan):
    forks = [threading.Semaphore() for n in range(filsuf)]

    philosophers = [Philosopher(i, forks[i % filsuf], forks[(i + 1) % filsuf], makan)
                    for i in range(filsuf)]

    Philosopher.is_all_eat = True
    for p in philosophers:
        p.start()
    time.sleep(100)
    Philosopher.is_all_eat = False
    print("Now we're finishing.")


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--filsuf")
    parser.add_argument("--makan")
    args = parser.parse_args()
    filsuf = int(args.filsuf)
    makan = int(args.makan)
    return filsuf, makan


if __name__ == "__main__":
    filsuf, makan = parser()
    main(filsuf, makan)
