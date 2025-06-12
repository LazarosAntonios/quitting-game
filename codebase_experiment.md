# _rooms\econ101.txt

```txt
Alice
Bob
Charlie
```

# _rooms\octagon.txt

```txt

```

# _static\global\empty.css

```css

```

# _static\imageid_task\apple.png

This is a binary file of the type: Image

# _static\imageid_task\Band.png

This is a binary file of the type: Image

# _static\imageid_task\book.png

This is a binary file of the type: Image

# _static\imageid_task\car_new.png

This is a binary file of the type: Image

# _static\imageid_task\car.png

This is a binary file of the type: Image

# _static\imageid_task\Car2.png

This is a binary file of the type: Image

# _static\imageid_task\chair.png

This is a binary file of the type: Image

# _static\imageid_task\dog.png

This is a binary file of the type: Image

# _static\imageid_task\eagle.png

This is a binary file of the type: Image

# _static\imageid_task\food.png

This is a binary file of the type: Image

# _static\imageid_task\game.png

This is a binary file of the type: Image

# _static\imageid_task\house.png

This is a binary file of the type: Image

# _static\imageid_task\mountain.png

This is a binary file of the type: Image

# _static\imageid_task\movie.png

This is a binary file of the type: Image

# _static\imageid_task\pencil.png

This is a binary file of the type: Image

# _static\imageid_task\phone.png

This is a binary file of the type: Image

# _static\imageid_task\sport.png

This is a binary file of the type: Image

# _static\imageid_task\Stadium.png

This is a binary file of the type: Image

# _static\imageid_task\tree.png

This is a binary file of the type: Image

# _static\imageid_task\trophy.png

This is a binary file of the type: Image

# _static\imageid_task\Wonder.png

This is a binary file of the type: Image

# _templates\global\Page.html

```html
{{ extends "otree/Page.html" }}
{{ load otree }}

{{ block global_styles  }}
{{ endblock }}
{{ block global_scripts  }}
{{ endblock }}

```

# .gitignore

```
venv
staticfiles
./db.sqlite3
.idea
*~
*.sqlite3
_static_root
_bots*s
__temp*
__pycache__/
*.py[cod]
.DS_Store
merge.ps1
*.otreezip
```

# button_mashing\__init__.py

```py
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
```

# button_mashing\MyPage.html

```html
{% extends "global/Page.html" %}
{% block app_styles %}
<style>
    .otree-timer {
        display: none;
    }
</style>
{% endblock %}
{% block title %}{% endblock %}

{% block content %}
<div class="card">
    <div class="card-body">
        <!-- Instructions Section -->
        <div class="instructions-section mb-4">
            <h3 class="text-center mb-3">Button Mashing Challenge</h3>
            <div class="alert alert-info">
                <h5>Instructions:</h5>
                <ul class="mb-0">
                    <li>The timer starts <strong>AFTER</strong> your first click</li>
                    <li>You have <strong>30 seconds</strong> to click the button <strong>EXACTLY</strong> 151 times.</li>
                    <li>Your objective is to get as close as possible to exactly 151 clicks</li>
                    <li>Your ranking will be determined by how close your final click count is to 151</li>
                    <li>The closer you get to 151 clicks compared to other participants, the higher your ranking</li>
                    <li>Try to be as precise as possible with your clicks!</li>
                    <li>🏆 Remember: This is a competition! The top 10% of performers will receive an additional £0.50</li>
                    <li>🎲 In case of ties (where multiple participants achieve the same score), rankings will be determined randomly among those tied</li>
                </ul>
            </div>
        </div>

        <!-- Game Statistics Display -->
        <div class="game-container text-center">
            <div class="stats-container mb-4">
                <div class="stat-box">
                    <span class="stat-label">Time Remaining:</span>
                    <span class="stat-value" id="time-remaining">30</span>
                    <span class="stat-unit">seconds</span>
                </div>
                <div class="stat-box">
                    <span class="stat-label">Clicks:</span>
                    <span class="stat-value" id="press-count">0</span>
                </div>
            </div>

            <button id="mash-button" type="button" class="click-button">
                CLICK ME!
            </button>
        </div>

        <form id="game-form" method="post" style="display: none;">
            <input type="hidden" name="button_press_count" id="final-count">
            <input type="hidden" name="completion_time" id="final-time">
        </form>
    </div>
</div>

<style>
    .card {
        max-width: 800px;
        margin: 0 auto;
        border: none;
        box-shadow: 0 0 20px rgba(0,0,0,0.1);
    }

    .alert-info {
        background-color: #f8f9fa;
        border-left: 4px solid #3498db;
        border-radius: 0;
    }

    .alert-info ul {
        list-style-type: none;
        padding-left: 0;
    }

    .alert-info li {
        margin-bottom: 8px;
        position: relative;
        padding-left: 20px;
    }

    .alert-info li:before {
        content: "•";
        color: #3498db;
        position: absolute;
        left: 0;
    }

    .stats-container {
        display: flex;
        justify-content: center;
        gap: 40px;
        flex-wrap: wrap;
    }

    .stat-box {
        background: #f8f9fa;
        padding: 15px 25px;
        border-radius: 10px;
        min-width: 150px;
    }

    .stat-label {
        font-size: 0.9em;
        color: #666;
        display: block;
        margin-bottom: 5px;
    }

    .stat-value {
        font-size: 1.8em;
        font-weight: bold;
        color: #2c3e50;
        display: block;
    }

    .stat-unit {
        font-size: 0.9em;
        color: #666;
    }

    .click-button {
        padding: 30px 60px;
        font-size: 1.5em;
        font-weight: bold;
        color: white;
        background-color: #3498db;
        border: none;
        border-radius: 15px;
        cursor: pointer;
        transition: all 0.1s ease;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }

    .click-button:hover {
        background-color: #2980b9;
        transform: scale(1.02);
    }

    .click-button:active {
        transform: scale(0.98);
    }

    .click-button:disabled {
        background-color: #bdc3c7;
        cursor: not-allowed;
        transform: none;
    }

    .click-button.success {
        background-color: #27ae60;
    }

    .click-button.failure {
        background-color: #e74c3c;
    }
</style>

<script>
    let pressCount = 0;
    let timerStarted = false;
    const timeLimit = 30;
    let timeRemaining = timeLimit;
    let startTime;
    let timerInterval;

    const button = document.getElementById("mash-button");
    const pressCountDisplay = document.getElementById("press-count");
    const timeRemainingDisplay = document.getElementById("time-remaining");

    button.addEventListener("click", (event) => {
    event.preventDefault();

    if (!timerStarted) {
        timerStarted = true;
        startTime = Date.now();
        startTimer();
    }

    pressCount++;
    pressCountDisplay.textContent = pressCount;
    liveSend({ type: "button_press" });

    if (pressCount >= 151) {  // ✅ If 151 clicks reached
        clearInterval(timerInterval);  // ✅ Stop timer
        button.disabled = true;  // ✅ Disable button
        button.textContent = "Task Completed!";  // ✅ Update UI

        // ✅ Store time spent
        const actualTime = timeLimit - timeRemaining;

        // ✅ Auto-submit form
        const form = document.createElement('form');
        form.method = 'post';

        const countInput = document.createElement('input');
        countInput.type = 'hidden';
        countInput.name = 'button_press_count';
        countInput.value = pressCount;
        form.appendChild(countInput);

        const timeInput = document.createElement('input');
        timeInput.type = 'hidden';
        timeInput.name = 'completion_time';
        timeInput.value = actualTime;
        form.appendChild(timeInput);

        document.body.appendChild(form);
        form.submit();
    }
});

    function startTimer() {
    timerInterval = setInterval(() => {
        timeRemaining--;
        timeRemainingDisplay.textContent = timeRemaining;

        if (timeRemaining <= 0) {
            clearInterval(timerInterval);
            button.disabled = true;
            button.textContent = "Time's Up!";

            // Calculate actual time spent
            const actualTime = 30 - timeRemaining;  // This gives actual seconds spent

            const form = document.createElement('form');
            form.method = 'post';

            const countInput = document.createElement('input');
            countInput.type = 'hidden';
            countInput.name = 'button_press_count';
            countInput.value = pressCount;
            form.appendChild(countInput);

            const timeInput = document.createElement('input');
            timeInput.type = 'hidden';
            timeInput.name = 'completion_time';
            timeInput.value = actualTime;  // Use actual time instead of total time
            form.appendChild(timeInput);

            document.body.appendChild(form);
            form.submit();
        }
    }, 1000);
}
</script>
{% endblock %}
```

# button_mashing\Results.html

```html
{% extends "global/Page.html" %}
{% block title %}Button Mashing Challenge - Results{% endblock %}

{% block content %}
<div class="card">
    <div class="card-body text-center">
        <!-- Title -->
        <h3 class="mb-4">Challenge Complete!</h3>

        <!-- Performance Summary -->
        <div class="result-box">
            <div class="result-label">Performance Summary</div>
            <div class="result-value">
                {{ button_press_count }} clicks
            </div>
            <div class="completion-time">
                Time taken: {{ completion_time }} seconds
            </div>
        </div>

        <!-- Quit Option -->
        {% if show_quit_option %}
        <div class="quit-section mt-4">
            <div class="quit-container">
                <div class="quit-header">
                    <h4>⚠️ <span class="quit-title">IMPORTANT: EXIT OPTION AVAILABLE</span> ⚠️</h4>
                </div>
                <div class="quit-content">
                    <p>You now have the option to <strong>exit this study</strong>.</p>
                    <p>If you choose to exit now:</p>
                    <ul>
                        <li>You will still receive £2 for your participation in this study</li>
                        <li>You will be eligible for performance bonuses for all the tasks where you have scored in the top 10%</li>
                        <li>You will not need to complete any remaining tasks</li>
                    </ul>
                    <div class="quit-action">
                        <button id="quit-button" class="btn btn-warning btn-lg">EXIT THE STUDY NOW</button>
                        <p class="continue-note">To continue with the study, simply click the "Next" button below</p>
                    </div>
                </div>
            </div>
        </div>

        <style>
            .quit-container {
                background-color: #fff8e1;
                border: 3px solid #ff9800;
                border-radius: 10px;
                padding: 20px;
                margin: 30px 0;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            }

            .quit-header {
                background-color: #ff9800;
                margin: -20px -20px 15px -20px;
                padding: 10px;
                text-align: center;
                border-radius: 7px 7px 0 0;
            }

            .quit-title {
                color: white;
                font-weight: bold;
                font-size: 1.2em;
            }

            .quit-content {
                padding: 0 10px;
            }

            .quit-content p, .quit-content ul {
                font-size: 1.1em;
            }

            .quit-action {
                text-align: center;
                margin-top: 20px;
                padding-top: 15px;
                border-top: 1px dashed #ff9800;
            }

            #quit-button {
                font-size: 1.2em;
                padding: 10px 25px;
                background-color: #ff5722;
                border-color: #ff5722;
            }

            #quit-button:hover {
                background-color: #e64a19;
                border-color: #e64a19;
                transform: scale(1.05);
            }

            .continue-note {
                margin-top: 15px;
                font-style: italic;
                color: #555;
            }
        </style>
        {% endif %}

        <!-- Continue Button -->
        <div class="mt-4">
            {% next_button %}
        </div>
    </div>
</div>

<!-- Quit Button Logic -->
{% if show_quit_option %}
<script>
    document.addEventListener('DOMContentLoaded', function() {
        const quitButton = document.getElementById('quit-button');
        if (quitButton) {
            quitButton.addEventListener('click', function() {
                liveSend({ action: 'quit' }).then(response => {
                    if (response[Object.keys(response)[0]].quit_status === 'success') {
                        window.location.reload();  // ✅ Reload to enforce quitting
                    }
                });
            });
        }
    });
</script>
{% endif %}

<!-- Styling -->
<style>
    .card {
        max-width: 600px;
        margin: 50px auto;
        border: none;
        box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
    }

    .result-box {
        background: #f8f9fa;
        padding: 30px;
        border-radius: 10px;
        margin: 20px 0;
    }

    .result-label {
        font-size: 1.2em;
        color: #666;
        margin-bottom: 10px;
    }

    .result-value {
        font-size: 3em;
        font-weight: bold;
        color: #2c3e50;
    }

    .completion-time {
        font-size: 1.2em;
        margin-top: 10px;
        color: #555;
    }

    .btn-primary {
        padding: 10px 30px;
        font-size: 1.1em;
    }
</style>
{% endblock %}
```

# colorsorting_task\__init__.py

```py
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
```

# colorsorting_task\ColorSortingTask.html

```html
{% extends "global/Page.html" %}
{% block app_styles %}
<style>
    .otree-timer {
        display: none;
    }
</style>
{% endblock %}
{% block title %}{% endblock %}

{% block content %}
<div class="card">
    <div class="card-body">
        <!-- Instructions Section -->
        <div class="instructions-section mb-4">
            <h3 class="text-center mb-3">Pattern Sorting Challenge</h3>
            <div class="alert alert-info">
                <h5>Instructions:</h5>
                <ul class="mb-0">
                    <li><strong>The timer has already started!</strong></li>
                    <li>You have <strong>2 minutes</strong> to sort as many blocks as possible</li>
                    <li>Sort the patterns in blocks by dragging them into their matching pattern zones</li>
                    <li>Your objective is to correctly sort <strong>as many blocks as possible</strong></li>
                    <li>The more blocks you correctly sort compared to other participants, the higher your ranking</li>
                    <li>Each block placed in its correct zone counts as one point</li>
                    <li>You can submit your answers at any time using the button below</li>
                    <li>🏆 Remember: This is a competition! The top 10% of performers will receive an additional £0.50</li>
                    <li>🎲 In case of ties (where multiple participants achieve the same score), rankings will be determined randomly among those tied</li>
                </ul>
            </div>
        </div>

        <!-- Timer -->
        <div class="timer-container text-center mb-4">
            <div class="stat-box">
                <span class="stat-label">Time Remaining:</span>
                <span class="stat-value" id="timer">2:00</span>
            </div>
        </div>

        <!-- Color Blocks Container -->
        <div class="color-blocks-section">
            <h5 class="section-title">Available Blocks</h5>
            <div id="color-container">
                {% for color in shuffled_colors %}
                <div class="color-block" draggable="true" data-color="{{ color }}">{{ color }}</div>
                {% endfor %}
            </div>
        </div>

        <!-- Sorting Areas -->
        <div class="sorting-section mt-4">
            <h5 class="section-title">Drop Zones</h5>
            <div id="sorting-areas">
                {% for color in unique_colors %}
                <div class="sorting-area" data-color="{{ color }}">
                    <h3>{{ color }}</h3>
                </div>
                {% endfor %}
            </div>
        </div>

        <form method="post" id="sorting-form" style="text-align: center;">
    <input type="hidden" name="sorted_colors" id="sorted_colors" value="[]">
    <input type="hidden" name="completion_time" id="completion_time" value="0">
    <div class="text-center mt-4">
        <button type="submit" class="btn btn-primary btn-lg">End Challenge & See Results</button>
    </div>
</form>
    </div>
</div>

<style>
    .card {
        max-width: 900px;
        margin: 0 auto;
        border: none;
        box-shadow: 0 0 20px rgba(0,0,0,0.1);
    }

    .alert-info {
        background-color: #f8f9fa;
        border-left: 4px solid #3498db;
        border-radius: 0;
    }

    .alert-info ul {
        list-style-type: none;
        padding-left: 0;
    }

    .alert-info li {
        margin-bottom: 8px;
        position: relative;
        padding-left: 20px;
    }

    .alert-info li:before {
        content: "•";
        color: #3498db;
        position: absolute;
        left: 0;
    }

    .timer-container {
        position: sticky;
        top: 0;
        background: white;
        padding: 10px;
        z-index: 100;
    }

    .stat-box {
        background: #f8f9fa;
        padding: 15px 25px;
        border-radius: 10px;
        display: inline-block;
    }

    .stat-value {
        font-size: 1.5em;
        font-weight: bold;
        color: #2c3e50;
        margin: 0 10px;
    }

    .section-title {
        color: #2c3e50;
        margin-bottom: 15px;
        padding-left: 10px;
        border-left: 4px solid #3498db;
    }

    #color-container {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        margin-bottom: 20px;
        padding: 15px;
        background: #f8f9fa;
        border-radius: 10px;
    }

    .color-block {
        width: 100px;
        height: 50px;
        text-align: center;
        line-height: 50px;
        border: none;
        border-radius: 8px;
        cursor: grab;
        color: white;
        text-shadow: 1px 1px 1px rgba(0,0,0,0.5);
        transition: transform 0.2s ease;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }

    .color-block:hover {
        transform: scale(1.05);
    }

    #sorting-areas {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
        gap: 20px;
        margin-top: 20px;
    }

    .sorting-area {
        min-height: 250px;
        border: 2px dashed #bdc3c7;
        border-radius: 10px;
        text-align: center;
        padding: 15px;
        transition: border-color 0.3s ease;
        background: #f8f9fa;
    }

    .sorting-area:hover {
        border-color: #3498db;
    }

    .btn-primary {
        background-color: #3498db;
        border: none;
        padding: 12px 30px;
        font-size: 1.1em;
        transition: all 0.3s ease;
    }

    .btn-primary:hover {
        background-color: #2980b9;
        transform: scale(1.05);
    }
</style>

<script>
    let draggedBlock = null;
    let timerStarted = true;  // ✅ Already started
    let timer;
    let startTime = new Date().getTime();  // ✅ Immediately

    startTimer({{ timeout_seconds }});  // ✅ Start countdown at page load


    const colorBlocks = document.querySelectorAll('.color-block');
    const sortingAreas = document.querySelectorAll('.sorting-area');
    const sortedColorsInput = document.getElementById('sorted_colors');
    const completionTimeInput = document.getElementById('completion_time');
    const timerDisplay = document.getElementById('timer');

    // Initialize sorted_colors with empty array
    sortedColorsInput.value = JSON.stringify([]);

    // Initially show full time
    timerDisplay.textContent = "2:00";

    colorBlocks.forEach(block => {
        block.addEventListener('dragstart', () => {
            draggedBlock = block;
            // Start timer on first drag
        });

        block.addEventListener('dragend', () => {
            draggedBlock = null;
        });
    });


    sortingAreas.forEach(area => {
        area.addEventListener('dragover', (e) => {
            e.preventDefault();
        });

        area.addEventListener('drop', (e) => {
            e.preventDefault();
            if (draggedBlock) {
                area.appendChild(draggedBlock);
                updateSortedColors();
            }
        });
    });

    function updateSortedColors() {
    const sortedColors = [];
    sortingAreas.forEach(area => {
        const blocks = area.querySelectorAll('.color-block');
        const targetArea = area.dataset.color;
        blocks.forEach(block => {
            sortedColors.push({
                color: block.dataset.color,
                targetArea: targetArea
            });
        });
    });
    // Convert to string and make sure to update the hidden input
    sortedColorsInput.value = JSON.stringify(sortedColors);

    // Log for debugging
    console.log('Sorted colors:', sortedColors);
}

// Update form submission to ensure colors are counted
document.getElementById('sorting-form').addEventListener('submit', (e) => {
    // Ensure the visual countdown timer is cleared if it's running
    if (timer) {
        clearInterval(timer);
    }

    const endTime = new Date().getTime();
    let timeSpent = 0;

    if (startTime && endTime > startTime) {
        timeSpent = Math.round((endTime - startTime) / 1000);
        if (timeSpent === 0) timeSpent = 1;
    }

    // Check if startTime is valid (it should be, as it's set on page load)
    // and if endTime is genuinely after startTime
    if (typeof startTime === 'number' && typeof endTime === 'number' && endTime > startTime) {
        timeSpent = Math.round((endTime - startTime) / 1000);

        // If timeSpent rounds to 0, but actual time passed (endTime > startTime),
        // set it to 1 second to reflect that some time was spent.
        // This handles cases where duration is < 0.5 seconds.
        if (timeSpent === 0 && endTime > startTime) {
            timeSpent = 1;
            console.log('Time spent was < 0.5s but > 0s, rounded up to 1s.');
        }
    } else if (typeof startTime === 'number' && typeof endTime === 'number' && endTime <= startTime) {
        // This case (end time before or exactly at start time) is unusual for page interaction.
        // Log it and keep timeSpent at 0 or handle as a specific case if needed.
        console.warn('Warning: endTime is less than or equal to startTime. Completion time set to 0 seconds.');
        timeSpent = 0;
    } else {
        // Handle cases where startTime or endTime might not be valid numbers (should not happen with new Date().getTime())
        console.error('Error: startTime or endTime is not a valid number. Completion time set to 0 seconds.');
        timeSpent = 0;
    }

    // Final check for NaN, though the above logic should prevent it.
    if (isNaN(timeSpent)) {
        console.error('Error: timeSpent calculated as NaN. Defaulting completion time to 0 seconds.');
        timeSpent = 0;
    }

    console.log('Form submitted! Calculated timeSpent:', timeSpent, 'seconds');

    // Explicitly set the value of the hidden input field
    document.getElementById('completion_time').value = timeSpent;
    console.log('Set hidden input completion_time to:', document.getElementById('completion_time').value);

    // Make sure to update sorted colors before submitting
    updateSortedColors();
});

    function startTimer(duration) {
        let timeLeft = duration;

        timer = setInterval(() => {
            const minutes = Math.floor(timeLeft / 60);
            const seconds = timeLeft % 60;

            timerDisplay.textContent = `${minutes}:${seconds.toString().padStart(2, '0')}`;

            if (--timeLeft < 0) {
                clearInterval(timer);

                // Make sure to update sorted colors before submitting
                updateSortedColors();

                // Set completion time to the full duration when timer expires
                completionTimeInput.value = {{ timeout_seconds }};

                // Force form submission
                document.getElementById('sorting-form').submit();
            }
        }, 1000);
    }
</script>
{% endblock %}
```

# colorsorting_task\Results.html

```html
{% extends "global/Page.html" %}
{% block title %}Pattern Sorting Challenge - Results{% endblock %}

{% block content %}
<div class="card">
    <div class="card-body text-center">
        <h3 class="mb-4">Challenge Complete!</h3>

        <div class="result-box">
            <div class="result-label">Your Performance</div>
            <div class="result-value">
                {{ correct_count }} out of {{ total_blocks }} blocks correctly sorted
            </div>
            <div class="result-details">
                Completed in {{ completion_time }} seconds
            </div>
        </div>

        <div class="mt-4">
            {% next_button %}
        </div>

        {% if show_quit_option %}
        <div class="quit-section mt-4">
            <div class="quit-container">
                <div class="quit-header">
                    <h4>⚠️ <span class="quit-title">IMPORTANT: EXIT OPTION AVAILABLE</span> ⚠️</h4>
                </div>
                <div class="quit-content">
                    <p>You now have the option to <strong>exit this study</strong>.</p>
                    <p>If you choose to exit now:</p>
                    <ul>
                        <li>You will still receive £2 for your participation in this study</li>
                        <li>You will be eligible for performance bonuses for all the tasks where you have scored in the top 10%</li>
                        <li>You will not need to complete any remaining tasks</li>
                    </ul>
                    <div class="quit-action">
                        <button id="quit-button" class="btn btn-warning btn-lg">EXIT THE STUDY NOW</button>
                        <p class="continue-note">To continue with the study, simply click the "Next" button below</p>
                    </div>
                </div>
            </div>
        </div>

        <style>
            .quit-container {
                background-color: #fff8e1;
                border: 3px solid #ff9800;
                border-radius: 10px;
                padding: 20px;
                margin: 30px 0;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            }

            .quit-header {
                background-color: #ff9800;
                margin: -20px -20px 15px -20px;
                padding: 10px;
                text-align: center;
                border-radius: 7px 7px 0 0;
            }

            .quit-title {
                color: white;
                font-weight: bold;
                font-size: 1.2em;
            }

            .quit-content {
                padding: 0 10px;
            }

            .quit-content p, .quit-content ul {
                font-size: 1.1em;
            }

            .quit-action {
                text-align: center;
                margin-top: 20px;
                padding-top: 15px;
                border-top: 1px dashed #ff9800;
            }

            #quit-button {
                font-size: 1.2em;
                padding: 10px 25px;
                background-color: #ff5722;
                border-color: #ff5722;
            }

            #quit-button:hover {
                background-color: #e64a19;
                border-color: #e64a19;
                transform: scale(1.05);
            }

            .continue-note {
                margin-top: 15px;
                font-style: italic;
                color: #555;
            }
        </style>

        <script>
            document.addEventListener('DOMContentLoaded', function() {
                const quitButton = document.getElementById('quit-button');
                if (quitButton) {
                    quitButton.addEventListener('click', function() {
                        liveSend({ action: 'quit' }).then(response => {
                            if (response[Object.keys(response)[0]].quit_status === 'success') {
                                window.location.href = "/End/";  // ✅ Redirect to End Page
                            }
                        });
                    });
                }
            });
        </script>
        {% endif %}
    </div>
</div>

<style>
    .card {
        max-width: 600px;
        margin: 50px auto;
        border: none;
        box-shadow: 0 0 20px rgba(0,0,0,0.1);
    }

    .result-box {
        background: #f8f9fa;
        padding: 30px;
        border-radius: 10px;
        margin: 20px 0;
    }

    .result-label {
        font-size: 1.2em;
        color: #666;
        margin-bottom: 10px;
    }

    .result-value {
        font-size: 3em;
        font-weight: bold;
        color: #2c3e50;
    }

    .result-details {
        margin-top: 15px;
        color: #666;
        font-size: 1.1em;
    }
</style>
{% endblock %}
```

# db.sqlite3

This is a binary file of the type: Binary

# demographics\__init__.py

```py
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
            ['Bank', 'UK Bank Account'],
            ['Donate', 'I wish to not receive payment and donate the amount instead']
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

    @staticmethod
    def error_message(player, values):
        # Make payment details required unless donating
        if values['payment_method'] != 'Donate':
            if values['payment_method'] == 'Bank':
                # Bank account details are required
                if not values['bank_account_number'] or not values['bank_sort_code'] or not values['bank_account_name']:
                    return 'Please fill in all bank account details'
            else:
                # Other payment methods require payment_details
                if not values['payment_details']:
                    return 'Please provide your payment details'


page_sequence = [Demographics]
```

# demographics\Demographics.html

```html
{% extends "global/Page.html" %}
{% block title %}{% endblock %}

{% block content %}
<div class="card">
    <div class="card-body">
        <div class="intro-message alert alert-info mb-4">
            <h4 class="text-center mb-3">Before We Begin...</h4>
            <p>We'll now ask you some general questions about yourself. Please try to be as precise as possible in your answers. Remember, there are no wrong answers - we're simply interested in learning more about our participants.</p>
        </div>

        <div class="mb-4">
            <h3 class="text-center">Participant Information</h3>
            <p class="text-muted text-center">Please answer the following questions about yourself. This information will be kept confidential and used only for research purposes.</p>
        </div>

        <form method="post">
            {% for field in form %}
                {% if field.name != "payment_method" and field.name != "payment_details" and field.name != "bank_account_number" and field.name != "bank_sort_code" and field.name != "bank_account_name" and field.name != "attitude" %}
                    <div class="form-group mb-4">
                        <label class="form-label">
                            {{ field.label }}
                        </label>

                        {% if field.name == "age" %}
                            <input type="number"
                                name="{{ field.name }}"
                                class="form-control"
                                min="18"
                                max="100"
                                required>
                        {% elif field.name == "prior_experiments" %}
                            <input type="number"
                                name="{{ field.name }}"
                                class="form-control"
                                min="0"
                                required>
                        {% else %}
                            <div class="form-control">
                                {{ field }}
                            </div>
                        {% endif %}

                        {% if field.errors %}
                            <div class="alert alert-danger mt-1">
                                {{ field.errors }}
                            </div>
                        {% endif %}
                    </div>
                {% endif %}
            {% endfor %}

            <!-- Payment Information Section -->
            <div class="payment-section mb-5">
                <h3 class="text-center mb-3">Payment Information</h3>
                <p class="text-muted text-center mb-4">Please select your preferred payment method and provide the relevant details so we can send your compensation after the experiment.</p>

                <div class="form-group mb-4">
                    <label class="form-label">
                        {{ form.payment_method.label }}
                    </label>
                    <div class="form-control">
                        {{ form.payment_method }}
                    </div>
                </div>

                <!-- Non-bank payment details -->
                <div id="general-payment-details" class="form-group mb-4">
                    <div id="paypal-info" class="payment-info">
                        <p class="text-muted mb-2">Please enter the PayPal email address where you'd like to receive payment.</p>
                    </div>
                    <div id="revolut-info" class="payment-info">
                        <p class="text-muted mb-2">Please enter the phone number or email associated with your Revolut account.</p>
                    </div>
                    <div id="monzo-info" class="payment-info">
                        <p class="text-muted mb-2">Please enter the phone number or email associated with your Monzo account.</p>
                    </div>

                    <div id="donate-info" class="payment-info">
                        <p class="text-muted mb-2">Thank you for choosing to donate your payment. The amount will be donated to charitable causes.</p>
                    </div>

                    <label class="form-label">
                        {{ form.payment_details.label }}
                    </label>
                    <div class="form-control">
                        {{ form.payment_details }}
                    </div>
                </div>

                <!-- Bank account specific fields -->
                <div id="bank-details" class="bank-fields" style="display: none;">
                    <div id="bank-info" class="payment-info">
                        <p class="text-muted mb-2">Please enter your UK bank account details below:</p>
                    </div>

                    <div class="form-group mb-3">
                        <label class="form-label">
                            {{ form.bank_account_number.label }}
                        </label>
                        <input type="text"
                               name="bank_account_number"
                               class="form-control"
                               maxlength="8"
                               placeholder="12345678"
                               pattern="[0-9]{8}"
                               id="bank_account_number_input">
                        <small class="form-text text-muted">Enter an 8-digit number with no spaces</small>
                    </div>

                    <div class="form-group mb-3">
                        <label class="form-label">
                            {{ form.bank_sort_code.label }}
                        </label>
                        <input type="text"
                               name="bank_sort_code"
                               class="form-control"
                               maxlength="8"
                               placeholder="12-34-56"
                               id="bank_sort_code_input">
                        <small class="form-text text-muted">Format: XX-XX-XX (e.g., 12-34-56)</small>
                    </div>

                    <div class="form-group mb-3">
                        <label class="form-label">
                            {{ form.bank_account_name.label }}
                        </label>
                        <input type="text"
                               name="bank_account_name"
                               class="form-control"
                               placeholder="John Smith"
                               id="bank_account_name_input">
                    </div>
                </div>
            </div>

            <!-- Attitude question -->
            <div class="form-group mb-4">
                <label class="form-label">
                    {{ form.attitude.label }}
                </label>
                <div class="form-control">
                    {{ form.attitude }}
                </div>
                {% if form.attitude.errors %}
                    <div class="alert alert-danger mt-1">
                        {{ form.attitude.errors }}
                    </div>
                {% endif %}
            </div>

            <div class="text-center mt-5">
                <button class="btn btn-primary btn-lg" type="submit">Continue</button>
            </div>
        </form>
    </div>
</div>

<style>
    .card {
        max-width: 800px;
        margin: 2rem auto;
        border: none;
        box-shadow: 0 0 20px rgba(0,0,0,0.1);
    }

    .intro-message {
        background-color: #f8f9fa;
        border-left: 4px solid #3498db;
        padding: 20px;
        border-radius: 8px;
    }

    .form-group label {
        font-weight: 500;
        color: #2c3e50;
        margin-bottom: 0.5rem;
    }

    .form-control {
        padding: 0.75rem;
        border: 1px solid #ddd;
        border-radius: 8px;
        width: 100%;
    }

    select.form-control {
        width: 100%;
        padding: 0.75rem;
    }

    .btn-primary {
        background-color: #3498db;
        border: none;
        padding: 1rem 2rem;
        font-size: 1.1rem;
        transition: all 0.3s ease;
    }

    .btn-primary:hover {
        background-color: #2980b9;
        transform: scale(1.05);
    }

    /* Style the select elements */
    select {
        width: 100%;
        padding: 0.75rem;
        border: 1px solid #ddd;
        border-radius: 8px;
        background-color: white;
    }

    /* Style radio buttons and checkboxes container */
    .form-check {
        margin: 0.5rem 0;
    }

    /* Add spacing between radio options */
    .form-check + .form-check {
        margin-top: 0.5rem;
    }

    /* Payment info styles */
    .payment-info {
        display: none;
        background-color: #f8f9fa;
        padding: 10px 15px;
        border-radius: 8px;
        margin-bottom: 10px;
    }

    .payment-section {
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 10px;
        border-left: 4px solid #3498db;
    }

    .form-text {
        font-size: 0.85rem;
        color: #6c757d;
        margin-top: 0.25rem;
    }
</style>

<script>
    // Script to show the appropriate helper text and fields based on payment method selection
    document.addEventListener('DOMContentLoaded', function() {
        const paymentMethodSelect = document.querySelector('select[name="payment_method"]');
        const paymentInfoDivs = document.querySelectorAll('.payment-info');
        const generalPaymentDetails = document.getElementById('general-payment-details');
        const bankDetails = document.getElementById('bank-details');

        // Format the sort code as user types (XX-XX-XX)
        const sortCodeInput = document.getElementById('bank_sort_code_input');
        sortCodeInput.addEventListener('input', function(e) {
            let value = e.target.value.replace(/[^\d]/g, ''); // Remove non-digits

            if (value.length > 6) {
                value = value.slice(0, 6); // Limit to 6 digits
            }

            // Add dashes automatically
            if (value.length > 4) {
                value = value.slice(0, 2) + '-' + value.slice(2, 4) + '-' + value.slice(4);
            } else if (value.length > 2) {
                value = value.slice(0, 2) + '-' + value.slice(2);
            }

            e.target.value = value;
        });

        // Format account number (ensure it's 8 digits)
        const accountNumberInput = document.getElementById('bank_account_number_input');
        accountNumberInput.addEventListener('input', function(e) {
            let value = e.target.value.replace(/[^\d]/g, ''); // Remove non-digits

            if (value.length > 8) {
                value = value.slice(0, 8); // Limit to 8 digits
            }

            e.target.value = value;
        });

        function updatePaymentInfo() {
            // Hide all payment info divs
            paymentInfoDivs.forEach(div => div.style.display = 'none');

            // Get selected payment method
            const selectedValue = paymentMethodSelect.value;

            // Show/hide appropriate sections
            if (selectedValue === 'Bank') {
                generalPaymentDetails.style.display = 'none';
                bankDetails.style.display = 'block';
                document.getElementById('bank-info').style.display = 'block';

                // Make bank fields required
                document.getElementById('bank_account_number_input').required = true;
                document.getElementById('bank_sort_code_input').required = true;
                document.getElementById('bank_account_name_input').required = true;
            } else if (selectedValue === 'Donate') {
                // Hide all payment detail fields for donation option
                generalPaymentDetails.style.display = 'none';
                bankDetails.style.display = 'none';

                // Make all fields not required
                document.getElementById('bank_account_number_input').required = false;
                document.getElementById('bank_sort_code_input').required = false;
                document.getElementById('bank_account_name_input').required = false;

                // Add this line to show the donation info message
                document.getElementById('donate-info').style.display = 'block';
            } else {
                generalPaymentDetails.style.display = 'block';
                bankDetails.style.display = 'none';

                // Make bank fields not required
                document.getElementById('bank_account_number_input').required = false;
                document.getElementById('bank_sort_code_input').required = false;
                document.getElementById('bank_account_name_input').required = false;

                // Show relevant info div
                if (selectedValue === 'PayPal') {
                    document.getElementById('paypal-info').style.display = 'block';
                } else if (selectedValue === 'Revolut') {
                    document.getElementById('revolut-info').style.display = 'block';
                } else if (selectedValue === 'Monzo') {
                    document.getElementById('monzo-info').style.display = 'block';
                }
            }
        }

        // Initial update
        updatePaymentInfo();

        // Update when selection changes
        paymentMethodSelect.addEventListener('change', updatePaymentInfo);
    });
</script>
{% endblock %}
```

# demographics\Results.html

```html
{% extends "global/Page.html" %}
{% block title %}{% endblock %}

{% block content %}
<div class="card">
    <div class="card-body text-center">
        <h3 class="mb-4">Information Recorded</h3>

        <div class="message-box mb-4">
            <p class="lead">Thank you for providing your information!</p>
            <p>Your responses have been successfully recorded.</p>
        </div>

        <div class="mt-4">
            <button class="btn btn-primary btn-lg" onclick="document.querySelector('form').submit();">
                Go to First Game
                <i class="fas fa-arrow-right ms-2"></i>
            </button>
        </div>

        <form method="post" style="display: none;">
            {% next_button %}
        </form>
    </div>
</div>

<style>
    .card {
        max-width: 600px;
        margin: 50px auto;
        border: none;
        box-shadow: 0 0 20px rgba(0,0,0,0.1);
    }

    .message-box {
        background: #f8f9fa;
        padding: 30px;
        border-radius: 10px;
        margin: 20px 0;
    }

    .lead {
        color: #2c3e50;
        font-size: 1.3em;
    }

    .btn-primary {
        background-color: #3498db;
        border: none;
        padding: 1rem 2rem;
        font-size: 1.1rem;
        transition: all 0.3s ease;
    }

    .btn-primary:hover {
        background-color: #2980b9;
        transform: scale(1.05);
    }

    .fas {
        font-size: 0.9em;
    }
</style>

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
{% endblock %}
```

# encryption_task\__init__.py

```py
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
```

# encryption_task\EncryptionTask.html

```html
{% extends "global/Page.html" %}
{% block app_styles %}
<style>
    .otree-timer {
        display: none;
    }
</style>
{% endblock %}
{% block title %}{% endblock %}

{% block content %}
<div class="card">
    <div class="card-body">
        <div class="instructions-section mb-4">
            <h3 class="text-center mb-3">Word Encryption Challenge</h3>
            <div class="alert alert-info">
                <h5>Instructions:</h5>
                <ul class="mb-0">
                    <li><strong>The timer has already started!</strong></li>
                    <li>You have <strong>3 minutes</strong> to encrypt all words</li>
                    <li>Convert letters to numbers (A=1, B=2, C=3, etc.)</li>
                    <li>Use 2 digits for each letter (01 for A, 02 for B, etc.)</li>
                    <li>Example: CAT → 030120</li>
                    <li>Your objective is to correctly encrypt <strong>as many words as possible</strong></li>
                    <li>Your ranking will be determined by the number of words you correctly encrypt</li>
                    <li>The more words you correctly encrypt compared to other participants, the higher your ranking</li>
                    <li>🏆 Remember: This is a competition! The top 10% of performers will receive an additional £0.50</li>
                    <li>🎲 In case of ties (where multiple participants achieve the same score), rankings will be determined randomly among those tied</li>
                </ul>
            </div>

            <div class="alert alert-warning mt-3">
                <h5>⚠️ Important Warning:</h5>
                <p class="mb-0"><strong>Please do not switch tabs or leave this page during the challenge.</strong> Navigating away from this page may be flagged as an attempt to search for answers online, which could result in your participation being disqualified. Stay on this page until you've completed all questions.</p>
            </div>

        </div>

        <div class="timer text-center mb-4">
            Time Remaining: <span id="timer">3:00</span>
        </div>

        <form id="form" method="post">
            {% for word, solution in words %}
            <div class="word-section mb-4">
                <div class="word-display">{{ word }}</div>
                <input type="text"
                       class="encryption-input"
                       placeholder="Enter encrypted number"
                       pattern="[0-9]*"
                       maxlength="30"
                       data-solution="{{ solution }}">
                <div class="feedback"></div>
            </div>
            {% endfor %}

            <input type="hidden" name="answers" id="answers">
            <input type="hidden" name="completion_time" id="completion_time">

            <div class="text-center">
                <button type="submit" class="submit-btn">Submit Answers</button>
            </div>
        </form>
    </div>
</div>

<style>
    .word-section {
        text-align: center;
        padding: 15px;
        background: #f8f9fa;
        border-radius: 8px;
        margin-bottom: 20px;
    }

    .word-display {
        font-size: 1.5rem;
        font-weight: bold;
        color: #2c3e50;
        letter-spacing: 3px;
        margin-bottom: 10px;
    }

    .encryption-input {
        width: 200px;
        padding: 10px;
        text-align: center;
        font-size: 1.2rem;
        border: 2px solid #ddd;
        border-radius: 5px;
        transition: border-color 0.3s ease;
    }

    .encryption-input:focus {
        border-color: #3498db;
        outline: none;
    }

    .submit-btn {
        background: #3498db;
        color: white;
        border: none;
        padding: 12px 30px;
        border-radius: 8px;
        font-size: 1.1rem;
        transition: all 0.3s ease;
    }

    .submit-btn:hover {
        background: #2980b9;
        transform: scale(1.05);
    }

    .timer {
        background: #f8f9fa;
        padding: 10px;
        border-radius: 8px;
        font-size: 1.2rem;
        font-weight: bold;
        color: #2c3e50;
    }
</style>

<script>
    let startTime = Date.now();

    function startTimer(duration) {
        let timer = duration;
        const display = document.getElementById('timer');

        const countdown = setInterval(function () {
            const minutes = parseInt(timer / 60, 10);
            const seconds = parseInt(timer % 60, 10);

            display.textContent = minutes + ":" + (seconds < 10 ? "0" : "") + seconds;

            // When 1 second left, preemptively collect answers
            if (timer === 1) {
                collectAndSetAnswers();
                console.log("Pre-emptively collected answers:", document.getElementById('answers').value);
            }

            if (--timer < 0) {
                clearInterval(countdown);
                // Do NOT try to collect answers here again
                document.getElementById('completion_time').value = {{ timeout_seconds }};
                document.querySelector("form").submit();
            }
        }, 1000);
    }

    // Add this new function
    function collectAndSetAnswers() {
        const inputs = document.querySelectorAll('.encryption-input');
        const answersArray = [];

        inputs.forEach(input => {
            answersArray.push(input.value.trim());
        });

        const answersString = answersArray.join(',');
        document.getElementById('answers').value = answersString;
    }


    // Update your form submit handler to use the same function
    document.querySelector('form').addEventListener('submit', function(e) {
        collectAndSetAnswers();
        const timeSpent = Math.floor((Date.now() - startTime) / 1000);
        document.getElementById('completion_time').value = timeSpent;
    });

    startTimer({{ timeout_seconds }});
</script>
{% endblock %}
```

# encryption_task\Results.html

```html
{% extends "global/Page.html" %}
{% block title %}Encryption Challenge - Results{% endblock %}

{% block content %}
<div class="card">
    <div class="card-body text-center">
        <h3 class="mb-4">Challenge Complete!</h3>

        <div class="result-box">
            <div class="result-label">Your Score</div>
            <div class="result-value">
                {{ correct_count }} out of {{ total_words }}
            </div>
            <div class="completion-time">
                Completed in {{ completion_time }} seconds
            </div>
        </div>

{% if show_quit_option %}
<div class="quit-section mt-4">
    <div class="quit-container">
        <div class="quit-header">
            <h4>⚠️ <span class="quit-title">IMPORTANT: EXIT OPTION AVAILABLE</span> ⚠️</h4>
        </div>
        <div class="quit-content">
            <p>You now have the option to <strong>exit this study</strong>.</p>
            <p>If you choose to exit now:</p>
            <ul>
                <li>You will still receive £2 for your participation in this study</li>
                <li>You will be eligible for performance bonuses for all the tasks where you have scored in the top 10%</li>
                <li>You will not need to complete any remaining tasks</li>
            </ul>
            <div class="quit-action">
                <button id="quit-button" class="btn btn-warning btn-lg">EXIT THE STUDY NOW</button>
                <p class="continue-note">To continue with the study, simply click the "Next" button below</p>
            </div>
        </div>
    </div>
</div>

<style>
    .quit-container {
        background-color: #fff8e1;
        border: 3px solid #ff9800;
        border-radius: 10px;
        padding: 20px;
        margin: 30px 0;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }

    .quit-header {
        background-color: #ff9800;
        margin: -20px -20px 15px -20px;
        padding: 10px;
        text-align: center;
        border-radius: 7px 7px 0 0;
    }

    .quit-title {
        color: white;
        font-weight: bold;
        font-size: 1.2em;
    }

    .quit-content {
        padding: 0 10px;
    }

    .quit-content p, .quit-content ul {
        font-size: 1.1em;
    }

    .quit-action {
        text-align: center;
        margin-top: 20px;
        padding-top: 15px;
        border-top: 1px dashed #ff9800;
    }

    #quit-button {
        font-size: 1.2em;
        padding: 10px 25px;
        background-color: #ff5722;
        border-color: #ff5722;
    }

    #quit-button:hover {
        background-color: #e64a19;
        border-color: #e64a19;
        transform: scale(1.05);
    }

    .continue-note {
        margin-top: 15px;
        font-style: italic;
        color: #555;
    }
</style>
{% endif %}

<script>
    document.addEventListener('DOMContentLoaded', function() {
    const quitButton = document.getElementById('quit-button');
    if (quitButton) {
        quitButton.addEventListener('click', function() {
            liveSend({ action: 'quit' }).then(response => {
                if (response[Object.keys(response)[0]].quit_status === 'success') {
                    window.location.href = "/End/";  // ✅ Redirect to End Page
                }
            });
        });
    }
});
</script>

        <div class="mt-4">
            {% next_button %}
        </div>
    </div>
</div>

<style>
    .card {
        max-width: 600px;
        margin: 50px auto;
        border: none;
        box-shadow: 0 0 20px rgba(0,0,0,0.1);
    }

    .result-box {
        background: #f8f9fa;
        padding: 30px;
        border-radius: 10px;
        margin: 20px 0;
    }

    .result-label {
        font-size: 1.2em;
        color: #666;
        margin-bottom: 10px;
    }

    .result-value {
        font-size: 3em;
        font-weight: bold;
        color: #2c3e50;
    }

    .completion-time {
        margin-top: 15px;
        color: #666;
        font-size: 1.1em;
    }
</style>
{% endblock %}
```

# End\__init__.py

```py
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
```

# End\End.html

```html
{% extends "global/Page.html" %}
{% block title %}{% endblock %}

{% block content %}
<div class="card">
    <div class="card-body text-center">
        <h2 class="mb-4">🎉 Congratulations!</h2>
        
        <div class="completion-message">
            {% if quit_early %}
                <p class="lead mb-4">You chose to exit the study early.</p>
                <p class="lead mb-4">In one week's time we will let you know your results. You will receive an additional £0.5 for each task that you have scored in the top 10%.</p>
                <p>Thank you for your time and effort!</p>

            {% else %}
                <p class="lead mb-4">You have completed all tasks in this study.</p>
                <p class="lead mb-4">In one week's time we will let you know your results. You will receive an additional £0.5 for each task that you have scored in the top 10%.</p>
                <p>Thank you for your time and effort!</p>
            {% endif %}
        </div>
    </div>
</div>

<style>
    .card {
        max-width: 600px;
        margin: 50px auto;
        border: none;
        box-shadow: 0 0 20px rgba(0,0,0,0.1);
    }

    .completion-message {
        background: #f8f9fa;
        padding: 30px;
        border-radius: 10px;
        margin: 20px 0;
    }
</style>
{% endblock %}
```

# End\Results.html

```html
{{ block title }}
    Page title
{{ endblock }}

{{ block content }}

    {{ next_button }}
{{ endblock }}



```

# GridCount_task\__init__.py

```py
from otree.api import *
import random

class Constants(BaseConstants):
    name_in_url = 'grid_count_task'
    players_per_group = None
    num_rounds = 1
    time_limit_seconds = 3 * 60
    grid_size = 58
    target_symbol = '0'
    target_count = 236

def generate_grid():
    total_cells = Constants.grid_size * Constants.grid_size
    cells = ['0'] * Constants.target_count + ['1'] * (total_cells - Constants.target_count)
    random.shuffle(cells)
    grid = [cells[i:i + Constants.grid_size] for i in range(0, total_cells, Constants.grid_size)]
    return grid

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    count_answer = models.IntegerField()
    is_correct = models.BooleanField()
    completion_time = models.IntegerField()

class GridCountTask(Page):
    timeout_seconds = Constants.time_limit_seconds
    form_model = 'player'
    form_fields = ['count_answer', 'completion_time']

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'grid': generate_grid(),
            'time_limit_seconds': Constants.time_limit_seconds,
        }

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.is_correct = player.count_answer == Constants.target_count

        # If the timeout happened, ensure completion_time is set to the full duration
        if timeout_happened:
            player.completion_time = Constants.time_limit_seconds
        # Consider partially correct answers as correct
        player.is_correct = player.count_answer > 0

class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return {
            'is_correct': player.is_correct,
            'actual_count': Constants.target_count,
            'participant_count': player.count_answer,
            'completion_time': player.completion_time
        }

page_sequence = [GridCountTask, Results]
```

# GridCount_task\GridCountTask.html

```html
{% extends "global/Page.html" %}
{% block app_styles %}
<style>
    .otree-timer {
        display: none;
    }
</style>
{% endblock %}

{% block title %}{% endblock %}

{% block content %}
<div class="card">
    <div class="card-body">
        <div class="instructions-section mb-4">
            <h3 class="text-center mb-3">Grid Counting Challenge</h3>
            <div class="alert alert-info">
                <h5>Instructions:</h5>
                <ul class="mb-0">
                    <li><strong>The timer has already started!</strong></li>
                    <li>You have <strong>3 minutes</strong> to complete this task</li>
                    <li>Your objective is to find and click <strong>as many zeros (0) as possible</strong> - the more zeros you find compared to other participants, the higher your ranking</li>
                    <li>Clicked zeros will be highlighted</li>
                    <li>The counter below will track your clicks</li>
                    <li>🏆 Remember: This is a competition! The top 10% of performers will receive an additional £0.50</li>
                    <li>🎲 In case of ties (where multiple participants achieve the same score), rankings will be determined randomly among those tied</li>
                </ul>
            </div>
        </div>

        <div class="timer-container text-center mb-4">
            <div class="stat-box">
                <span class="stat-label">Time Remaining:</span>
                <span class="stat-value" id="timer">3:00</span>
            </div>
        </div>

        <div class="count-display text-center mb-3">
            <span class="count-label">Zeros counted:</span>
            <span id="clickCount" class="count-value">0</span>
        </div>

        <div class="grid-container mb-4">
            <table class="grid-table">
                {% for row in grid %}
                <tr>
                    {% for cell in row %}
                    <td class="grid-cell" data-value="{{ cell }}">{{ cell }}</td>
                    {% endfor %}
                </tr>
                {% endfor %}
            </table>
        </div>

        <form method="post">
            <input type="hidden" name="count_answer" id="countInput">
            <input type="hidden" name="completion_time" id="completionTime">
            <div class="text-center mt-4">
                <button type="submit" class="btn btn-primary btn-lg">Submit Count</button>
            </div>
        </form>
    </div>
</div>

<style>
    .grid-container {
        overflow-x: auto;
        max-width: 100%;
    }

    .grid-table {
        border-collapse: collapse;
        margin: 0 auto;
    }

    .grid-cell {
        width: 35px;
        height: 35px;
        border: 1px solid #ccc;
        text-align: center;
        font-family: monospace;
        font-size: 1.2em;
        font-weight: bold;
        cursor: pointer;
        user-select: none;
    }

    .grid-cell[data-value="0"] {
        background-color: #f8f9fa;
    }

    .grid-cell.clicked {
        background-color: #d4edda !important;
        color: #155724;
    }

    .count-display {
        font-size: 1.3em;
        position: sticky;
        top: 0;
        background: white;
        padding: 10px;
        z-index: 100;
    }
</style>

<script>
    let clickCount = 0;
    let startTime = Date.now();
    const countDisplay = document.getElementById('clickCount');
    const countInput = document.getElementById('countInput');
    const completionTimeInput = document.getElementById('completionTime');

    document.querySelectorAll('.grid-cell[data-value="0"]').forEach(cell => {
        cell.addEventListener('click', function() {
            if (!this.classList.contains('clicked')) {
                this.classList.add('clicked');
                clickCount++;
            } else {
                this.classList.remove('clicked');
                clickCount--;
            }
            countDisplay.textContent = clickCount;
            countInput.value = clickCount;
        });
    });

    document.querySelector('form').addEventListener('submit', function() {
        const endTime = Date.now();
        const timeSpent = Math.floor((endTime - startTime) / 1000);
        completionTimeInput.value = timeSpent;
    });

    function startTimer(duration) {
        let timer = duration;
        const display = document.getElementById('timer');

        const countdown = setInterval(function () {
            const minutes = parseInt(timer / 60, 10);
            const seconds = parseInt(timer % 60, 10);

            display.textContent = minutes + ":" + (seconds < 10 ? "0" : "") + seconds;

            if (--timer < 0) {
                clearInterval(countdown);
                // Set completion time to the full duration when timer expires
                document.getElementById('completionTime').value = {{ time_limit_seconds }};
                document.querySelector("form").submit();
            }
        }, 1000);
    }

    startTimer({{ time_limit_seconds }});
</script>
{% endblock %}
```

# GridCount_task\Results.html

```html
{% extends "global/Page.html" %}
{% block title %}Grid Count Complete{% endblock %}

{% block content %}
<div class="card">
    <div class="card-body text-center">
        <h3 class="mb-4">Challenge Complete!</h3>

        <div class="result-box">
            <div class="result-label">Your Count</div>
            <div class="result-value {% if is_correct %}text-success{% else %}text-danger{% endif %}">
                {{ participant_count }}
            </div>
            <div class="result-details">
                Correct count: {{ actual_count }}
            </div>
            <div class="completion-time">
                Time taken: {{ completion_time }} seconds
            </div>
        </div>

        <div class="mt-4">
            {% next_button %}
        </div>
    </div>
</div>

<style>
    .card {
        max-width: 600px;
        margin: 50px auto;
        border: none;
        box-shadow: 0 0 20px rgba(0,0,0,0.1);
    }

    .result-box {
        background: #f8f9fa;
        padding: 30px;
        border-radius: 10px;
        margin: 20px 0;
    }

    .text-success {
        color: #28a745 !important;
    }

    .text-danger {
        color: #dc3545 !important;
    }
</style>
{% endblock %}
```

# ImageID_task\__init__.py

```py
from otree.api import *

class Constants(BaseConstants):
    name_in_url = 'ImageID_task'
    players_per_group = None
    num_rounds = 1
    timeout_seconds = 120  # 2 minutes

    images_data = [
        {
            'name': 'eagle.png',
            'url': 'imageid_task/eagle.png',
            'question': 'What animal is this?',
            'options': ['1. Earthworm', '2. Sea Cucumber', '3. Naked Mole Rat', '4. Blobfish', '5. Axolotl', '6. Goat', '7. Cabbage Moth', '8. Dung Beetle', '9. Star-nosed Mole', '10. Hammerhead Shark', '11. Leopard Slug', '12. Proboscis Monkey', '13. Eagle', '14. Narwhal', '15. Amoeba', '16. Coconut Crab', '17. Tardigrade', '18. Mudskipper', '19. Sea Sponge', '20. Pistol Shrimp', '21. Blue Dragon Nudibranch', '22. Lungfish', '23. Fainting Goat', '24. Manatee', '25. Platypus', '26. Giant Isopod', '27. Hagfish', '28. Shoebill Stork', '29. Liger', '30. Wombat', '31. Sun Bear', '32. Yeti Crab', '33. Mimic Octopus', '34. Frilled Lizard', '35. Glass Frog', '36. Zebra Turkeyfish', '37. Japanese Spider Crab', '38. Dumbo Octopus', '39. Aye-Aye', '40. Leafy Sea Dragon', '41. Jerboa', '42. Satanic Leaf-Tailed Gecko', '43. Fossa', '44. Goblin Shark', '45. Okapi', '46. Indian Purple Frog', '47. Quokka', '48. Giant Anteater', '49. Tasmanian Devil'],
            'correct': '13. Eagle'
        },
        {
            'name': 'Car2.png',
            'url': 'imageid_task/Car2.png',
            'question': 'What car brand is this?',
            'options': ['1. BMW', '2. Mercedes-Benz', '3. Audi', '4. Porsche', '5. Lamborghini', '6. Maserati', '7. Bentley', '8. Rolls-Royce', '9. Jaguar', '10. Land Rover', '11. Lexus', '12. Toyota', '13. Honda', '14. Nissan', '15. Mazda', '16. Subaru', '17. Volkswagen', '18. Ford', '19. Chevrolet', '20. Dodge', '21. Chrysler', '22. Jeep', '23. Hyundai', '24. Kia', '25. Volvo', '26. Peugeot', '27. Renault', '28. Fiat', '29. Alfa Romeo', '30. Mini', '31. Tesla', '32. Smart', '33. Acura', '34. Infiniti', '35. Cadillac', '36. Lincoln', '37. Buick', '38. GMC', '39. Ram', '40. Pontiac', '41. Saturn', '42. DeLorean', '43. Ferrari', '44. McLaren', '45. Aston Martin', '46. Bugatti', '47. Pagani', '48. Koenigsegg', '49. Lotus', '50. Genesis'],
            'correct': '43. Ferrari'
        },
        {
            'name': 'game.png',
            'url': 'imageid_task/game.png',
            'question': 'What board game is this?',
            'options': ['1. Chess', '2. Checkers', '3. Scrabble', '4. Risk', '5. Catan', '6. Clue', '7. Battleship', '8. Sorry!', '9. Monopoly', '10. The Game of Life', '11. Candy Land', '12. Chutes and Ladders', '13. Trivial Pursuit', '14. Stratego', '15. Axis & Allies', '16. Carcassonne', '17. Ticket to Ride', '18. Pandemic', '19. Codenames', '20. Dominion', '21. Azul', '22. Twilight Struggle', '23. Gloomhaven', '24. 7 Wonders', '25. Agricola', '26. Power Grid', '27. Small World', '28. Eldritch Horror', '29. Terra Mystica', '30. Puerto Rico', '31. King of Tokyo', '32. Blood Rage', '33. Tigris & Euphrates', '34. Arkham Horror', '35. Shogun', '36. Through the Ages', '37. Brass: Birmingham', '38. Betrayal at House on the Hill', '39. Caverna', '40. Scythe', '41. Dixit', '42. Patchwork', '43. Splendor', '44. Jaipur', '45. Camel Up', '46. Hive', '47. Tsuro', '48. Hanabi', '49. Love Letter', '50. Telestrations'],
            'correct': '9. Monopoly'
        },
        {
            'name': 'Band.png',
            'url': 'imageid_task/Band.png',
            'question': 'Which band is this?',
            'options': ['1. The Beatles', '2. The Rolling Stones', '3. Led Zeppelin', '4. Pink Floyd', '5. The Doors', '6. The Who', '7. The Kinks', '8. Fleetwood Mac', '9. Deep Purple', '10. The Clash', '11. The Smiths', '12. The Cure', '13. Joy Division', '14. The Police', '15. Talking Heads', '16. Nirvana', '17. Pearl Jam', '18. Soundgarden', '19. Alice in Chains', '20. Foo Fighters', '21. Radiohead', '22. Coldplay', '23. Muse', '24. Arctic Monkeys', '25. The Strokes', '26. Red Hot Chili Peppers', '27. Green Day', '28. Blink-182', '29. My Chemical Romance', '30. Paramore', '31. Metallica', '32. Iron Maiden', '33. Black Sabbath', '34. Megadeth', '35. Slayer', '36. AC/DC', '37. Guns N Roses', '38. Aerosmith', '39. Bon Jovi', '40. Van Halen', '41. The Eagles', '42. The Beach Boys', '43. The Byrds', '44. The Velvet Underground', '45. Genesis', '46. Yes', '47. King Crimson', '48. Rush', '49. Queen', '50. ELO', '51. Tame Impala', '52. The National', '53. The Smashing Pumpkins', '54. The White Stripes', '55. The Black Keys'],
            'correct': '49. Queen'
        },
        {
            'name': 'Stadium.png',
            'url': 'imageid_task/Stadium.png',
            'question': 'Which NFL team plays in this stadium?',
            'options': ['1. Arizona Cardinals', '2. Atlanta Falcons', '3. Baltimore Ravens', '4. Buffalo Bills', '5. Carolina Panthers', '6. Chicago Bears', '7. Cincinnati Bengals', '8. Cleveland Browns', '9. Dallas Cowboys', '10. Denver Broncos', '11. Detroit Lions', '12. Green Bay Packers', '13. Houston Texans', '14. Indianapolis Colts', '15. Jacksonville Jaguars', '16. Kansas City Chiefs', '17. Las Vegas Raiders', '18. Los Angeles Chargers', '19. Los Angeles Rams', '20. Miami Dolphins', '21. Minnesota Vikings', '22. New England Patriots', '23. New Orleans Saints', '24. New York Giants', '25. New York Jets', '26. Philadelphia Eagles', '27. Pittsburgh Steelers', '28. San Francisco 49ers', '29. Seattle Seahawks', '30. Tampa Bay Buccaneers', '31. Tennessee Titans', '32. Washington Commanders'],
            'correct': '21. Minnesota Vikings'
        },
        {
            'name': 'trophy.png',
            'url': 'imageid_task/trophy.png',
            'question': 'What is the name of this award trophy?',
            'options': ['1. Golden Globe', '2. Primetime Emmy Award', '3. Daytime Emmy Award', '4. Grammy Award', '5. Tony Award', '6. BAFTA Award', '7. Screen Actors Guild (SAG) Award', '8. Critics\' Choice Award', '9. MTV Movie & TV Award', '10. People\'s Choice Award', '11. Independent Spirit Award', '12. Cannes Palme d\'Or', '13. Venice Film Festival Golden Lion', '14. Berlin Film Festival Golden Bear', '15. Goya Award', '16. César Award', '17. Hollywood Walk of Fame Star', '18. Nickelodeon Kids\' Choice Award', '19. BET Award', '20. NAACP Image Award', '21. Country Music Association (CMA) Award', '22. Academy of Country Music (ACM) Award', '23. Billboard Music Award', '24. American Music Award', '25. MTV Europe Music Award', '26. Brit Award', '27. Juno Award', '28. Mercury Prize', '29. Pulitzer Prize for Drama', '30. Tony Award for Best Musical', '31. Oscar', '32. Golden Raspberry (Razzie) Award', '33. Saturn Award', '34. Hugo Award', '35. Nebula Award', '36. Clio Award', '37. Peabody Award', '38. Television Critics Association (TCA) Award', '39. Drama Desk Award', '40. Olivier Award', '41. Hollywood Critics Association Award', '42. Webby Award', '43. Shorty Award', '44. Streamy Award', '45. Game Awards Trophy', '46. Annie Award', '47. Kidscreen Award', '48. Producers Guild of America (PGA) Award', '49. Writers Guild of America (WGA) Award', '50. Directors Guild of America (DGA) Award'],
            'correct': '31. Oscar'
        },
        {
            'name': 'Wonder.png',
            'url': 'imageid_task/Wonder.png',
            'question': 'Which Wonder of the World is this?',
            'options': ['1. Eiffel Tower', '2. Statue of Liberty', '3. Great Wall of China', '4. Big Ben', '5. Colosseum', '6. Taj Mahal', '7. Machu Picchu', '8. Christ the Redeemer', '9. Sydney Opera House', '10. Mount Rushmore', '11. Stonehenge', '12. Petra', '13. Angkor Wat', '14. Burj Khalifa', '15. Leaning Tower of Pisa', '16. Chichen Itza', '17. Neuschwanstein Castle', '18. The Pyramids', '19. Hagia Sophia', '20. Sagrada Familia', '21. Brandenburg Gate', '22. Golden Gate Bridge', '23. Tower of London', '24. Acropolis of Athens', '25. Alhambra', '26. Versailles Palace', '27. Moai Statues (Easter Island)', '28. Mont Saint-Michel', '29. CN Tower', '30. Empire State Building', '31. Kremlin', '32. Edinburgh Castle', '33. St. Basil’s Cathedral', '34. Niagara Falls', '35. Grand Canyon', '36. Mount Fuji', '37. Victoria Falls', '38. Santorini (Oia Village)', '39. Christchurch Cathedral', '40. Forbidden City', '41. Louvre Museum', '42. The Blue Mosque', '43. Tiananmen Square', '44. Buckingham Palace', '45. Hollywood Sign', '46. Brooklyn Bridge', '47. Pompeii', '48. Guggenheim Museum', '49. Red Square', '50. Table Mountain', '51. White House'],
            'correct': '18. The Pyramids'
        },
        {
            'name': 'food.png',
            'url': 'imageid_task/food.png',
            'question': 'Which food chain owns this logo?',
            'options': ['1. Burger King', '2. KFC', '3. Wendy\'s', '4. Taco Bell', '5. Subway', '6. Pizza Hut', '7. Domino\'s', '8. Papa John\'s', '9. Dairy Queen', '10. Starbucks', '11. Chick-fil-A', '12. Chipotle', '13. Five Guys', '14. Panda Express', '15. Dunkin\' Donuts', '16. Sonic Drive-In', '17. Arby\'s', '18. Jack in the Box', '19. Little Caesars', '20. Culver\'s', '21. Shake Shack', '22. In-N-Out Burger', '23. Zaxby\'s', '24. Raising Cane\'s', '25. Bojangles', '26. Whataburger', '27. Hardee\'s', '28. Carl\'s Jr.', '29. Wingstop', '30. Jersey Mike\'s Subs', '31. Jimmy John\'s', '32. Qdoba', '33. Del Taco', '34. El Pollo Loco', '35. White Castle', '36. Boston Market', '37. Church\'s Chicken', '38. Quiznos', '39. Tim Hortons', '40. Blaze Pizza', '41. Checkers', '42. Krystal', '43. Freddy\'s Frozen Custard', '44. Nando\'s', '45. Sweetgreen', '46. Firehouse Subs', '47. Pret A Manger', '48. McDonald\'s', '49. McAlister\'s Deli', '50. Portillo\'s'],
            'correct': '48. McDonald\'s'
        },
        {
            'name': 'movie.png',
            'url': 'imageid_task/movie.png',
            'question': 'Which movie poster is this?',
            'options': ['1. The Godfather', '2. The Shawshank Redemption', '3. The Dark Knight', '4. Forrest Gump', '5. Inception', '6. The Matrix', '7. Titanic', '8. The Lord of the Rings: The Return of the King', '9. Gladiator', '10. Schindler\'s List', '11. The Silence of the Lambs', '12. Saving Private Ryan', '13. Interstellar', '14. The Green Mile', '15. Fight Club', '16. The Departed', '17. The Prestige', '18. Goodfellas', '19. The Usual Suspects', '20. Django Unchained', '21. Se7en', '22. The Wolf of Wall Street', '23. No Country for Old Men', '24. There Will Be Blood', '25. Casablanca', '26. Braveheart', '27. The Grand Budapest Hotel', '28. A Beautiful Mind', '29. The Social Network', '30. Joker', '31. La La Land', '32. Whiplash', '33. The Revenant', '34. Mad Max: Fury Road', '35. Once Upon a Time in Hollywood', '36. The Truman Show', '37. The Shining', '38. Parasite', '39. Oldboy', '40. The Big Lebowski', '41. Pulp Fiction', '42. The Lion King', '43. Avengers: Endgame', '44. Spider-Man: Into the Spider-Verse', '45. Guardians of the Galaxy', '46. Logan', '47. The Incredibles', '48. Toy Story', '49. Coco', '50. Up', '51. Inside Out'],
            'correct': '41. Pulp Fiction'
        },
        {
            'name': 'sport.png',
            'url': 'imageid_task/sport.png',
            'question': 'Which Olympic sport is shown in this image?',
            'options': ['1. Soccer', '2. Basketball', '3. Tennis', '4. Baseball', '5. Football', '6. Rugby', '7. Cricket', '8. Golf', '9. Hockey', '10. Lacrosse', '11. Volleyball', '12. Badminton', '13. Table Tennis', '14. Handball', '15. Squash', '16. Bowling', '17. Darts', '18. Archery', '19. Shooting', '20. Weightlifting', '21. Powerlifting', '22. Bodybuilding', '23. Swimming', '24. Diving', '25. Water Polo', '26. Sailing', '27. Rowing', '28. Kayaking', '29. Fencing', '30. Canoeing', '31. Surfing', '32. Skiing', '33. Snowboarding', '34. Skateboarding', '35. Ice Skating', '36. Speed Skating', '37. Cycling', '38. BMX', '39. Motocross', '40. Auto Racing', '41. Equestrian', '42. Wrestling', '43. Boxing', '44. Kickboxing', '45. Judo', '46. Karate', '47. Taekwondo', '48. Muay Thai', '49. Brazilian Jiu-Jitsu', '50. Sumo Wrestling'],
            'correct': '29. Fencing'
        }
    ]

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    correct_count = models.IntegerField(initial=0)
    completion_time = models.IntegerField(initial=0)
    quit_early = models.BooleanField(initial=False)

    image1_response = models.StringField(blank=True)
    image2_response = models.StringField(blank=True)
    image3_response = models.StringField(blank=True)
    image4_response = models.StringField(blank=True)
    image5_response = models.StringField(blank=True)
    image6_response = models.StringField(blank=True)
    image7_response = models.StringField(blank=True)
    image8_response = models.StringField(blank=True)
    image9_response = models.StringField(blank=True)
    image10_response = models.StringField(blank=True)

class ImageID(Page):
    form_model = 'player'
    form_fields = ['image1_response', 'image2_response', 'image3_response',
                   'image4_response', 'image5_response', 'image6_response',
                   'image7_response', 'image8_response', 'image9_response',
                   'image10_response', 'completion_time']
    timeout_seconds = Constants.timeout_seconds

    @staticmethod
    def is_displayed(player):
        return not player.participant.vars.get('finished', False)  # ✅ Skip if quit


    @staticmethod
    def vars_for_template(player: Player):
        return {
            'images_data': Constants.images_data,
            'timeout_seconds': Constants.timeout_seconds
        }

    @staticmethod
    def before_next_page(player, timeout_happened):
        # Set completion time for timeout
        if timeout_happened:
            player.completion_time = Constants.timeout_seconds

        # ✅ If the player chose to quit, move them directly to "End"
        if player.participant.vars.get('quit', False):
            try:
                end_index = player.session.config['app_sequence'].index('End')  # 🚀 Find the "End" app position
                player.participant._index_in_pages = end_index  # ✅ Move directly to "End"
            except ValueError:
                player.participant._index_in_pages = len(player.session.config['app_sequence'])  # Fallback
            player.participant.vars['finished'] = True  # ✅ Ensures all remaining pages are skipped
            return  # 🚀 Stops any further processing

        # ✅ If the player did not quit, count correct answers
        player.correct_count = sum(
            1 for i in range(len(Constants.images_data))
            if getattr(player, f'image{i + 1}_response', "").strip().lower() ==
            Constants.images_data[i]['correct'].strip().lower()
        )

class Results(Page):
    @staticmethod
    def vars_for_template(player):
        return {
            'correct_count': player.correct_count,
            'total_images': len(Constants.images_data),
            'completion_time': player.completion_time,
            'show_quit_option': player.session.config.get('quit_option', False)  # ✅ Fixes error
        }

    @staticmethod
    def live_method(player, data):
        if data.get('action') == 'quit':
            player.participant.vars['quit'] = True
            player.participant.vars['finished'] = True  # ✅ Ensures future tasks are skipped
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

    #@staticmethod
    #def is_displayed(player):
        #return not player.participant.vars.get('finished', False)  # ✅ Skips if the player quit

page_sequence = [ImageID, Results]

```

# ImageID_task\_static\apple.png

This is a binary file of the type: Image

# ImageID_task\_static\Band.png

This is a binary file of the type: Image

# ImageID_task\_static\book.png

This is a binary file of the type: Image

# ImageID_task\_static\car_new.png

This is a binary file of the type: Image

# ImageID_task\_static\Car2.png

This is a binary file of the type: Image

# ImageID_task\_static\chair.png

This is a binary file of the type: Image

# ImageID_task\_static\dog.png

This is a binary file of the type: Image

# ImageID_task\_static\eagle.png

This is a binary file of the type: Image

# ImageID_task\_static\food.png

This is a binary file of the type: Image

# ImageID_task\_static\game.png

This is a binary file of the type: Image

# ImageID_task\_static\house.png

This is a binary file of the type: Image

# ImageID_task\_static\mountain.png

This is a binary file of the type: Image

# ImageID_task\_static\movie.png

This is a binary file of the type: Image

# ImageID_task\_static\pencil.png

This is a binary file of the type: Image

# ImageID_task\_static\phone.png

This is a binary file of the type: Image

# ImageID_task\_static\sport.png

This is a binary file of the type: Image

# ImageID_task\_static\Stadium.png

This is a binary file of the type: Image

# ImageID_task\_static\tree.png

This is a binary file of the type: Image

# ImageID_task\_static\trophy.png

This is a binary file of the type: Image

# ImageID_task\_static\Wonder.png

This is a binary file of the type: Image

# ImageID_task\ImageID.html

```html
{% extends "global/Page.html" %}
{% block app_styles %}
<style>
    .otree-timer {
        display: none;
    }
</style>
{% endblock %}
{% load static %}

{% block content %}
<div class="card">
    <div class="card-body">
        <div class="instructions-section mb-4">
            <h3 class="text-center mb-3">Image Identification Challenge</h3>
            <div class="alert alert-info">
                <h5>Instructions:</h5>
                <ul class="mb-0">
                    <li><strong>The timer has already started!</strong></li>
                    <li>You have <strong>2 minutes</strong> to complete this task</li>
                    <li>You will be presented with <strong>10 different images</strong></li>
                    <li>Your objective is to correctly identify <strong>as many images as possible</strong> by selecting the correct option for each image via the drop-down menu.</li>
                    <li>The more images you correctly identify compared to other participants, the higher your ranking</li>
                    <li>🏆 Remember: This is a competition! The top 10% of performers will receive an additional £0.50</li>
                    <li>🎲 In case of ties (where multiple participants achieve the same score), rankings will be determined randomly among those tied</li>
                </ul>
            </div>
        </div>

        <div class="timer text-center mb-4">
            Time Remaining: <span id="timer">2:00</span>
        </div>

        <form id="form" method="post">
            {% for image in images_data %}
            <div class="image-question mb-5">
                <div class="question-header mb-2">Image {{ forloop.counter }} of 10</div>
                <h4 class="question-text mb-3">{{ image.question }}</h4>
                <div class="image-container">
                    <img src="{% static image.url %}" class="rounded-image" alt="Image {{ forloop.counter }}">
                </div>
                <div class="select-wrapper">
                    <select name="image{{ forloop.counter }}_response" class="custom-select" required>
                        <option value="">Select an option</option>
                        {% for option in image.options %}
                        <option value="{{ option }}">{{ option }}</option>
                        {% endfor %}
                    </select>
                </div>
            </div>
            {% endfor %}

            <input type="hidden" name="completion_time" id="completion_time" value="0">
            <div class="text-center">
                <button type="submit" class="submit-btn">Submit Answers</button>
            </div>
        </form>
    </div>
</div>

<style>
    .card {
        max-width: 800px;
        margin: 30px auto;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }

    .question-text {
    color: #2c3e50;
    font-weight: 500;
    text-align: center;
    margin: 15px 0;
    font-size: 1.2rem;  /* Matches your other text sizes */
}

    .rounded-image {
        max-width: 300px;
        height: auto;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        transition: transform 0.3s ease;
    }

    .rounded-image:hover {
        transform: scale(1.02);
    }

    .image-container {
        text-align: center;
        margin: 20px 0;
    }

    .select-wrapper {
        position: relative;
        max-width: 300px;
        margin: 0 auto;
    }

    .custom-select {
        width: 100%;
        padding: 12px;
        border: 2px solid #ddd;
        border-radius: 8px;
        background-color: white;
        appearance: none;
        cursor: pointer;
        font-size: 1rem;
    }

    .select-wrapper::after {
        content: '▼';
        font-size: 1rem;
        color: #666;
        position: absolute;
        right: 12px;
        top: 50%;
        transform: translateY(-50%);
        pointer-events: none;
    }

    .custom-select:focus {
        border-color: #3498db;
        outline: none;
    }

    .timer {
        background: #f8f9fa;
        padding: 10px;
        border-radius: 8px;
        font-size: 1.2rem;
        font-weight: bold;
        color: #2c3e50;
    }

    .submit-btn {
        background: #3498db;
        color: white;
        border: none;
        padding: 12px 30px;
        border-radius: 8px;
        font-size: 1.1rem;
        transition: all 0.3s ease;
    }

    .submit-btn:hover {
        background: #2980b9;
        transform: scale(1.05);
    }

    .question-header {
        color: #2c3e50;
        font-weight: bold;
        text-align: center;
    }
</style>

<script>
    let startTime = Date.now();

    function startTimer(duration) {
        let timer = duration;
        const display = document.getElementById('timer');

        const countdown = setInterval(function () {
            const minutes = parseInt(timer / 60, 10);
            const seconds = parseInt(timer % 60, 10);

            display.textContent = minutes + ":" + (seconds < 10 ? "0" : "") + seconds;

            if (--timer < 0) {
                clearInterval(countdown);
                document.querySelector("form").submit();
            }
        }, 1000);
    }

    document.querySelector('form').addEventListener('submit', function() {
        const timeSpent = Math.floor((Date.now() - startTime) / 1000);
        document.getElementById('completion_time').value = timeSpent;
    });

    startTimer({{ timeout_seconds }});
</script>
{% endblock %}
```

# ImageID_task\Results.html

```html
{% extends "global/Page.html" %}
{% block title %}Image Challenge - Results{% endblock %}

{% block content %}
<div class="card">
    <div class="card-body text-center">
        <h3 class="mb-4">Challenge Complete!</h3>

        <div class="result-box">
            <div class="result-label">Your Performance</div>
            <div class="result-value">
                {{ correct_count }} out of {{ total_images }}
            </div>
            <div class="result-details">
                Images Correctly Identified
            </div>
            <div class="completion-time">
                Completed in {{ completion_time }} seconds
            </div>
        </div>

{% if show_quit_option %}
<div class="quit-section mt-4">
    <div class="quit-container">
        <div class="quit-header">
            <h4>⚠️ <span class="quit-title">IMPORTANT: EXIT OPTION AVAILABLE</span> ⚠️</h4>
        </div>
        <div class="quit-content">
            <p>You now have the option to <strong>exit this study</strong>.</p>
            <p>If you choose to exit now:</p>
            <ul>
                <li>You will still receive £2 for your participation in this study</li>
                <li>You will be eligible for performance bonuses for all the tasks where you have scored in the top 10%</li>
                <li>You will not need to complete any remaining tasks</li>
            </ul>
            <div class="quit-action">
                <button id="quit-button" class="btn btn-warning btn-lg">EXIT THE STUDY NOW</button>
                <p class="continue-note">To continue with the study, simply click the "Next" button below</p>
            </div>
        </div>
    </div>
</div>

<style>
    .quit-container {
        background-color: #fff8e1;
        border: 3px solid #ff9800;
        border-radius: 10px;
        padding: 20px;
        margin: 30px 0;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }

    .quit-header {
        background-color: #ff9800;
        margin: -20px -20px 15px -20px;
        padding: 10px;
        text-align: center;
        border-radius: 7px 7px 0 0;
    }

    .quit-title {
        color: white;
        font-weight: bold;
        font-size: 1.2em;
    }

    .quit-content {
        padding: 0 10px;
    }

    .quit-content p, .quit-content ul {
        font-size: 1.1em;
    }

    .quit-action {
        text-align: center;
        margin-top: 20px;
        padding-top: 15px;
        border-top: 1px dashed #ff9800;
    }

    #quit-button {
        font-size: 1.2em;
        padding: 10px 25px;
        background-color: #ff5722;
        border-color: #ff5722;
    }

    #quit-button:hover {
        background-color: #e64a19;
        border-color: #e64a19;
        transform: scale(1.05);
    }

    .continue-note {
        margin-top: 15px;
        font-style: italic;
        color: #555;
    }
</style>
{% endif %}

<script>
    document.addEventListener('DOMContentLoaded', function() {
    const quitButton = document.getElementById('quit-button');
    if (quitButton) {
        quitButton.addEventListener('click', function() {
            liveSend({ action: 'quit' }).then(response => {
                if (response[Object.keys(response)[0]].quit_status === 'success') {
                    window.location.replace("/End/");  // ✅ Forces navigation to End
                }
            });
        });
    }
});
</script>
        <div class="mt-4">
            {% next_button %}
        </div>
    </div>
</div>

<style>
    .card {
        max-width: 600px;
        margin: 50px auto;
        border: none;
        box-shadow: 0 0 20px rgba(0,0,0,0.1);
    }

    .result-box {
        background: #f8f9fa;
        padding: 30px;
        border-radius: 10px;
        margin: 20px 0;
    }

    .result-label {
        font-size: 1.2em;
        color: #666;
        margin-bottom: 10px;
    }

    .result-value {
        font-size: 3em;
        font-weight: bold;
        color: #2c3e50;
    }

    .result-details, .completion-time {
        margin-top: 15px;
        color: #666;
        font-size: 1.1em;
    }
</style>
{% endblock %}
```

# numbertype_task\__init__.py

```py
from otree.api import *

class Constants(BaseConstants):
    name_in_url = 'numbertype_task'
    players_per_group = None
    num_rounds = 1
    time_limit_seconds = 3 * 60  # 3 minutes
    numbers_to_sort = list(range(0, 100))  # Numbers from 0 to 100


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    sorted_numbers = models.LongStringField()  # Stores the participant's input
    correct_count = models.IntegerField(initial=0)  # Number of correctly sorted numbers
    completion_time = models.IntegerField(initial=0)  # Add this field


class NumberTypingTask(Page):
    timeout_seconds = Constants.time_limit_seconds
    form_model = 'player'
    form_fields = ['sorted_numbers', 'completion_time']

    def vars_for_template(self):
        import random
        shuffled_numbers = Constants.numbers_to_sort[:]
        random.shuffle(shuffled_numbers)
        return {
            'shuffled_numbers': shuffled_numbers,
            'time_limit_seconds': Constants.time_limit_seconds,
        }

    def before_next_page(self, **kwargs):  # Keep the **kwargs approach
        # Handle timeout
        if kwargs.get('timeout_happened', False):
            self.completion_time = Constants.time_limit_seconds

        # Process the sorted numbers with better error handling
        try:
            # Clean up input: strip whitespace and handle potential trailing commas
            cleaned_input = self.sorted_numbers.strip()
            if cleaned_input.endswith(','):
                cleaned_input = cleaned_input[:-1]

            # Split by commas and clean each element
            number_strings = [num.strip() for num in cleaned_input.split(',')]

            # Convert to integers with careful handling
            participant_input = []
            for num_str in number_strings:
                if num_str:  # Only process non-empty strings
                    try:
                        participant_input.append(int(num_str))
                    except ValueError:
                        # Skip invalid entries instead of failing completely
                        pass

            # Generate the correct order (descending from 99 to 0)
            correct_order = sorted(Constants.numbers_to_sort, reverse=True)

            # Count correct positions
            correct_count = 0
            for i, num in enumerate(participant_input):
                if i < len(correct_order) and num == correct_order[i]:
                    correct_count += 1

            self.correct_count = correct_count

            # Debug output
            print(f"Processed {len(participant_input)} numbers, found {self.correct_count} correct")
        except Exception as e:
            print(f"Error processing numbers: {e}")
            print(f"Raw input: {self.sorted_numbers}")
            self.correct_count = 0


class Results(Page):
    def vars_for_template(self):
        return {
            'correct_count': self.correct_count,
            'completion_time': self.completion_time,  # Add this line
        }


page_sequence = [NumberTypingTask, Results]

```

# numbertype_task\NumberTypingTask.html

```html
{% extends "global/Page.html" %}
{% block app_styles %}
<style>
    .otree-timer {
        display: none;
    }
</style>
{% endblock %}
{% block title %}{% endblock %}
{% block content %}
<div class="card">
    <div class="card-body">
        <!-- Instructions Section -->
        <div class="instructions-section mb-4">
            <h3 class="text-center mb-3">Number Typing Challenge</h3>
            <div class="alert alert-info">
                <h5>Instructions:</h5>
                <ul class="mb-0">
                    <li><strong>The timer has already started!</strong></li>
                    <li>You have <strong>3 minutes</strong> to complete this task</li>
                    <li>Arrange the numbers in <strong>descending order</strong> (highest to lowest)</li>
                    <li>Your ranking will be determined by how many numbers you correctly order, counted sequentially from the largest number downward</li>
                    <li>The more numbers you correctly arrange compared to other participants, the higher your ranking</li>
                    <li>Separate each number with a comma <strong>","</strong>.</li>
                    <li>Example format: 29, 28, 27, 26,...</li>
                    <li>🏆 Remember: This is a competition! The top 10% of performers will receive an additional £0.50</li>
                    <li>🎲 In case of ties (where multiple participants achieve the same score), rankings will be determined randomly among those tied</li>
                </ul>
            </div>
        </div>

        <!-- Timer -->
        <div class="timer-container text-center mb-4">
            <div class="stat-box">
                <span class="stat-label">Time Remaining:</span>
                <span class="stat-value" id="timer">3:00</span>
            </div>
        </div>

        <!-- Numbers Display -->
        <div class="numbers-display mb-4">
            <div class="numbers-label">Numbers to arrange:</div>
            <div class="numbers-content">
                {{ shuffled_numbers }}
            </div>
        </div>

        <!-- Input Form -->
        <form method="post">
            <div class="form-group">
                <textarea
                    name="sorted_numbers"
                    id="numbers-input"
                    class="form-control"
                    rows="4"
                    placeholder="Enter numbers separated by commas, e.g., 29,28,27,..."
                    required
                ></textarea>
            </div>

            <!-- Counter Display -->
            <div class="counter-display mt-3 p-3 bg-light rounded">
                <div class="d-flex justify-content-between">
                    <span>Numbers entered: <span id="entered-count" class="font-weight-bold">0</span>/100</span>
                    <span>In correct position: <span id="correct-count" class="font-weight-bold text-success">0</span></span>
                </div>
                <div class="progress mt-2">
                    <div id="progress-bar" class="progress-bar bg-success" role="progressbar" style="width: 0%"></div>
                </div>
            </div>

            <input type="hidden" name="completion_time" id="completionTime" value="0">

            <div class="text-center mt-4">
                <button type="submit" class="btn btn-primary btn-lg">Submit Answer</button>
            </div>
        </form>
    </div>
</div>

<style>
    .card {
        max-width: 800px;
        margin: 0 auto;
        border: none;
        box-shadow: 0 0 20px rgba(0,0,0,0.1);
    }

    .alert-info {
        background-color: #f8f9fa;
        border-left: 4px solid #3498db;
        border-radius: 0;
    }

    .alert-info ul {
        list-style-type: none;
        padding-left: 0;
    }

    .alert-info li {
        margin-bottom: 8px;
        position: relative;
        padding-left: 20px;
    }

    .alert-info li:before {
        content: "•";
        color: #3498db;
        position: absolute;
        left: 0;
    }

    .timer-container {
        position: sticky;
        top: 0;
        background: white;
        padding: 10px;
        z-index: 100;
    }

    .stat-box {
        background: #f8f9fa;
        padding: 15px 25px;
        border-radius: 10px;
        display: inline-block;
    }

    .stat-value {
        font-size: 1.5em;
        font-weight: bold;
        color: #2c3e50;
        margin: 0 10px;
    }

    .numbers-display {
        background: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
    }

    .numbers-label {
        font-weight: bold;
        margin-bottom: 10px;
        color: #2c3e50;
    }

    .numbers-content {
        font-family: monospace;
        font-size: 1.2em;
        word-wrap: break-word;
    }

    textarea.form-control {
        font-family: monospace;
        font-size: 1.1em;
        padding: 15px;
    }

    .btn-primary {
        background-color: #3498db;
        border: none;
        padding: 12px 30px;
        font-size: 1.1em;
        transition: all 0.3s ease;
    }

    .btn-primary:hover {
        background-color: #2980b9;
        transform: scale(1.05);
    }

    /* Counter display styles */
    .counter-display {
        background-color: #f8f9fa;
        border-left: 4px solid #28a745;
    }

    .progress {
        height: 10px;
        border-radius: 5px;
    }
</style>

<script>
    let startTime = Date.now();

    function startTimer(duration) {
        let timer = duration;
        const display = document.getElementById('timer');

        const countdown = setInterval(function () {
            const minutes = parseInt(timer / 60, 10);
            const seconds = parseInt(timer % 60, 10);

            display.textContent = minutes + ":" + (seconds < 10 ? "0" : "") + seconds;

            if (--timer < 0) {
                clearInterval(countdown);
                document.querySelector("form").submit();
            }
        }, 1000);
    }

    document.querySelector('form').addEventListener('submit', function() {
        const endTime = Date.now();
        const timeSpent = Math.floor((endTime - startTime) / 1000);
        document.getElementById('completionTime').value = timeSpent;
    });

    // Start timer when page loads
    startTimer({{ time_limit_seconds }});

    // Live validation for the numbers input
    const numbersInput = document.getElementById('numbers-input');
    const enteredCountEl = document.getElementById('entered-count');
    const correctCountEl = document.getElementById('correct-count');
    const progressBar = document.getElementById('progress-bar');

    // The expected correct order (descending from 99 to 0)
    const correctOrder = Array.from({length: 100}, (_, i) => 99 - i);

    function validateInput() {
        const inputText = numbersInput.value.trim();

        if (!inputText) {
            enteredCountEl.textContent = "0";
            correctCountEl.textContent = "0";
            progressBar.style.width = "0%";
            return;
        }

        // Split by commas and clean up each entry
        const enteredNumbers = inputText.split(',').map(n => parseInt(n.trim()));

        // Count valid numbers (filter out NaN)
        const validNumbers = enteredNumbers.filter(n => !isNaN(n));
        enteredCountEl.textContent = validNumbers.length;

        // Count correct positions
        let correctCount = 0;
        for (let i = 0; i < Math.min(validNumbers.length, correctOrder.length); i++) {
            if (validNumbers[i] === correctOrder[i]) {
                correctCount++;
            }
        }

        correctCountEl.textContent = correctCount;

        // Update progress bar
        const percentage = (validNumbers.length / 100) * 100;
        progressBar.style.width = `${percentage}%`;

        // Change color based on percentage of correct answers
        const correctPercentage = (correctCount / validNumbers.length) * 100 || 0;
        if (correctPercentage > 90) {
            progressBar.className = "progress-bar bg-success";
        } else if (correctPercentage > 50) {
            progressBar.className = "progress-bar bg-warning";
        } else {
            progressBar.className = "progress-bar bg-danger";
        }
    }

    // Add event listeners
    numbersInput.addEventListener('input', validateInput);
    numbersInput.addEventListener('paste', function() {
        // Use setTimeout to allow the paste operation to complete
        setTimeout(validateInput, 10);
    });
</script>
{% endblock %}
```

# numbertype_task\Results.html

```html
{% extends "global/Page.html" %}
{% block title %}Number Challenge - Results{% endblock %}

{% block content %}
<div class="card">
    <div class="card-body text-center">
        <h3 class="mb-4">Challenge Complete!</h3>

        <p class="text-muted">There were 100 numbers in total!</p> <!-- ✅ Added sentence here -->

        <div class="result-box">
            <div class="result-label">Your Score</div>
            <div class="result-value">
                {{ correct_count }} correct out of 100
            </div>
            <!-- ADD THIS NEW DIV HERE -->
            <div class="completion-time">
                Completed in {{ completion_time }} seconds
            </div>
        </div>

        <div class="mt-4">
            {% next_button %}
        </div>
    </div>
</div>

<style>
    .card {
        max-width: 600px;
        margin: 50px auto;
        border: none;
        box-shadow: 0 0 20px rgba(0,0,0,0.1);
    }

    .result-box {
        background: #f8f9fa;
        padding: 30px;
        border-radius: 10px;
        margin: 20px 0;
    }

    .result-label {
        font-size: 1.2em;
        color: #666;
        margin-bottom: 10px;
    }

    .result-value {
        font-size: 3em;
        font-weight: bold;
        color: #2c3e50;
    }

    /* ADD THIS NEW CSS CLASS HERE */
    .completion-time {
        margin-top: 15px;
        color: #666;
        font-size: 1.1em;
    }
</style>
{% endblock %}
```

# patternsorting_task\__init__.py

```py
from otree.api import *

class Constants(BaseConstants):
    name_in_url = 'colorsorting_task'
    players_per_group = None
    num_rounds = 1
    timeout_seconds = 120
    colors = ['Red', 'Blue', 'Green', 'Yellow', 'Orange', 'Purple']

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

    @staticmethod
    def is_displayed(player):
        # ✅ If the player quit, they should not see this task
        return not player.participant.vars.get('finished', False)

    @staticmethod
    def before_next_page(player, timeout_happened):
        if player.participant.vars.get('quit', False):
            try:
                end_index = player.session.config['app_sequence'].index('End')  # 🚀 Locate "End"
                player.participant._index_in_pages = end_index  # ✅ Move directly to "End"
            except ValueError:
                player.participant._index_in_pages = len(player.session.config['app_sequence'])  # Fallback

            player.participant.vars['finished'] = True  # ✅ Ensures future pages recognize quitting
            raise StopIteration  # 🚀 **FORCE QUITTING IMMEDIATELY**

    def vars_for_template(self):
        import random
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
```

# patternsorting_task\PatternSortingTask.html

```html
{% extends "global/Page.html" %}
{% block title %}Pattern Sorting Challenge{% endblock %}

{% block content %}
<div class="card">
    <div class="card-body text-center">
        <h3 class="mb-4">Sort the Patterns</h3>
        <p>Drag and drop the patterns into their correct categories.</p>

        <div class="patterns-container">
            {% for pattern in unique_patterns %}
            <div class="pattern-box draggable" id="pattern{{ forloop.counter }}" draggable="true" data-pattern="{{ pattern }}">
                <div class="pattern {{ pattern }}"></div>
            </div>
            {% endfor %}
        </div>

        <div class="drop-zone-container">
            <div class="drop-zone" data-category="Stripes">Stripes</div>
            <div class="drop-zone" data-category="Checkerboard">Checkerboard</div>
            <div class="drop-zone" data-category="Dots">Polka Dots</div>
            <div class="drop-zone" data-category="Waves">Waves</div>
            <div class="drop-zone" data-category="Zigzag">Zigzag</div>
        </div>
    </div>
</div>

<style>
    .card {
        max-width: 900px;
        margin: 30px auto;
        border: none;
        box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
    }
    .patterns-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 15px;
        margin: 20px 0;
    }
    .pattern-box {
        width: 100px;
        height: 100px;
        border: 2px solid #333;
        cursor: grab;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .drop-zone-container {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-top: 20px;
    }
    .drop-zone {
        width: 120px;
        height: 120px;
        border: 2px dashed #aaa;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        color: #555;
        background-color: #f8f9fa;
    }

    /* CSS Patterns */
    .Stripes {
        background: repeating-linear-gradient(45deg, #ff6b6b, #ff6b6b 10px, #f8f9fa 10px, #f8f9fa 20px);
    }
    .Checkerboard {
        background: repeating-linear-gradient(45deg, #3498db, #3498db 25px, #f8f9fa 25px, #f8f9fa 50px);
    }
    .Dots {
        background: radial-gradient(#ffbe76 10%, transparent 20%), #f8f9fa;
        background-size: 20px 20px;
    }
    .Waves {
        background: repeating-linear-gradient(90deg, #6ab04c, #6ab04c 10px, #f8f9fa 10px, #f8f9fa 20px);
    }
    .Zigzag {
        background: repeating-linear-gradient(135deg, #e056fd, #e056fd 10px, #f8f9fa 10px, #f8f9fa 20px);
    }
</style>

<script>
    document.querySelectorAll('.draggable').forEach(item => {
        item.addEventListener('dragstart', event => {
            event.dataTransfer.setData('text', event.target.dataset.pattern);
        });
    });

    document.querySelectorAll('.drop-zone').forEach(zone => {
        zone.addEventListener('dragover', event => event.preventDefault());
        zone.addEventListener('drop', event => {
            event.preventDefault();
            let patternType = event.dataTransfer.getData('text');
            let correctCategory = event.target.dataset.category;
            if (patternType.includes(correctCategory)) {
                event.target.style.backgroundColor = '#d4edda';
                event.target.innerHTML = '✔ Sorted';
            } else {
                event.target.style.backgroundColor = '#f8d7da';
                event.target.innerHTML = '❌ Wrong';
            }
        });
    });
</script>
{% endblock %}

```

# patternsorting_task\Results.html

```html
{% extends "global/Page.html" %}
{% block title %}Color Sorting Challenge - Results{% endblock %}

{% block content %}
<div class="card">
    <div class="card-body text-center">
        <h3 class="mb-4">Challenge Complete!</h3>

        <p class="text-muted">There were 100 numbers in total!</p>

        <div class="result-box">
            <div class="result-label">Your Performance</div>
            <div class="result-value">
                {{ correct_count }} out of {{ total_blocks }} blocks correctly sorted
            </div>
            <div class="result-details">
                Completed in {{ completion_time }} seconds
            </div>
        </div>

        <div class="mt-4">
    {% next_button %}
</div>

        {% if show_quit_option %}
<div class="quit-section mt-4">
    <h4>⚠️ <strong> Important Notice </strong></h4>
    <p>If you wish, you have the option to end your participation now. You will still receive payment for the rounds you have completed so far.</p>
    <button id="quit-button" class="btn btn-warning">Quit Now</button>
</div>
        {% endif %}

        {% if show_quit_option %}
<script>
    document.getElementById('quit-button').addEventListener('click', function() {
        liveSend({ action: 'quit' }).then(response => {
            if (response[Object.keys(response)[0]].quit_status === 'success') {
                window.location.href = "/End/";  // ✅ Redirect to End Page
            }
        });
    });
</script>
    {% endif %}
    </div>
</div>

<style>
    .card {
        max-width: 600px;
        margin: 50px auto;
        border: none;
        box-shadow: 0 0 20px rgba(0,0,0,0.1);
    }

    .result-box {
        background: #f8f9fa;
        padding: 30px;
        border-radius: 10px;
        margin: 20px 0;
    }

    .result-label {
        font-size: 1.2em;
        color: #666;
        margin-bottom: 10px;
    }

    .result-value {
        font-size: 3em;
        font-weight: bold;
        color: #2c3e50;
    }

    .result-details {
        margin-top: 15px;
        color: #666;
        font-size: 1.1em;
    }
</style>
{% endblock %}
```

# payment_info\__init__.py

```py
from otree.api import *



doc = """
This application provides a webpage instructing participants how to get paid.
Examples are given for the lab and Amazon Mechanical Turk (AMT).
"""


class C(BaseConstants):
    NAME_IN_URL = 'payment_info'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# FUNCTIONS
# PAGES
class PaymentInfo(Page):
    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        return dict(redemption_code=participant.label or participant.code)


page_sequence = [PaymentInfo]

```

# payment_info\PaymentInfo.html

```html
{{ block title }}Thank you{{ endblock }}
{{ block content }}

    <p>
        <em>Below are examples of messages that could be displayed for different experimental settings.</em>
    </p>

    <div class="panel panel-default" style="margin-bottom:10px">
        <div class="panel-body">
            <p><b>Laboratory:</b></p>
            <p>Please remain seated until your number is called. Then take your number card, and proceed to the cashier.</p>
            <p><em>Note: For the cashier in the laboratory, oTree can print a list of payments for all participants as a PDF.</em></p>
        </div>
    </div>

    <div class="panel panel-default" style="margin-bottom:10px">
        <div class="panel-body">
            <p><b>Classroom:</b></p>
            <p><em>If you want to keep track of how students did, the easiest thing is to assign the starting links to students by name.
                It is even possible to give each student a single permanent link for a whole semester using Rooms;
                so no need to waste time in each lecture with handing out new links and keeping track of which student uses which link.
                Alternatively, you may just give
                students anonymous links or secret nicknames.</em>
            </p>
        </div>
    </div>


{{ endblock }}


```

# Procfile

```
web: otree prodserver1of2 
worker: otree prodserver2of2 

```

# quit\__init__.py

```py
from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'quit'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]

```

# quit\MyPage.html

```html
{{ block title }}
    Page title
{{ endblock }}
{{ block content }}

    {{ formfields }}
    {{ next_button }}

{{ endblock }}

```

# quit\Results.html

```html
{{ block title }}
    Page title
{{ endblock }}

{{ block content }}

    {{ next_button }}
{{ endblock }}



```

# requirements.txt

```txt
otree
psycopg2-binary 
whitenoise 

```

# settings.py

```py
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
            #'colorsorting_task',
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

```

# slider_task\__init__.py

```py
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
```

# slider_task\Results.html

```html
{% extends "global/Page.html" %}
{% block title %}Slider Challenge - Complete{% endblock %}

{% block content %}
<div class="card">
    <div class="card-body text-center">
        <h3 class="mb-4">Challenge Complete!</h3>

        <div class="result-box">
            <div class="result-label">Your Performance</div>
            <div class="result-value">
                {{ correct_sliders }} out of {{ total_sliders }} sliders
            </div>
            <div class="result-details">
                correctly positioned at {{ target_value }}
            </div>
            <div class="result-details">
                Completed in {{ completion_time }} seconds
            </div>
        </div>

        <div class="mt-4">
            {{ next_button }}
        </div>
    </div>
</div>

<style>
    .card {
        max-width: 600px;
        margin: 50px auto;
        border: none;
        box-shadow: 0 0 20px rgba(0,0,0,0.1);
    }

    .result-box {
        background: #f8f9fa;
        padding: 30px;
        border-radius: 10px;
        margin: 20px 0;
    }

    .result-label {
        font-size: 1.2em;
        color: #666;
        margin-bottom: 10px;
    }

    .result-value {
        font-size: 3em;
        font-weight: bold;
        color: #2c3e50;
    }

    .result-details {
        margin-top: 15px;
        color: #666;
        font-size: 1.1em;
    }
</style>
{% endblock %}
```

# slider_task\SliderTask.html

```html
{% extends "global/Page.html" %}
{% block app_styles %}
<style>
    .otree-timer {
        display: none;
    }
</style>
{% endblock %}

{% block title %}Slider Challenge{% endblock %}

{% block content %}
<div class="card">
    <div class="card-body">
        <!-- Instructions Section -->
        <div class="instructions-section mb-4">
            <h3 class="text-center mb-3">Slider Challenge</h3>
            <div class="alert alert-info">
                <h5>Instructions:</h5>
                <ul class="mb-0">
                    <li><strong>The timer has already started!</strong></li>
                    <li>You have <strong>2 minutes</strong> to complete this task</li>
                    <li>You will see <strong>48 sliders</strong> positioned at random values</li>
                    <li>Your objective is to correctly position <strong>as many sliders as possible</strong> to exactly <strong>{{ target_value }}</strong></li>
                    <li>Your ranking will be determined by the number of sliders you correctly position</li>
                    <li>The more sliders you correctly position compared to other participants, the higher your ranking</li>
                    <li>Each correctly positioned slider counts as one point</li>
                    <li>You can submit your answers at any time using the button below</li>
                    <li>🏆 Remember: This is a competition! The top 10% of performers will receive an additional £0.50</li>
                    <li>🎲 In case of ties (where multiple participants achieve the same score), rankings will be determined randomly among those tied</li>
                </ul>
            </div>
        </div>

        <!-- Timer and Score -->
        <div class="stats-container mb-4">
            <div class="stat-box">
                <div class="stat-label">Time Remaining</div>
                <div class="stat-value" id="timer">1:00</div>
            </div>
            <div class="stat-box">
                <div class="stat-label">Correct Sliders</div>
                <div class="stat-value" id="correct-count">0</div>
            </div>
        </div>

        <!-- Sliders Container -->
        <div class="sliders-container">
            {% for position in random_positions %}
            <div class="slider-unit">
                <input type="range"
                       min="0"
                       max="100"
                       value="{{ position }}"
                       class="form-range slider"
                       id="slider{{ forloop.counter }}">
                <span class="value-display">{{ position }}</span>
            </div>
            {% endfor %}
        </div>

        <form id="form" method="post">
            <input type="hidden" name="correct_sliders" id="correct_sliders" value="0">
            <input type="hidden" name="completion_time" id="completion_time" value="0">
            <div class="text-center mt-4">
                <button type="submit" class="btn btn-primary btn-lg">Submit Results</button>
            </div>
        </form>
    </div>
</div>

<style>
    .card {
        max-width: 1000px;
        margin: 0 auto;
        border: none;
        box-shadow: 0 0 20px rgba(0,0,0,0.1);
    }

    .alert-info {
        background-color: #f8f9fa;
        border-left: 4px solid #3498db;
        border-radius: 0;
    }

    .alert-info ul {
        list-style-type: none;
        padding-left: 0;
    }

    .alert-info li {
        margin-bottom: 8px;
        position: relative;
        padding-left: 20px;
    }

    .alert-info li:before {
        content: "•";
        color: #3498db;
        position: absolute;
        left: 0;
    }

    .stats-container {
        display: flex;
        justify-content: center;
        gap: 40px;
        margin: 20px 0;
    }

    .stat-box {
        background: #f8f9fa;
        padding: 15px 25px;
        border-radius: 10px;
        min-width: 150px;
        text-align: center;
    }

    .stat-label {
        font-size: 0.9em;
        color: #666;
        text-transform: uppercase;
        margin-bottom: 5px;
    }

    .stat-value {
        font-size: 1.8em;
        font-weight: bold;
        color: #2c3e50;
    }

    .sliders-container {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
        gap: 15px;
        margin: 20px 0;
        padding: 20px;
        background: #f8f9fa;
        border-radius: 10px;
    }

    .slider-unit {
        padding: 10px;
        background: white;
        border: 1px solid #e1e1e1;
        border-radius: 8px;
        transition: transform 0.2s ease;
    }

    .slider-unit:hover {
        transform: scale(1.02);
    }

    .value-display {
        display: inline-block;
        min-width: 40px;
        text-align: center;
        font-weight: bold;
        color: #2c3e50;
        margin-top: 5px;
    }

    .form-range {
        width: 100%;
    }

    .btn-primary {
        background-color: #3498db;
        border: none;
        padding: 12px 30px;
        font-size: 1.1em;
        transition: all 0.3s ease;
    }

    .btn-primary:hover {
        background-color: #2980b9;
        transform: scale(1.05);
    }

    /* Customize the slider appearance */
    input[type="range"] {
        -webkit-appearance: none;
        height: 8px;
        background: #dfe6e9;
        border-radius: 4px;
        outline: none;
    }

    input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        width: 20px;
        height: 20px;
        background: #3498db;
        border-radius: 50%;
        cursor: pointer;
        transition: background .15s ease-in-out;
    }

    input[type="range"]::-webkit-slider-thumb:hover {
        background: #2980b9;
    }
</style>

<script>
    let startTime = new Date().getTime();
    const targetValue = {{ target_value }};
    const sliders = document.querySelectorAll('.slider');
    const displays = document.querySelectorAll('.value-display');
    const correctCountDisplay = document.getElementById('correct-count');

    sliders.forEach((slider, index) => {
        slider.addEventListener('input', function() {
            displays[index].textContent = this.value;
            updateCorrectCount();
        });
    });

    function updateCorrectCount() {
        const correct = Array.from(sliders).filter(slider =>
            parseInt(slider.value) === targetValue
        ).length;
        document.getElementById('correct_sliders').value = correct;
        correctCountDisplay.textContent = correct;
    }

    document.getElementById('form').addEventListener('submit', function() {
    const endTime = new Date().getTime();
    let elapsedTime = Math.round((endTime - startTime) / 1000);
    let correctSliders = parseInt(document.getElementById('correct_sliders').value) || 0;

    document.getElementById('completion_time').value = elapsedTime;
    document.getElementById('correct_sliders').value = correctSliders;
});

    function updateTimer(duration) {
        const timerDisplay = document.getElementById('timer');
        let timeLeft = duration;

        const timer = setInterval(() => {
            const minutes = Math.floor(timeLeft / 60);
            const seconds = timeLeft % 60;

            timerDisplay.textContent = `${minutes}:${seconds.toString().padStart(2, '0')}`;

            if (--timeLeft < 0) {
                clearInterval(timer);
                // Set the completion time to the full duration
                document.getElementById('completion_time').value = {{ timeout_seconds }};
                document.getElementById('form').submit();
            }
        }, 1000);
    }

    updateTimer({{ timeout_seconds }});
</script>
{% endblock %}
```

# survey\__init__.py

```py
from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(label='What is your age?', min=13, max=125)
    gender = models.StringField(
        choices=[['Male', 'Male'], ['Female', 'Female']],
        label='What is your gender?',
        widget=widgets.RadioSelect,
    )
    crt_bat = models.IntegerField(
        label='''
        A bat and a ball cost 22 dollars in total.
        The bat costs 20 dollars more than the ball.
        How many dollars does the ball cost?'''
    )
    crt_widget = models.IntegerField(
        label='''
        If it takes 5 machines 5 minutes to make 5 widgets,
        how many minutes would it take 100 machines to make 100 widgets?
        '''
    )
    crt_lake = models.IntegerField(
        label='''
        In a lake, there is a patch of lily pads.
        Every day, the patch doubles in size.
        If it takes 48 days for the patch to cover the entire lake,
        how many days would it take for the patch to cover half of the lake?
        '''
    )


# FUNCTIONS
# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender']


class CognitiveReflectionTest(Page):
    form_model = 'player'
    form_fields = ['crt_bat', 'crt_widget', 'crt_lake']


page_sequence = [Demographics, CognitiveReflectionTest]

```

# survey\CognitiveReflectionTest.html

```html
{{ block title }}Survey{{ endblock }}
{{ block content }}

    <p>
        Please answer the following questions.
    </p>

    {{ formfields }}

    {{ next_button }}

{{ endblock }}

```

# survey\Demographics.html

```html
{{ block title }}Survey{{ endblock }}
{{ block content }}

    <p>
        Please answer the following questions.
    </p>

    {{ formfields }}

    {{ next_button }}

{{ endblock }}

```

# trivia_task\__init__.py

```py
from otree.api import *


class Constants(BaseConstants):
    name_in_url = 'trivia_task'
    players_per_group = None
    num_rounds = 1
    time_limit_seconds = 3 * 60  # 3 minutes
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
    completion_time = models.IntegerField(initial=0)


class TriviaTask(Page):
    form_model = 'player'
    form_fields = ['answers_json', 'completion_time']
    timeout_seconds = Constants.time_limit_seconds

    @staticmethod
    def vars_for_template(player: Player):
        import random
        return {
            'questions': random.sample(Constants.questions, len(Constants.questions)),
        }

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            player.completion_time = Constants.time_limit_seconds

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
            'total_questions': len(Constants.questions),
            'completion_time': player.completion_time
        }


page_sequence = [TriviaTask, TriviaResults]
```

# trivia_task\Trivia_Results.html

```html
{% extends "global/Page.html" %}
{% block title %}Trivia Challenge - Results{% endblock %}

{% block content %}
<div class="card">
    <div class="card-body text-center">
        <h3 class="mb-4">Challenge Complete!</h3>

        <div class="result-box">
            <div class="result-label">Your Score</div>
            <div class="result-value">
                {{ correct_answers }} correct out of 12
            </div>

            <div class="completion-time">
                Completed in {{ completion_time }} seconds
            </div>
        </div>

        <div class="mt-4">
            {% next_button %}
        </div>
    </div>
</div>

<style>
    .completion-time {
        margin-top: 15px;
        color: #666;
        font-size: 1.1em;
    }
    .card {
        max-width: 600px;
        margin: 50px auto;
        border: none;
        box-shadow: 0 0 20px rgba(0,0,0,0.1);
    }

    .result-box {
        background: #f8f9fa;
        padding: 30px;
        border-radius: 10px;
        margin: 20px 0;
    }

    .result-label {
        font-size: 1.2em;
        color: #666;
        margin-bottom: 10px;
    }

    .result-value {
        font-size: 3em;
        font-weight: bold;
        color: #2c3e50;
    }
</style>
{% endblock %}
```

# trivia_task\TriviaTask.html

```html
{% extends "global/Page.html" %}
{% block app_styles %}
<style>
    .otree-timer {
        display: none;
    }
</style>
{% endblock %}
{% block content %}
<div class="card">
    <div class="card-body">
        <div class="instructions-section mb-4">
            <h3 class="text-center mb-3">Trivia Challenge</h3>
            <div class="alert alert-info">
                <h5>Instructions:</h5>
                <ul class="mb-0">
                    <li><strong>The timer has already started!</strong></li>
                    <li>You have <strong>3 minutes</strong> to answer all questions</li>
                    <li>Your objective is to answer <strong>as many questions correctly as possible</strong></li>
                    <li>Your ranking will be determined by the number of correct answers you provide</li>
                    <li>The more questions you answer correctly compared to other participants, the higher your ranking</li>
                    <li>Questions include multiple choice and true/false</li>
                    <li>You can submit your answers at any time using the button at the bottom</li>
                    <li>🏆 Remember: This is a competition! The top 10% of performers will receive an additional £0.50</li>
                    <li>🎲 In case of ties (where multiple participants achieve the same score), rankings will be determined randomly among those tied</li>
                </ul>
            </div>

            <div class="alert alert-warning mt-3">
                <h5>⚠️ Important Warning:</h5>
                <p class="mb-0"><strong>Please do not switch tabs or leave this page during the challenge.</strong> Navigating away from this page may be flagged as an attempt to search for answers online, which could result in your participation being disqualified. Stay on this page until you've completed all questions.</p>
            </div>

        </div>

        <div class="timer-container text-center mb-4">
            <div class="stat-box">
                <span class="stat-label">Time Remaining:</span>
                <span class="stat-value" id="timer">3:00</span>
            </div>
        </div>

        <form method="post">
            <input type="hidden" name="answers_json" id="answers_json" value="{}">
            <input type="hidden" name="completion_time" id="completion_time" value="0">

            {% for question in questions %}
            <div class="question-container mb-4">
                <div class="question-header">
                    Question {{ forloop.counter }} of 12
                </div>
                <div class="question-text">
                    {{ question.question }}
                </div>
                <div class="options-container">
                    {% for choice in question.choices %}
                    <div class="option">
                        <label>
                            <input type="radio"
                                   name="question_{{ question.question }}"
                                   value="{{ choice }}"
                                   onclick="recordAnswer('{{ question.question }}','{{ choice }}')"
                            >
                            {{ choice }}
                        </label>
                    </div>
                    {% endfor %}
                </div>
            </div>
            {% endfor %}

            <div class="text-center mt-4">
                {% next_button %}
            </div>
        </form>
    </div>
</div>

<style>
    .card {
        max-width: 800px;
        margin: 0 auto;
        border: none;
        box-shadow: 0 0 20px rgba(0,0,0,0.1);
    }

    .alert-info {
        background-color: #f8f9fa;
        border-left: 4px solid #3498db;
        border-radius: 0;
    }

    .alert-info ul {
        list-style-type: none;
        padding-left: 0;
    }

    .alert-info li {
        margin-bottom: 8px;
        position: relative;
        padding-left: 20px;
    }

    .alert-info li:before {
        content: "•";
        color: #3498db;
        position: absolute;
        left: 0;
    }

    .timer-container {
        position: sticky;
        top: 0;
        background: white;
        padding: 10px;
        z-index: 100;
    }

    .stat-box {
        background: #f8f9fa;
        padding: 15px 25px;
        border-radius: 10px;
        display: inline-block;
    }

    .stat-value {
        font-size: 1.5em;
        font-weight: bold;
        color: #2c3e50;
        margin: 0 10px;
    }

    .question-container {
        background: #fff;
        border: 1px solid #e1e1e1;
        border-radius: 8px;
        padding: 20px;
    }

    .question-header {
        color: #666;
        font-size: 0.9em;
        margin-bottom: 10px;
    }

    .question-text {
        font-size: 1.1em;
        margin-bottom: 15px;
        font-weight: 500;
    }

    .option {
        padding: 10px;
        background: #f8f9fa;
        border-radius: 5px;
        transition: background-color 0.2s;
        margin-bottom: 5px;
    }

    .option:hover {
        background: #e9ecef;
    }

    .option label {
        display: block;
        margin: 0;
        cursor: pointer;
    }

    .btn-primary {
        background-color: #3498db;
        border: none;
        padding: 12px 30px;
        font-size: 1.1em;
        margin-right: 10px;
    }
</style>

<script>
    let answersObj = {};
    const startTime = Date.now();  // Add this line

    function recordAnswer(questionText, chosenOption) {
        answersObj[questionText] = chosenOption;
        document.getElementById("answers_json").value = JSON.stringify(answersObj);
    }

    // Add this function to handle form submission
    document.querySelector('form').addEventListener('submit', function() {
        const endTime = Date.now();
        const timeSpent = Math.round((endTime - startTime) / 1000);
        document.getElementById('completion_time').value = timeSpent;
    });

    function startTimer(duration) {
        let timer = duration;
        const display = document.getElementById('timer');

        const countdown = setInterval(function () {
            const minutes = parseInt(timer / 60, 10);
            const seconds = parseInt(timer % 60, 10);

            display.textContent = minutes + ":" + (seconds < 10 ? "0" : "") + seconds;

            if (--timer < 0) {
                clearInterval(countdown);
                // Set the completion time to full duration on timeout (3 minutes = 180 seconds)
                document.getElementById('completion_time').value = 180;  // Hardcoded value
                document.querySelector("form").submit();
            }
        }, 1000);
    }

    startTimer(3 * 60);
</script>
{% endblock %}
```

# verification_task\__init__.py

```py
# verification_task/__init__.py
from otree.api import *


class Constants(BaseConstants):
    name_in_url = 'verification_task'
    players_per_group = None
    num_rounds = 1
    timeout_seconds = 120  # 2 minutes
    grid_size = 16  # 4x4 grid
    required_rounds = 5  # Number of grids they need to complete

    # Define verification challenges
    verification_challenges = [
        {
            'prompt': "Click all squares that sum to exactly 10",
            'grid': [3, 7, 5, 2, 8, 1, 4, 6, 9, 0, 5, 8, 2, 4, 7, 3],
            'correct': [2, 7, 11, 15]  # Indices where correct answers are
        },
        {
            'prompt': "Click all squares containing an even number greater than 5",
            'grid': [2, 8, 3, 6, 1, 4, 10, 5, 7, 12, 9, 4, 8, 3, 6, 2],
            'correct': [1, 6, 9, 12]
        },
        {
            'prompt': "Click all squares where the number is a multiple of 3",
            'grid': [4, 9, 2, 6, 1, 3, 8, 12, 5, 15, 7, 9, 3, 6, 4, 18],
            'correct': [1, 3, 5, 7, 9, 11, 13, 15]
        },
        {
            'prompt': "Click all squares containing prime numbers",
            'grid': [4, 7, 9, 2, 11, 6, 13, 8, 15, 17, 10, 19, 12, 23, 16, 29],
            'correct': [1, 3, 4, 6, 9, 11, 13]
        },
        {
            'prompt': "Click all squares where the number is less than 5",
            'grid': [7, 2, 9, 4, 1, 6, 3, 8, 2, 10, 4, 7, 3, 5, 1, 8],
            'correct': [1, 4, 6, 8, 10, 12, 14]
        }
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    current_round = models.IntegerField(initial=0)
    correct_count = models.IntegerField(initial=0)
    completion_time = models.IntegerField(initial=0)
    quit_early = models.BooleanField(initial=False) # Change this to StringField with blank=True to allow empty submissions
    responses = models.StringField(blank=True)


class VerificationTask(Page):
    form_model = 'player'
    form_fields = ['responses', 'completion_time']

    @staticmethod
    def vars_for_template(player):
        import json  # Add this import
        return {
            'verification_challenges': json.dumps(Constants.verification_challenges),  # Convert to JSON string
            'timeout_seconds': Constants.timeout_seconds,
        }

    @staticmethod
    def is_displayed(player):
        return not player.participant.vars.get('finished', False)

    @staticmethod
    def before_next_page(player, timeout_happened):
        if timeout_happened:
            return

        if player.participant.vars.get('quit', False):
            try:
                end_index = player.session.config['app_sequence'].index('End')
                player.participant._index_in_pages = end_index
            except ValueError:
                player.participant._index_in_pages = len(player.session.config['app_sequence'])
            player.participant.vars['finished'] = True
            return

        # Process responses
        import json
        try:
            responses = json.loads(player.responses)
            # Calculate correct count based on responses
            player.correct_count = sum(1 for resp in responses
                                       if set(resp['selected']) == set(resp['correct']))
        except (json.JSONDecodeError, KeyError):
            player.correct_count = 0

class Results(Page):
    @staticmethod
    def vars_for_template(player):
        return {
            'correct_count': player.correct_count,
            'total_rounds': Constants.required_rounds,
            'completion_time': player.completion_time,
            'show_quit_option': player.session.config.get('quit_option', False)
        }

    @staticmethod
    def live_method(player, data):
        if data.get('action') == 'quit':
            player.participant.vars['quit'] = True
            player.participant.vars['finished'] = True
            player.quit_early = True
            try:
                end_index = player.session.config['app_sequence'].index('End')
                player.participant._index_in_pages = end_index
            except ValueError:
                player.participant._index_in_pages = len(player.session.config['app_sequence'])
            return {player.id_in_group: {'quit_status': 'success'}}

    @staticmethod
    def is_displayed(player):
        return not (player.participant.vars.get('finished', False) or player.participant.vars.get('quit', False))


page_sequence = [VerificationTask, Results]
```

# verification_task\Results.html

```html
{% extends "global/Page.html" %}
{% block title %}Verification Challenge - Results{% endblock %}

{% block content %}
<div class="card">
    <div class="card-body text-center">
        <h3 class="mb-4">Challenge Complete!</h3>

        <div class="result-box">
            <div class="result-label">Your Performance</div>
            <div class="result-value">
                {{ correct_count }} out of {{ total_rounds }} grids correctly completed
            </div>
            <div class="completion-time">
                Completed in {{ completion_time }} seconds
            </div>
        </div>

        {% if show_quit_option %}
        <div class="quit-section mt-4">
            <h4>⚠️ <strong> Important Notice </strong></h4>
            <p>If you wish, you have the option to end your participation now.
            You will still receive payment for the rounds you have completed so far.</p>
            <button id="quit-button" class="btn btn-warning">Quit Now</button>
        </div>
        {% endif %}

        <div class="mt-4">
            {% next_button %}
        </div>
    </div>
</div>

<style>
    .card {
        max-width: 600px;
        margin: 50px auto;
        border: none;
        box-shadow: 0 0 20px rgba(0,0,0,0.1);
    }

    .result-box {
        background: #f8f9fa;
        padding: 30px;
        border-radius: 10px;
        margin: 20px 0;
    }

    .result-label {
        font-size: 1.2em;
        color: #666;
        margin-bottom: 10px;
    }

    .result-value {
        font-size: 3em;
        font-weight: bold;
        color: #2c3e50;
    }

    .completion-time {
        margin-top: 15px;
        color: #666;
        font-size: 1.1em;
    }
</style>

{% if show_quit_option %}
<script>
    document.getElementById('quit-button').addEventListener('click', function() {
        liveSend({ action: 'quit' }).then(response => {
            if (response[Object.keys(response)[0]].quit_status === 'success') {
                window.location.href = "/End/";
            }
        });
    });
</script>
{% endif %}
{% endblock %}
```

# verification_task\VerificationTask.html

```html
{% extends "global/Page.html" %}
{% block title %}{% endblock %}

{% block content %}
<div class="card">
    <div class="card-body">
        <!-- Instructions Section -->
        <div class="instructions-section mb-4">
            <h3 class="text-center mb-3">Verification Challenge</h3>
            <div class="alert alert-info">
                <h5>Instructions:</h5>
                <ul class="mb-0">
                    <li>You will see <strong>5 different grids</strong> of numbers</li>
                    <li>For each grid, follow the specific instructions given</li>
                    <li>Click the squares that match the criteria</li>
                    <li>You have <strong>2 minutes</strong> to complete all grids</li>
                </ul>
            </div>
        </div>

        <!-- Timer -->
        <div class="timer-container text-center mb-4">
            <div class="stat-box">
                <span class="stat-label">Time Remaining:</span>
                <span class="stat-value" id="timer">2:00</span>
            </div>
        </div>

        <!-- Progress Display -->
        <div class="progress-display text-center mb-4">
            <div class="stat-box">
                <span class="stat-label">Grid</span>
                <span class="stat-value"><span id="current-round">1</span> of 5</span>
            </div>
        </div>

        <!-- Challenge Prompt -->
        <div class="challenge-prompt alert alert-primary mb-4" id="current-prompt">
            Click to start the first challenge
        </div>

        <!-- Grid Container -->
        <div class="grid-container mb-4">
            <div class="verification-grid" id="grid">
                <!-- Grid will be populated by JavaScript -->
            </div>
        </div>

        <!-- Next Button -->
        <div class="text-center mb-4">
            <button id="next-grid" class="btn btn-primary" disabled>
                Verify and Continue
            </button>
        </div>

        <form id="completion-form" method="post" style="display: none;">
            <input type="hidden" name="responses" id="responses">
            <input type="hidden" name="completion_time" id="completion_time">
        </form>
    </div>
</div>

<style>
    .card {
        max-width: 800px;
        margin: 30px auto;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }

    .verification-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 10px;
        max-width: 500px;
        margin: 0 auto;
    }

    .grid-square {
        aspect-ratio: 1;
        background: #f8f9fa;
        border: 2px solid #dee2e6;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.5rem;
        font-weight: bold;
        color: #2c3e50;
        cursor: pointer;
        transition: all 0.2s ease;
    }

    .grid-square:hover {
        border-color: #3498db;
        transform: scale(1.02);
    }

    .grid-square.selected {
        background: #3498db;
        color: white;
        border-color: #2980b9;
    }

    .challenge-prompt {
        font-size: 1.2rem;
        font-weight: 500;
        text-align: center;
    }

    .btn-primary {
        background-color: #3498db;
        border: none;
        padding: 12px 30px;
        font-size: 1.1rem;
        transition: all 0.3s ease;
    }

    .btn-primary:hover:not(:disabled) {
        background-color: #2980b9;
        transform: scale(1.05);
    }

    .btn-primary:disabled {
        background-color: #bdc3c7;
        cursor: not-allowed;
    }

    .stat-box {
        background: #f8f9fa;
        padding: 15px 25px;
        border-radius: 10px;
        display: inline-block;
    }

    .stat-label {
        font-size: 0.9em;
        color: #666;
        margin-right: 10px;
    }

    .stat-value {
        font-size: 1.5em;
        font-weight: bold;
        color: #2c3e50;
    }
</style>

<script>
    let currentRound = 0;
    let startTime = Date.now();
    let challenges = JSON.parse('{{ verification_challenges|safe }}');  // Parse the JSON string
    let selectedSquares = new Set();

    function initializeGrid() {
        currentRound++;
        document.getElementById('current-round').textContent = currentRound;
        selectedSquares.clear();

        const challenge = challenges[currentRound - 1];
        document.getElementById('current-prompt').textContent = challenge.prompt;

        const grid = document.getElementById('grid');
        grid.innerHTML = '';

        challenge.grid.forEach((num, index) => {
            const square = document.createElement('div');
            square.className = 'grid-square';
            square.dataset.index = index;
            square.textContent = num;
            square.onclick = () => toggleSquare(square);
            grid.appendChild(square);
        });

        document.getElementById('next-grid').disabled = false;
    }

    function toggleSquare(square) {
        const index = parseInt(square.dataset.index);
        if (selectedSquares.has(index)) {
            selectedSquares.delete(index);
            square.classList.remove('selected');
        } else {
            selectedSquares.add(index);
            square.classList.add('selected');
        }
    }

    let allResponses = [];  // Array to store all round responses

document.getElementById('next-grid').addEventListener('click', () => {
    const responseData = {
        round: currentRound,
        selected: Array.from(selectedSquares),
        correct: challenges[currentRound - 1].correct
    };

    allResponses.push(responseData);  // Store this round's response

    if (currentRound < 5) {
        initializeGrid();
    } else {
        // Submit all responses at once
        document.getElementById('responses').value = JSON.stringify(allResponses);
        document.getElementById('completion_time').value =
            Math.floor((Date.now() - startTime) / 1000);
        document.getElementById('completion-form').submit();
    }
});

    let globalTimer = null;  // Store timer reference

function startTimer(duration) {
    if (globalTimer) {  // If timer exists, don't create a new one
        return;
    }

    let timer = duration;
    const display = document.getElementById('timer');

    globalTimer = setInterval(() => {
        const minutes = parseInt(timer / 60, 10);
        const seconds = parseInt(timer % 60, 10);

        display.textContent =
            minutes + ":" + (seconds < 10 ? "0" : "") + seconds;

        if (--timer < 0) {
            clearInterval(globalTimer);
            document.getElementById('completion-form').submit();
        }
    }, 1000);
}

    // Initialize first grid when page loads
    initializeGrid();
    startTimer({{ timeout_seconds }});
</script>
{% endblock %}
```

# welcome\__init__.py

```py
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
```

# welcome\Instructions.html

```html
{{ block title }}
    Page title
{{ endblock }}

{{ block content }}

    {{ next_button }}
{{ endblock }}



```

# welcome\Welcome.html

```html
{% extends "global/Page.html" %}
{% block title %}{% endblock %}

{% block content %}
<div class="card">
    <div class="card-body text-center">
        <h2 class="card-title mb-4">Welcome to the OCTAGON!</h2>

        <div class="welcome-text mb-5">
            <div class="instruction-section">
                <h3>📝 Study Overview</h3>
                <p>The Octagon is a study that consists of 8 competitive mini-games.</p>
            </div>

            <div class="instruction-section">
                <h3>⚙️ Game Structure</h3>
                    <p>Each game has specific instructions and a time limit displayed at the top of the page.</p>
                    <p>Games end either when completed or when time expires.</p>
                    <p>All games must be played in sequence and cannot be revisited.</p>
                    <p>Upcoming games remain hidden until reached.</p>
                    <p>If you are using a laptop, it is recommended that you use an external mouse rather than the built-in trackpad during the experiment.</p>
            </div>

            <div class="instruction-section">
                <h3>🎯 Your Objective</h3>
                <p>Maximize your score in each game through accurate and focused performance.</p>
                <p>To ensure the validity of the study please stay engaged. If you stay inactive for too long, you will not be able to continue, and your participation may not count.</p>
            </div>

            <div class="instruction-section">
                <h3>📜 Ranking & Results</h3>
                <p>Each game is a competition against other participants. Your performance in each game determines your ranking.</p>
                <p>At the end of each game, scores are recorded, and participants are ranked based on performance.</p>
                <p><b>Final Results:</b> Your overall ranking will be communicated one week after your participation.</p>
            </div>

            <div class="instruction-section">
                <h3>💰 Payment</h3>
                <p>You will receive <b>&pound;3</b> for entering the games, and additional pay based on your performance in the games.</p>
                <p>At the end of the study, a performance ranking for each game will be published. In each game, if you score in the <b>top 10%</b> of participants you will receive an additional <b>£0.50</b>. This means that high performance in multiple games can significantly increase your earnings!</p>
                <p>Example: If you rank in the top 10% for 2 of the 8 games, you would receive £3 (base) + £1 (bonuses) = £4 total. The maximum possible payment is £7 (if you rank in the top 10% for all games).</p>
                <p>The exact amount. alongside your ranking will be communicated one week after you participate in the games.</p>
            </div>

            {% if show_quit_info %}
                <div class="instruction-section important-notice">
                    <h3>⚠️ Important Notice</h3>
                    <p>After completing the 4th game, you will have the option to end your participation early.</p>
                    <p>You will receive performance-based payment for any games in which you have achieved the top 10%, <u>up to and including the game you decide to exit.</u></p>
                </div>
            {% endif %}

        <div class="instruction-section">
                <h3>🕐 TIMING NOTICE</h3>
                <p>Some games begin automatically upon loading, while other games start upon your first interaction with the game interface. Make sure to keep an eye on that timer!</p>
        </div>
        </div>
        <form method="post">
            <button class="btn btn-primary btn-lg start-button" type="submit">
                Let the Games begin !!
            </button>
        </form>
    </div>
</div>

<style>
    .card {
        max-width: 600px;
        margin: 50px auto;
        border: none;
        box-shadow: 0 0 20px rgba(0,0,0,0.1);
    }

    .card-title {
        color: #2c3e50;
        font-size: 2.5em;
    }

    .welcome-text {
        font-size: 1.2em;
        line-height: 1.6;
        color: #34495e;
    }

    .welcome-text p {
        margin-bottom: 15px;
    }

    .start-button {
        padding: 15px 50px;
        font-size: 1.3em;
        background-color: #3498db;
        border: none;
        transition: all 0.3s ease;
    }

    .start-button:hover {
        background-color: #2980b9;
        transform: scale(1.05);
    }

    /* INSERT HERE: Important Notice CSS */
    .important-notice {
        border: 3px solid #e63946;
        background-color: #ffebee;
        color: #b71c1c;
        padding: 15px;
        border-radius: 8px;
        margin: 20px 0;
    }

    .important-notice h3 {
        color: #b71c1c;
        font-weight: bold;
    }

    .important-notice p {
        font-weight: 600;
        margin-bottom: 10px;
    }

    .important-notice u {
        text-decoration-color: #e63946;
        text-decoration-thickness: 2px;
    }
</style>
{% endblock %}
```

