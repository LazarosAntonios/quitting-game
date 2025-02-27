from otree.api import *

class Constants(BaseConstants):
    name_in_url = 'encryption_task'
    players_per_group = None
    num_rounds = 1
    timeout_seconds = 180  # 3 minutes
    words = ['HELLO', 'WORLD', 'FLOWER', 'BRIGHT', 'SIMPLE', 'TASK', 'COMPLEX', 'SEE', 'ENCRYPTION', 'TALK']

def encrypt_word(word):
    return ''.join(str(ord(c) - ord('A') + 1).zfill(2) for c in word)

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    answers = models.StringField()
    correct_count = models.IntegerField(initial=0)
    completion_time = models.IntegerField()
    quit_early = models.BooleanField(initial=False)  # Add this field to track quitting

class EncryptionTask(Page):
    form_model = 'player'
    form_fields = ['answers', 'completion_time']
    timeout_seconds = Constants.timeout_seconds

    @staticmethod
    def vars_for_template(player):
        words_with_solution = [(word, encrypt_word(word)) for word in Constants.words]
        return {
            'words': words_with_solution,
            'timeout_seconds': Constants.timeout_seconds
        }

    @staticmethod
    def before_next_page(player, timeout_happened):
        if player.answers:
            answers = player.answers.split(',')
            correct_count = sum(1 for ans, (_, solution) in
                              zip(answers, [(w, encrypt_word(w)) for w in Constants.words])
                              if ans.strip() == solution)
            player.correct_count = correct_count


class Results(Page):
    @staticmethod
    def vars_for_template(player):
        return {
            'correct_count': player.correct_count,
            'total_words': len(Constants.words),
            'completion_time': player.completion_time,
            'show_quit_option': player.session.config.get('quit_option', False)  # ✅ Prevents KeyError
        }

    @staticmethod
    def before_next_page(player, timeout_happened):
        if player.participant.vars.get('quit', False):
            try:
                end_index = player.session.config['app_sequence'].index('End')  # 🚀 Locate "End" in app sequence
                player.participant._index_in_pages = end_index  # ✅ Move directly to "End"
            except ValueError:
                player.participant._index_in_pages = len(player.session.config['app_sequence'])  # Fallback
            player.participant.vars['finished'] = True  # ✅ Ensures future pages recognize quitting
            return  # 🚀 Ensures no further processing

    @staticmethod
    def live_method(player, data):
        if data.get('action') == 'quit':
            player.participant.vars['quit'] = True
            player.quit_early = True
            try:
                end_index = player.session.config['app_sequence'].index('End')  # 🚀 Locate "End" in app sequence
                player.participant._index_in_pages = end_index  # ✅ Move directly to "End"
            except ValueError:
                player.participant._index_in_pages = len(player.session.config['app_sequence'])  # Fallback
            return {player.id_in_group: {'quit_status': 'success'}}

    @staticmethod
    def is_displayed(player):
        return not (player.participant.vars.get('finished', False) or player.participant.vars.get('quit', False))
        # ✅ Skips if the player has quit at ANY point.

page_sequence = [EncryptionTask, Results]