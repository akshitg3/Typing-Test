class PlayerStats:
    def __init__(self):
        self.num_tests = 0
        self.speed = 0
        self.avg_speed = 0

    def update_stats(self, speed):
        self.num_tests += 1
        self.speed += speed
        self.avg_speed = self.speed / self.num_tests
        self.avg_speed = round(self.avg_speed)
