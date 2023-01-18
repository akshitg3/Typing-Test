import tkinter

import game_logic
import player_stats
import quotes


class GUI:
    def __init__(self):
        self.window = tkinter.Tk()
        self.geometry = '1280x720'

        self.text_window = tkinter.Text(self.window)

        self.title = tkinter.Label(self.window)
        self.WPM = tkinter.Label(self.window)
        self.final_stats = tkinter.Label(self.window)
        self.player_stats = tkinter.Label(self.window)

        self.stats_player = player_stats.PlayerStats()

        self.generated_text = None

        self.logic = None

        self.new_text_button = tkinter.Button(self.window, text="Get New Text", command=self.get_new_text)

        self.initialize_window()

    def initialize_window(self):
        self.window.geometry(self.geometry)
        self.window.title('Typing Test')

        self.get_new_text()

        self.initialize_title()

        self.display_text_window()
        self.display_WPM()
        self.display_final_stats()
        self.display_next_button()

        self.initialize_player_stats()

        self.window.mainloop()

    def get_new_text(self):
        self.text_window.configure(state="normal")
        self.generated_text = quotes.Text().get_text()

        self.text_window.delete(1.0, tkinter.END)
        self.text_window.insert(tkinter.INSERT, self.generated_text)
        self.text_window.configure(state="disabled")

        self.final_stats.config(text="")

        self.logic = game_logic.GameLogic(self.generated_text, self.window, self.text_window, self.WPM,
                                          self.new_text_button, self.player_stats, self.stats_player,
                                          self.final_stats)
        self.window.bind('<Key>', self.logic.onKeyPress)

    def initialize_title(self):
        self.title.config(text="Typing Test",font=('Helvetica bold', 26),foreground='red')
        self.title.pack(expand=1)

    def initialize_player_stats(self):
        self.player_stats.config(text=f"Player Statistics:\n\n\n"
                                      f"Number of races: {self.stats_player.num_tests}\n\n"
                                      f"Average Speed: {self.stats_player.avg_speed}\n\n")
        self.player_stats.pack(side=tkinter.LEFT)

    def display_text_window(self):
        self.text_window.pack(expand=1)

    def display_WPM(self):
        self.WPM.pack(expand=1)

    def display_final_stats(self):
        self.final_stats.pack(expand=1)

    def display_next_button(self):
        self.new_text_button.pack(side=tkinter.RIGHT, padx=15, pady=15)
