from otree.api import *

class Constants(BaseConstants):
    name_in_url = 'colorsorting_task'
    players_per_group = None
    num_rounds = 1
    timeout_seconds = 120
    colors = ['∷∷∷', '⋮⋮⋮', '⋯⋯⋯', '⋰⋰⋰', '⋱⋱⋱', '|||', '///', '---', '⊞⊞⊞', '◠◠◠']  # More patterns = longer task

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    sorted_colors = models.StringField(blank=True)
    correct_count = models.IntegerField(initial=0)
    completion_time = models.IntegerField(initial=0)
    quit_early = models.BooleanField(initial=False)

class ColorSortingTask(Page):
    form_model = 'player'
    form_fields = ['sorted_colors', 'completion_time']
    timeout_seconds = Constants.timeout_seconds  # Add this line

    @staticmethod
    def is_displayed(player):
        return not player.participant.vars.get('finished', False)

    @staticmethod
    def before_next_page(player, timeout_happened):
        if timeout_happened:
            player.completion_time = Constants.timeout_seconds
            print(f"Timeout happened, set completion_time to: {player.completion_time}")

        # ✅ Fallback for missing/zero completion_time
        if player.completion_time in [None, 0]:
            import time
            now = int(time.time())
            start_time = player.participant.vars.get('task_start_time')
            if start_time:
                player.completion_time = now - start_time
                print(f"Fallback: computed completion_time as {player.completion_time} seconds")
            else:
                player.completion_time = -1
                print("Fallback failed: no start_time found, set completion_time to -1")

        if player.participant.vars.get('quit', False):
            try:
                end_index = player.session.config['app_sequence'].index('End')
                player.participant._index_in_pages = end_index
            except ValueError:
                player.participant._index_in_pages = len(player.session.config['app_sequence'])
            player.participant.vars['finished'] = True
            raise StopIteration

        # Count correct matches
        import json
        try:
            sorted_colors = json.loads(player.sorted_colors)
            player.correct_count = sum(
                1 for item in sorted_colors
                if item['color'] == item['targetArea']
            )
        except (json.JSONDecodeError, KeyError):
            player.correct_count = 0

    @staticmethod
    def vars_for_template(player):
        import random, time
        if 'task_start_time' not in player.participant.vars:
            player.participant.vars['task_start_time'] = int(time.time())
        return {
            "shuffled_colors": random.sample(Constants.colors * 4, len(Constants.colors) * 4),
            "unique_colors": Constants.colors,
            "timeout_seconds": Constants.timeout_seconds,
        }

class Results(Page):
    @staticmethod
    def vars_for_template(player):
        return {
            "correct_count": player.correct_count,
            "total_blocks": len(Constants.colors) * 4,
            "completion_time": player.completion_time,
            "show_quit_option": player.session.config.get('quit_option', False)  # ✅ Prevents error
        }

    @staticmethod
    def live_method(player, data):
        if data.get('action') == 'quit':
            player.participant.vars['quit'] = True
            player.participant.vars['finished'] = True  # ✅ Ensures quitting is recognized everywhere
            player.quit_early = True  # ✅ Mark player as quitting

            try:
                end_index = player.session.config['app_sequence'].index('End')  # 🚀 Locate "End"
                player.participant._index_in_pages = end_index  # ✅ Move directly to "End"
            except ValueError:
                player.participant._index_in_pages = len(player.session.config['app_sequence'])  # 🚀 Fallback

            return {player.id_in_group: {'quit_status': 'success'}}  # ✅ Tell front-end the player quit

    @staticmethod
    def is_displayed(player):
        return not (player.participant.vars.get('finished', False) or player.participant.vars.get('quit', False))
        # ✅ Skips if the player has quit at ANY point.

page_sequence = [ColorSortingTask, Results]