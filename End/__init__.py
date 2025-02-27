# end/__init__.py
from otree.api import *

class Constants(BaseConstants):
    name_in_url = 'end'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    pass

class End(Page):
    @staticmethod
    def vars_for_template(player):
        return {
            "quit_early": player.participant.vars.get('quit', False)
        }

page_sequence = [End]