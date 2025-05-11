from otree.api import *
import random

class Constants(BaseConstants):
    name_in_url = 'grid_count_task'
    players_per_group = None
    num_rounds = 1
    time_limit_seconds = 3 * 60
    grid_size = 58
    target_symbol = '0'
    target_count = 236

def generate_grid():
    total_cells = Constants.grid_size * Constants.grid_size
    cells = ['0'] * Constants.target_count + ['1'] * (total_cells - Constants.target_count)
    random.shuffle(cells)
    grid = [cells[i:i + Constants.grid_size] for i in range(0, total_cells, Constants.grid_size)]
    return grid

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    count_answer = models.IntegerField()
    is_correct = models.BooleanField()
    completion_time = models.IntegerField()

class GridCountTask(Page):
    timeout_seconds = Constants.time_limit_seconds
    form_model = 'player'
    form_fields = ['count_answer', 'completion_time']

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'grid': generate_grid(),
            'time_limit_seconds': Constants.time_limit_seconds,
        }

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.is_correct = player.count_answer == Constants.target_count

        # If the timeout happened, ensure completion_time is set to the full duration
        if timeout_happened:
            player.completion_time = Constants.time_limit_seconds
        # Consider partially correct answers as correct
        player.is_correct = player.count_answer > 0

class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return {
            'is_correct': player.is_correct,
            'actual_count': Constants.target_count,
            'participant_count': player.count_answer,
            'completion_time': player.completion_time
        }

page_sequence = [GridCountTask, Results]