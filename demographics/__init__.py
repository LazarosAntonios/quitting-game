# demographics/__init__.py
from otree.api import *


class Constants(BaseConstants):
    name_in_url = 'demographics'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Basic Demographics
    age = models.IntegerField(
        label='What is your age?',
        min=18, max=100
    )

    gender = models.StringField(
        label='What is your gender?',
        choices=[
            [1, 'Male'],
            [2, 'Female'],
            [3, 'Prefer not to say']
        ]
    )

    education = models.StringField(
        label='What is your highest level of education?',
        choices=[
            [1, 'Less than high school'],
            [2, 'High school graduate'],
            [3, 'Some college'],
            [4, 'Bachelor degree'],
            [5, 'Master degree'],
            [6, 'Professional degree'],
            [7, 'Doctorate']
        ]
    )

    employment = models.StringField(
        label='What is your current employment status?',
        choices=[
            [1, 'Full-time employed'],
            [2, 'Part-time employed'],
            [3, 'Self-employed'],
            [4, 'Student'],
            [5, 'Retired'],
            [6, 'Unemployed'],
            [7, 'Other']
        ]
    )

    income = models.StringField(
        label='What is your annual household income?',
        choices=[
            [1, 'Less than £20,000'],
            [2, '£20,000 - £34,999'],
            [3, '£35,000 - £49,999'],
            [4, '£50,000 - £74,999'],
            [5, '£75,000 - £99,999'],
            [6, '£100,000 or more'],
            [7, 'Prefer not to say']
        ]
    )

    english_native = models.BooleanField(
        label='Is English your native language?',
        choices=[[True, 'Yes'], [False, 'No']]
    )

    # Payment information fields
    payment_method = models.StringField(
        label='Please select your preferred payment method:',
        choices=[
            ['PayPal', 'PayPal Email'],
            ['Revolut', 'Revolut Account'],
            ['Monzo', 'Monzo Account'],
            ['Bank', 'UK Bank Account']
        ]
    )

    payment_details = models.StringField(
        label='Please provide the details for your selected payment method:',
        blank=True
    )

    # Bank account specific fields
    bank_account_number = models.StringField(
        label='Account Number (8 digits):',
        blank=True
    )
    bank_sort_code = models.StringField(
        label='Sort Code (6 digits):',
        blank=True
    )
    bank_account_name = models.StringField(
        label='Account Holder Name:',
        blank=True
    )

    # Optional: Research-specific questions
    prior_experiments = models.IntegerField(
        label='How many economic experiments have you participated in before?',
        min=0
    )

    attitude = models.IntegerField(
        label='When facing challenges or setbacks, do you generally prefer to persist and push through, or do you sometimes decide to step away and move on? There’s no right or wrong answer—just interested in how people approach different situations.',
        choices=[
            [1, 'Always push through'],
            [2, 'Sometimes push through'],
            [3, 'Sometimes step away and move on'],
            [4, 'Always step away and move on'],
        ]
    )


class Demographics(Page):
    form_model = 'player'
    form_fields = [
        'age',
        'gender',
        'education',
        'employment',
        'income',
        'english_native',
        'prior_experiments',
        'payment_method',
        'payment_details',
        'bank_account_number',
        'bank_sort_code',
        'bank_account_name',
        'attitude'
    ]


page_sequence = [Demographics]