import time

class Timer(object):
    def __init__(self):
        self._start = None
        self._end = None
        self._config = 'seconds'
        self._lastTime = None
    
    def start(self):
        if self._start is None:
            self._start = time.time()
        else:
            print 'The timer was already started'
    
    def end(self):
        if self._start is None:
            print 'The timer was never started'
        else:
            self._end = time.time()
            self._lastTime = self._end - self._start
            self._start, self._end = None, None
            self.displayTime(self._lastTime)
    
    def configure(self, option):
        self._config = option

    def displayTime(self, t):
        if self._config == 'seconds':
            print self._lastTime, 'seconds'
        elif self._config == 'minutes':
            print self._lastTime / 60, 'minutes'
        elif self._config == 'hours':
            print self._lastTime / 3600, 'hours'
    
    def lastTime(self):
        self.displayTime(self._lastTime)
        

