from os import environ

SESSION_CONFIGS = [
    dict(
        name='control',
        display_name='OCTAGON - Control',
        num_demo_participants=1,
        quit_option=False,
        informed_early=False,
        app_sequence=[
            'welcome',
            #'button_mashing',
            'demographics',
            'GridCount_task',
            'numbertype_task',
            'trivia_task',
            'encryption_task',
            'ImageID_task',
            'button_mashing',
            'colorsorting_task',
            'slider_task',
            'End',  # 🚀 Make sure "End" is the last app
        ]
    ),
    dict(
        name='treatment1',
        display_name='OCTAGON - Early Quit Info',
        num_demo_participants=1,
        quit_option=True,  # This should be True
        informed_early=True,
        app_sequence=[
            'welcome',
            'demographics',
            'GridCount_task',
            'numbertype_task',
            'trivia_task',
            'encryption_task',
            'ImageID_task',
            'button_mashing',
            'colorsorting_task',
            'slider_task',
            'End',  # 🚀 Must be the last page
        ]
    ),
    dict(
        name='treatment2',
        display_name='OCTAGON - Late Quit Info',
        num_demo_participants=1,
        quit_option=True,
        informed_early=False,
        app_sequence=[
            'welcome',
            'demographics',
            'GridCount_task',
            'numbertype_task',
            'trivia_task',
            'encryption_task',
            'ImageID_task',
            'button_mashing',
            'colorsorting_task',
            'slider_task',
            'End',  # 🚀 Must be the last page
        ]
    )
]


# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# Debug settings
DEBUG = False
PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    dict(
        name='Octagon_Control',
        display_name='The Octagon Games - Control',
    ),
    dict(
        name='Octagon_EarlyQuit',
        display_name='The Octagon Games - Early Quit',
    ),
    dict(
        name='Octagon_LateQuit',
        display_name='The Octagon Games - Late Quit',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '8509881957774'

INSTALLED_APPS = ['otree']
