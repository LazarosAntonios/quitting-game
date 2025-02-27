# welcome/__init__.py
from otree.api import *

class Constants(BaseConstants):
   name_in_url = 'welcome'
   players_per_group = None
   num_rounds = 1

class Subsession(BaseSubsession):
   pass

class Group(BaseGroup):
   pass

class Player(BasePlayer):
   pass

class Welcome(Page):
   @staticmethod
   def vars_for_template(player):
       return {
           'show_quit_info': player.session.config['quit_option'] and 
                            player.session.config['informed_early']
       }

page_sequence = [Welcome]