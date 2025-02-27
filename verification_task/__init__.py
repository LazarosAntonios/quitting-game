# verification_task/__init__.py
from otree.api import *


class Constants(BaseConstants):
    name_in_url = 'verification_task'
    players_per_group = None
    num_rounds = 1
    timeout_seconds = 120  # 2 minutes
    grid_size = 16  # 4x4 grid
    required_rounds = 5  # Number of grids they need to complete

    # Define verification challenges
    verification_challenges = [
        {
            'prompt': "Click all squares that sum to exactly 10",
            'grid': [3, 7, 5, 2, 8, 1, 4, 6, 9, 0, 5, 8, 2, 4, 7, 3],
            'correct': [2, 7, 11, 15]  # Indices where correct answers are
        },
        {
            'prompt': "Click all squares containing an even number greater than 5",
            'grid': [2, 8, 3, 6, 1, 4, 10, 5, 7, 12, 9, 4, 8, 3, 6, 2],
            'correct': [1, 6, 9, 12]
        },
        {
            'prompt': "Click all squares where the number is a multiple of 3",
            'grid': [4, 9, 2, 6, 1, 3, 8, 12, 5, 15, 7, 9, 3, 6, 4, 18],
            'correct': [1, 3, 5, 7, 9, 11, 13, 15]
        },
        {
            'prompt': "Click all squares containing prime numbers",
            'grid': [4, 7, 9, 2, 11, 6, 13, 8, 15, 17, 10, 19, 12, 23, 16, 29],
            'correct': [1, 3, 4, 6, 9, 11, 13]
        },
        {
            'prompt': "Click all squares where the number is less than 5",
            'grid': [7, 2, 9, 4, 1, 6, 3, 8, 2, 10, 4, 7, 3, 5, 1, 8],
            'correct': [1, 4, 6, 8, 10, 12, 14]
        }
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    current_round = models.IntegerField(initial=0)
    correct_count = models.IntegerField(initial=0)
    completion_time = models.IntegerField(initial=0)
    quit_early = models.BooleanField(initial=False) # Change this to StringField with blank=True to allow empty submissions
    responses = models.StringField(blank=True)


class VerificationTask(Page):
    form_model = 'player'
    form_fields = ['responses', 'completion_time']

    @staticmethod
    def vars_for_template(player):
        import json  # Add this import
        return {
            'verification_challenges': json.dumps(Constants.verification_challenges),  # Convert to JSON string
            'timeout_seconds': Constants.timeout_seconds,
        }

    @staticmethod
    def is_displayed(player):
        return not player.participant.vars.get('finished', False)

    @staticmethod
    def before_next_page(player, timeout_happened):
        if timeout_happened:
            return

        if player.participant.vars.get('quit', False):
            try:
                end_index = player.session.config['app_sequence'].index('End')
                player.participant._index_in_pages = end_index
            except ValueError:
                player.participant._index_in_pages = len(player.session.config['app_sequence'])
            player.participant.vars['finished'] = True
            return

        # Process responses
        import json
        try:
            responses = json.loads(player.responses)
            # Calculate correct count based on responses
            player.correct_count = sum(1 for resp in responses
                                       if set(resp['selected']) == set(resp['correct']))
        except (json.JSONDecodeError, KeyError):
            player.correct_count = 0

class Results(Page):
    @staticmethod
    def vars_for_template(player):
        return {
            'correct_count': player.correct_count,
            'total_rounds': Constants.required_rounds,
            'completion_time': player.completion_time,
            'show_quit_option': player.session.config.get('quit_option', False)
        }

    @staticmethod
    def live_method(player, data):
        if data.get('action') == 'quit':
            player.participant.vars['quit'] = True
            player.participant.vars['finished'] = True
            player.quit_early = True
            try:
                end_index = player.session.config['app_sequence'].index('End')
                player.participant._index_in_pages = end_index
            except ValueError:
                player.participant._index_in_pages = len(player.session.config['app_sequence'])
            return {player.id_in_group: {'quit_status': 'success'}}

    @staticmethod
    def is_displayed(player):
        return not (player.participant.vars.get('finished', False) or player.participant.vars.get('quit', False))


page_sequence = [VerificationTask, Results]