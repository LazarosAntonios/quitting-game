from otree.api import *

class Constants(BaseConstants):
    name_in_url = 'slider_task'
    players_per_group = None
    num_rounds = 1
    num_sliders = 48
    target_value = 48
    timeout_seconds = 120

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    correct_sliders = models.IntegerField(initial=0)
    completion_time = models.IntegerField(initial=0)
    quit_early = models.BooleanField(initial=False)

class SliderTask(Page):
    form_model = 'player'
    form_fields = ['correct_sliders', 'completion_time']
    timeout_seconds = Constants.timeout_seconds

    @staticmethod
    def is_displayed(player):
        # ✅ If the player quit, they should not see this task
        return not player.participant.vars.get('quit', False)

    @staticmethod
    def vars_for_template(player: Player):
        import random
        return {
            'num_sliders': Constants.num_sliders,
            'target_value': Constants.target_value,
            'random_positions': [random.randint(0, 100) for _ in range(Constants.num_sliders)],
            'timeout_seconds': Constants.timeout_seconds
        }

    @staticmethod
    def before_next_page(player, timeout_happened):
        # Add this line to handle timeout
        if timeout_happened:
            player.completion_time = Constants.timeout_seconds

        if player.participant.vars.get('quit', False):
            try:
                end_index = player.session.config['app_sequence'].index('End')  # 🚀 Locate "End"
                player.participant._index_in_pages = end_index  # ✅ Move directly to "End"
            except ValueError:
                player.participant._index_in_pages = len(player.session.config['app_sequence'])  # Fallback

            player.participant.vars['finished'] = True  # ✅ Ensures future pages recognize quitting
            raise StopIteration  # 🚀 **FORCE QUITTING IMMEDIATELY**

class Results(Page):
    @staticmethod
    def vars_for_template(player):
        return {
            'correct_sliders': player.correct_sliders,
            'total_sliders': Constants.num_sliders,
            'target_value': Constants.target_value,
            'completion_time': player.completion_time  # Add this line
        }

    @staticmethod
    def before_next_page(player, timeout_happened):
        # Add this line to handle timeout
        if timeout_happened:
            player.completion_time = Constants.timeout_seconds

        if player.participant.vars.get('quit', False):
            try:
                end_index = player.session.config['app_sequence'].index('End')  # 🚀 Locate "End"
                player.participant._index_in_pages = end_index  # ✅ Move directly to "End"
            except ValueError:
                player.participant._index_in_pages = len(player.session.config['app_sequence'])  # Fallback

            player.participant.vars['finished'] = True  # ✅ Ensures no further pages are shown
            raise StopIteration  # 🚀 **FORCE QUITTING IMMEDIATELY**

    @staticmethod
    def is_displayed(player):
        return not player.participant.vars.get('finished', False)  # ✅ Skips results if quit


page_sequence = [SliderTask, Results]