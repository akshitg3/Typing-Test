import re
import time
import tkinter

import score

import threading


class GameLogic:

    def __init__(self, sample_text, window, text_window, WPM, next_button, player_stats_label, player_stats,
                 final_stats):
        self.sample_text = sample_text

        self.window = window
        self.text_window = text_window
        self.final_stats = final_stats

        self.num_chars_typed = 0
        self.incorrect_count = 0

        self.num_correct = len(self.sample_text)

        self.speed_count = 0

        self.game_condition = True

        self.length_text = len(self.sample_text)

        self.WPM = WPM

        self.speed_measure_thread = threading.Thread(target=self.measure_speed)

        self.started = False

        self.next_button = next_button

        self.player_stats_label = player_stats_label

        self.player_stats = player_stats

    def onKeyPress(self, event):

        if self.num_chars_typed < len(self.sample_text) and re.search(
                "[a-zA-z0-9\.\+\?\^\$\(\)\[\]\{\}\|\\&#@!_\"'<>:; ,-]", event.char):

            if not self.started:
                self.speed_measure_thread.start()
                self.next_button['state'] = tkinter.DISABLED
                self.started = True

            if self.sample_text[self.num_chars_typed] == event.char and self.incorrect_count == 0:
                self.text_window.tag_add("correcttexttag", "1.0", f"1.{self.num_chars_typed + 1}")
                self.text_window.tag_config("correcttexttag", background="green")
                self.num_chars_typed += 1
                if self.num_chars_typed == len(self.sample_text):
                    self.final_stats.config(
                        text=f"Final Stats:\n\n\n"
                             f"WPM = {str(round((self.num_chars_typed / 5) / (self.speed_count / 60)))}\n\n"
                             f"Your accuracy was {round((self.num_correct / len(self.sample_text)) * 100, 1)}%\n\n"
                             f"Time taken was {self.speed_count}s")
                    self.window.unbind('<Key>')

                    self.player_stats.update_stats(round((self.num_chars_typed / 5) / (self.speed_count / 60)))

                    self.player_stats_label.config(text=f"Player Statistics:\n\n\n"
                                                        f"Number of races: {self.player_stats.num_tests}\n\n"
                                                        f"Average Speed: {self.player_stats.avg_speed}\n\n")
                    self.next_button['state'] = tkinter.NORMAL
            else:
                if self.incorrect_count == 0:
                    self.num_correct -= 1
                self.incorrect_count += 1
                self.text_window.tag_add("incorrecttexttag", f"1.{self.num_chars_typed}",
                                         f"1.{self.incorrect_count + self.num_chars_typed}")
                self.text_window.tag_config("incorrecttexttag", background="red")

        elif 0 < self.num_chars_typed < len(self.sample_text) and event.char == "\b":
            if self.incorrect_count > 0:
                self.text_window.tag_remove("incorrecttexttag", f"1.{self.num_chars_typed + self.incorrect_count - 1}",
                                            f"1.{self.num_chars_typed + self.incorrect_count}")
                self.incorrect_count -= 1

        elif self.num_chars_typed == 0 and event.char == "\b":
            if self.incorrect_count > 0:
                self.text_window.tag_remove("incorrecttexttag", f"1.{self.num_chars_typed + self.incorrect_count - 1}",
                                            f"1.{self.num_chars_typed + self.incorrect_count}")
                self.incorrect_count -= 1

    def measure_speed(self):
        while self.game_condition:
            time.sleep(1)
            self.game_condition, self.speed_count = score.Score(self.num_chars_typed, self.length_text,
                                                                self.WPM, self.speed_count).measure()
