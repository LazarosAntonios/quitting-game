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
        # Set completion time for timeout
        if timeout_happened:
            player.completion_time = Constants.timeout_seconds

        # Print debugging information
        print(f"Raw answers: '{player.answers}'")

        if player.answers:
            try:
                answers = player.answers.split(',')
                print(f"Split answers: {answers}")

                # Debug each word's expected encryption
                for i, word in enumerate(Constants.words):
                    expected = encrypt_word(word)
                    print(f"Word {i + 1}: {word} -> Expected: '{expected}'")

                # Compare each answer with its expected solution
                correct = 0
                for i, word in enumerate(Constants.words):
                    if i < len(answers):
                        expected = encrypt_word(word)
                        actual = answers[i].strip()
                        is_match = actual == expected
                        print(
                            f"Comparing answer {i + 1}: Expected '{expected}' vs Actual '{actual}' -> Match: {is_match}")
                        if is_match:
                            correct += 1

                print(f"Final correct count: {correct}")
                player.correct_count = correct
            except Exception as e:
                print(f"Error in processing: {e}")
                player.correct_count = 0
        else:
            print("No answers received")
            player.correct_count = 0

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