import threading
from barrier import  Barrier

barrier = Barrier(10)

class thread(threading.Thread):
    def __init__(self, thread_ID):
        threading.Thread.__init__(self)
        self.thread_ID = thread_ID
    def run(self):
        print("before barrier|thread_id={0}".format(str(self.thread_ID)))
        barrier.wait()
        print("after barrier|thread_id={0}".format(str(self.thread_ID)))

threads = []

for i in range(10):
    threads.append(thread(i))

for t in threads:
    t.start()
barrier.wait()
print("Exit\n")