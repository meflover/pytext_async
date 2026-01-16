import time
class RateLimiter:
    def __init__(self, limit=30, interval=1.0):
        self.score = 0
        self.limit = limit
        self.interval = interval

    def acquire(self):
        while self.score >= self.limit:
            time.sleep(self.interval)
            self.score = 0
        self.score += 1
limiter = RateLimiter()