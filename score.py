class Score:
    def __init__(self, num_typed, length, WPM, seconds):
        super().__init__()
        self.seconds = seconds
        self.num_chars_typed = num_typed
        self.game_cond = True
        self.length = length
        self.WPM = WPM

    def measure(self):
        if self.num_chars_typed < self.length:
            self.seconds += 1
            wpm = (self.num_chars_typed / 5) / (self.seconds / 60)
        else:
            self.game_cond = False
            self.WPM.config(text="")
            return self.game_cond, self.seconds

        self.WPM.config(text="WPM = " + str(round(wpm)))

        return self.game_cond, self.seconds
