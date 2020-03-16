from threading import Condition, Lock

"""a simple implementation of barrier"""
class Barrier():
    def __init__(self, parties, action = None):
        self.parties = parties
        self.n_waiting = 0
        self.cond = Condition(Lock())
        self.action = action


    def wait(self):
        with self.cond:
            self.n_waiting += 1
            if self.n_waiting < self.parties:
                self.cond.wait()

            elif self.n_waiting >= self.parties:
                if self.action:
                    self.action()
                self.cond.notify_all()

