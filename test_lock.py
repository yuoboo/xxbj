import threading
import time


class MyThead(threading.Thread):

    def _funca(self):
        if _lockA.acquire():
            print 'funca'
            time.sleep(1)
            print threading.Thread.name
            if _lockB.acquire():
                print 'this is lockB'
                _lockB.release()
            _lockA.acquire()

    def _funcb(self):
        if _lockB.acquire():
            print 'funcb'
            time.sleep(1)
            if _lockA.acquire():
                _lockB.release()
            _lockB.release()

    # def run(self):
    #     time.sleep(1)
    #     if _lockA.acquire():
    #         print threading.Thread.name
    #         time.sleep(1)
    #         _lockB.acquire()
    #         time.sleep(2)
    #         _lockB.release()
    #         _lockA.release()
    def run(self):
        self._funca()
        self._funcb()


_lockA = threading.Lock()
_lockB = threading.Lock()


def test():
    for i in range(5):
        t = MyThead()
        t.start()


if __name__ == '__main__':
    test()
