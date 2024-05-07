import threading
from typing import Optional

from game import Game
from millionaire_game.question import Question


class TimedGame(Game):
    def __init__(self, questions, time_limit):
        super().__init__(questions)
        self.timer = None
        self.time_limit = time_limit

    def start_timer(self):
        print(f"Time started...! You have {self.time_limit} sec")
        self.timer = threading.Timer(self.time_limit, self.time_up)
        self.timer.start()

    def time_up(self):
        print("Time over!!!")
        self.submit_answer(None)

    def get_next_question(self) -> Optional[Question]:
        if self._current_question_index < len(self.questions):
            question = self.questions[self._current_question_index]
            self._current_question_index += 1
            self.start_timer()
            return question
        else:
            return None

    def submit_answer(self, answer):
        if self.timer:
            self.timer.cancel()

        if answer is None:
            print("---> Didn't answer on time!")
            return False

        if super().submit_answer(answer):
            return True
        else:
            self._score -= 10
            print(f"Wrong!")
            return True


    def show_best_time(self):
        return f'Player best time: {self.time_limit}'


    def __str__(self):
        return f'time--> {self.time_limit}'



def main():
    from question import Question
    question_list = [
        Question("What is the capital of France?", ["London", "Paris", "Berlin", "Madrid"], "Paris", difficulty='easy'),
        Question("What is 2 + 2?", ["3", "4", "2", "5"], "4",  difficulty='easy'),
        Question("Who wrote 'Macbeth'?", ["Shakespeare", "Austen", "Joyce", "Hemingway"], "Shakespeare", difficulty='easy'),
    ]

    game = TimedGame(question_list, 10)
    print(game)
    print(game.show_best_time)
    game.time_limit = 100
    print(game)
    print(game.show_best_time)


if __name__ == '__main__':
    main()