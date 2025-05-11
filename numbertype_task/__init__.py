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
