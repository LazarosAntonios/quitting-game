from otree.api import *

class Constants(BaseConstants):
    name_in_url = 'numbertype_task'
    players_per_group = None
    num_rounds = 1
    time_limit_seconds = 3 * 60  # 3 minutes
    numbers_to_sort = list(range(0, 100))  # Numbers from 0 to 100


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    sorted_numbers = models.LongStringField()  # Stores the participant's input
    correct_count = models.IntegerField(initial=0)  # Number of correctly sorted numbers
    completion_time = models.IntegerField(initial=0)  # Add this field


class NumberTypingTask(Page):
    timeout_seconds = Constants.time_limit_seconds
    form_model = 'player'
    form_fields = ['sorted_numbers', 'completion_time']

    def vars_for_template(self):
        import random
        shuffled_numbers = Constants.numbers_to_sort[:]
        random.shuffle(shuffled_numbers)
        return {
            'shuffled_numbers': shuffled_numbers,
            'time_limit_seconds': Constants.time_limit_seconds,
        }

    def before_next_page(self, **kwargs):  # Add **kwargs to handle timeout_happened
        try:
            participant_input = list(map(int, self.sorted_numbers.split(',')))  # Correct reference to `self.sorted_numbers`
            correct_order = sorted(Constants.numbers_to_sort, reverse=True)
            self.correct_count = sum(
                1 for i, j in zip(participant_input, correct_order) if i == j
            )
        except ValueError:
            self.correct_count = 0


class Results(Page):
    def vars_for_template(self):
        return {
            'correct_count': self.correct_count,
            'completion_time': self.completion_time,  # Add this line
        }


page_sequence = [NumberTypingTask, Results]
