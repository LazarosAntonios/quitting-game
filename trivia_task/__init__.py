from otree.api import *


class Constants(BaseConstants):
    name_in_url = 'trivia_task'
    players_per_group = None
    num_rounds = 1
    time_limit_seconds = 8 * 60  # 8 minutes
    questions = [
        {
            "question": "Which country has the longest coastline in the world?",
            "choices": ["Canada", "USA", "Australia", "Iceland"],
            "correct": "Canada"
        },
        {
            "question": "Which of these cities is further north? Nagasaki or Hiroshima?",
            "choices": ["Nagasaki", "Hiroshima"],
            "correct": "Hiroshima",  # Hiroshima: 34.3853° N, Nagasaki: 32.7503° N
        },
        {
            "question": "Looking at a standard keyboard, are there more keys in the top row (numbers row) or bottom row (including spacebar)?",
            "choices": ["Top row", "Bottom row"],
            "correct": "Bottom row"  # Requires counting and comparison
        },
        {
            "question": "Starting at the Eiffel Tower, if you traveled to the Taj Mahal, then to the Great Wall of China, then back to the Eiffel Tower, in which country would you spend the most time crossing (by straight-line distance)?",
            "choices": ["India", "China", "Russia", "Mongolia"],
            "correct": "China"
        },
        {
            "question": "If light takes 8 minutes to travel from the Sun to Earth, and Mars is currently 1.5 times Earth's distance from the Sun, how many minutes would light take to reach Mars from the Sun?",
            "choices": ["10 minutes", "12 minutes", "14 minutes", "16 minutes"],
            "correct": "12 minutes"
        },
        {
            "question": "In the sentence 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG', how many letters appear the exact same number of times as their position in the alphabet? (A=1, B=2, etc.)",
            "choices": ["2", "3", "4", "5"],
            "correct": "3" # F appears 1 time (6th letter), L appears 12 times (12th letter), T appears 20 times (20th letter)
        },
        {
            "question": "Which country has won the most FIFA World Cup titles?",
            "choices": ["Brazil", "Argentina", "France", "Germany"],
            "correct": "Brazil"
        },
        {
            "question": "On an analog clock, how many times between 3:00 and 4:00 do the minute and hour hands form exactly a right angle?",
            "choices": ["1", "2", "3", "4"],
            "correct": "3"
        },
        {
            "question": "Starting facing North, you turn right, then left, then right twice, then left. Which direction are you facing?",
            "choices": ["North", "South", "East", "West"],
            "correct": "East"
        },
        {
            "question": "Among these European capital cities: Madrid, Rome, Athens, and Lisbon, which one is closest to being the exact geographic center of the group?",
            "choices": ["Madrid", "Rome", "Athens", "Lisbon"],
            "correct": "Rome"
        },
        {
            "question": "If you could rotate Italy (the 'boot'), would it fit entirely within Ukraine's borders without overlapping?",
            "choices": ["Yes", "No"],
            "correct": "Yes"  # Italy: 301,340 km² vs Ukraine: 603,550 km², and shape allows fitting
        },
        {
            "question": "Looking at China's population distribution: If you split China into East and West halves, approximately what percentage of the total population lives in the Eastern half?",
            "choices": ["55-60%", "65-70%", "75-80%", "85-90%"],
            "correct": "85-90%"
        }
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    answers_json = models.StringField(blank=True)
    answers = models.LongStringField(blank=True)
    correct_answers = models.IntegerField(initial=0)


class TriviaTask(Page):
    form_model = 'player'
    form_fields = ['answers_json']
    timeout_seconds = Constants.time_limit_seconds

    @staticmethod
    def vars_for_template(player: Player):
        import random
        return {
            'questions': random.sample(Constants.questions, len(Constants.questions)),
        }

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import json
        player.answers = player.answers_json

        try:
            # Parse the answers from JSON
            if player.answers_json:
                answers_dict = json.loads(player.answers_json)
                correct_count = 0

                # Check each answer
                for question in Constants.questions:
                    question_text = question['question']
                    if question_text in answers_dict:
                        user_answer = answers_dict[question_text]
                        if user_answer == question['correct']:
                            correct_count += 1

                player.correct_answers = correct_count
            else:
                player.correct_answers = 0
        except (json.JSONDecodeError, KeyError):
            player.correct_answers = 0


class TriviaResults(Page):
    template_name = 'trivia_task/Trivia_Results.html'  # Add this line

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'correct_answers': player.correct_answers,
            'total_questions': len(Constants.questions)
        }


page_sequence = [TriviaTask, TriviaResults]