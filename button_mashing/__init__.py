from otree.api import *
import time

class Constants(BaseConstants):
    name_in_url = 'button_mashing'
    players_per_group = None
    num_rounds = 1
    time_limit_seconds = 30  # Time limit for task
    target_clicks = 151  # Number of required clicks

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    button_press_count = models.IntegerField(initial=0)
    completion_time = models.IntegerField(initial=0)
    quit_early = models.BooleanField(initial=False)  # ✅ Track quitting
    start_time = models.FloatField(initial=0)  # ✅ Track start time

class ButtonMashingTask(Page):
    template_name = 'button_mashing/MyPage.html'
    form_model = 'player'
    form_fields = ['button_press_count', 'completion_time']

    @staticmethod
    def is_displayed(player):
        return not player.participant.vars.get('finished', False)  # ✅ Skip if quit

    @staticmethod
    def vars_for_template(player):
        return {
            'time_limit_seconds': Constants.time_limit_seconds,
            'target_clicks': Constants.target_clicks
        }

    @staticmethod
    def before_next_page(player, timeout_happened):
        if player.participant.vars.get('quit', False):  # ✅ Check quit before anything else
            player.participant.vars['finished'] = True  # ✅ Ensure future tasks recognize quitting

            try:
                end_index = player.session.config['app_sequence'].index('End')
                player.participant._index_in_pages = end_index  # ✅ Move directly to "End"
            except ValueError:
                player.participant._index_in_pages = len(player.session.config['app_sequence'])  # 🚀 Fallback

            return  # ✅ Prevent further execution

    @staticmethod
    def live_method(player, data):
        if data.get('action') == 'quit':  # ✅ Quit button clicked
            player.participant.vars['quit'] = True
            player.participant.vars['finished'] = True
            player.quit_early = True

            try:
                end_index = player.session.config['app_sequence'].index('End')
                player.participant._index_in_pages = end_index  # ✅ Move directly to "End"
            except ValueError:
                player.participant._index_in_pages = len(player.session.config['app_sequence'])  # 🚀 Fallback

            return {player.id_in_group: {'quit_status': 'success'}}  # ✅ Notify front-end

        if data['type'] == 'button_press':  # ✅ Handle button presses
            if player.button_press_count == 0:  # ✅ Capture start time on first click
                player.start_time = time.time()

            player.button_press_count += 1

            if player.button_press_count >= Constants.target_clicks:  # ✅ Auto-end if clicks reached
                player.completion_time = int(time.time() - player.start_time)  # ✅ Calculate actual completion time
                player.participant._index_in_pages += 1  # ✅ Move to next page
                return {0: {'button_press_count': player.button_press_count, 'task_complete': True}}

            return {0: {'button_press_count': player.button_press_count}}

class Results(Page):
    @staticmethod
    def vars_for_template(player):
        return {
            'button_press_count': player.button_press_count,
            'completion_time': player.completion_time,
            'show_quit_option': player.session.config.get('quit_option', False)  # ✅ Prevents error
        }

    @staticmethod
    def before_next_page(player, timeout_happened):
        if player.participant.vars.get('quit', False):
            player.participant.vars['finished'] = True  # ✅ Ensure quitting is recognized everywhere

            try:
                end_index = player.session.config['app_sequence'].index('End')
                player.participant._index_in_pages = end_index  # ✅ Move directly to "End"
            except ValueError:
                player.participant._index_in_pages = len(player.session.config['app_sequence'])  # 🚀 Fallback

            return  # ✅ Prevent further execution

    @staticmethod
    def live_method(player, data):
        if data.get('action') == 'quit':  # ✅ Quit button clicked
            player.participant.vars['quit'] = True
            player.participant.vars['finished'] = True
            player.quit_early = True

            try:
                end_index = player.session.config['app_sequence'].index('End')
                player.participant._index_in_pages = end_index  # ✅ Move directly to "End"
            except ValueError:
                player.participant._index_in_pages = len(player.session.config['app_sequence'])  # 🚀 Fallback

            return {player.id_in_group: {'quit_status': 'success'}}  # ✅ Notify front-end

    @staticmethod
    def is_displayed(player):
        return not (player.participant.vars.get('finished', False) or player.participant.vars.get('quit', False))
        # ✅ Ensures quitting works properly.

page_sequence = [ButtonMashingTask, Results]