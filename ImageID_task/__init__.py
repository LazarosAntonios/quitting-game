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
            'options': ['Earthworm', 'Sea Cucumber', 'Naked Mole Rat', 'Blobfish', 'Axolotl', 'Goat', 'Cabbage Moth', 'Dung Beetle', 'Star-nosed Mole', 'Hammerhead Shark', 'Leopard Slug', 'Proboscis Monkey', 'Eagle', 'Narwhal', 'Amoeba', 'Coconut Crab', 'Tardigrade', 'Mudskipper', 'Sea Sponge', 'Pistol Shrimp', 'Blue Dragon Nudibranch', 'Lungfish', 'Fainting Goat', 'Manatee', 'Platypus', 'Giant Isopod', 'Hagfish', 'Shoebill Stork', 'Liger', 'Wombat', 'Sun Bear', 'Yeti Crab', 'Mimic Octopus', 'Frilled Lizard', 'Glass Frog', 'Zebra Turkeyfish', 'Japanese Spider Crab', 'Dumbo Octopus', 'Aye-Aye', 'Leafy Sea Dragon', 'Jerboa', 'Satanic Leaf-Tailed Gecko', 'Fossa', 'Goblin Shark', 'Okapi', 'Indian Purple Frog', 'Quokka', 'Giant Anteater', 'Tasmanian Devil'],
            'correct': 'Eagle'
        },
        {
            'name': 'Car2.png',
            'url': 'imageid_task/Car2.png',
            'question': 'What car brand is this?',
            'options': ['BMW', 'Mercedes-Benz', 'Audi', 'Porsche', 'Lamborghini', 'Maserati', 'Bentley', 'Rolls-Royce', 'Jaguar', 'Land Rover', 'Lexus', 'Toyota', 'Honda', 'Nissan', 'Mazda', 'Subaru', 'Volkswagen', 'Ford', 'Chevrolet', 'Dodge', 'Chrysler', 'Jeep', 'Hyundai', 'Kia', 'Volvo', 'Peugeot', 'Renault', 'Fiat', 'Alfa Romeo', 'Mini', 'Tesla', 'Smart', 'Acura', 'Infiniti', 'Cadillac', 'Lincoln', 'Buick', 'GMC', 'Ram', 'Pontiac', 'Saturn', 'DeLorean', 'Ferrari', 'McLaren', 'Aston Martin', 'Bugatti', 'Pagani', 'Koenigsegg', 'Lotus', 'Genesis'],
            'correct': 'Ferrari'
        },
        {
            'name': 'game.png',
            'url': 'imageid_task/game.png',
            'question': 'What board game is this?',
            'options': ['Chess', 'Checkers', 'Scrabble', 'Risk', 'Catan', 'Clue', 'Battleship', 'Sorry!', 'Monopoly', 'The Game of Life', 'Candy Land', 'Chutes and Ladders', 'Trivial Pursuit', 'Stratego', 'Axis & Allies', 'Carcassonne', 'Ticket to Ride', 'Pandemic', 'Codenames', 'Dominion', 'Azul', 'Twilight Struggle', 'Gloomhaven', '7 Wonders', 'Agricola', 'Power Grid', 'Small World', 'Eldritch Horror', 'Terra Mystica', 'Puerto Rico', 'King of Tokyo', 'Blood Rage', 'Tigris & Euphrates', 'Arkham Horror', 'Shogun', 'Through the Ages', 'Brass: Birmingham', 'Betrayal at House on the Hill', 'Caverna', 'Scythe', 'Dixit', 'Patchwork', 'Splendor', 'Jaipur', 'Camel Up', 'Hive', 'Tsuro', 'Hanabi', 'Love Letter', 'Telestrations'],
            'correct': 'Monopoly'
        },
        {
            'name': 'Band.png',
            'url': 'imageid_task/Band.png',
            'question': 'Which band is this?',
            'options': ['The Beatles', 'The Rolling Stones', 'Led Zeppelin', 'Pink Floyd', 'The Doors', 'The Who', 'The Kinks', 'Fleetwood Mac', 'Deep Purple', 'The Clash', 'The Smiths', 'The Cure', 'Joy Division', 'The Police', 'Talking Heads', 'Nirvana', 'Pearl Jam', 'Soundgarden', 'Alice in Chains', 'Foo Fighters', 'Radiohead', 'Coldplay', 'Muse', 'Arctic Monkeys', 'The Strokes', 'Red Hot Chili Peppers', 'Green Day', 'Blink-182', 'My Chemical Romance', 'Paramore', 'Metallica', 'Iron Maiden', 'Black Sabbath', 'Megadeth', 'Slayer', 'AC/DC', 'Guns N Roses', 'Aerosmith', 'Bon Jovi', 'Van Halen', 'The Eagles', 'The Beach Boys', 'The Byrds', 'The Velvet Underground', 'Genesis', 'Yes', 'King Crimson', 'Rush', 'Queen', 'ELO', 'Tame Impala', 'The National', 'The Smashing Pumpkins', 'The White Stripes', 'The Black Keys'],
            'correct': 'Queen'
        },
        {
            'name': 'Stadium.png',
            'url': 'imageid_task/Stadium.png',
            'question': 'Which NFL team plays in this stadium?',
            'options': ['Arizona Cardinals', 'Atlanta Falcons', 'Baltimore Ravens', 'Buffalo Bills', 'Carolina Panthers', 'Chicago Bears', 'Cincinnati Bengals', 'Cleveland Browns', 'Dallas Cowboys', 'Denver Broncos', 'Detroit Lions', 'Green Bay Packers', 'Houston Texans', 'Indianapolis Colts', 'Jacksonville Jaguars', 'Kansas City Chiefs', 'Las Vegas Raiders', 'Los Angeles Chargers', 'Los Angeles Rams', 'Miami Dolphins', 'Minnesota Vikings', 'New England Patriots', 'New Orleans Saints', 'New York Giants', 'New York Jets', 'Philadelphia Eagles', 'Pittsburgh Steelers', 'San Francisco 49ers', 'Seattle Seahawks', 'Tampa Bay Buccaneers', 'Tennessee Titans', 'Washington Commanders'],
            'correct': 'Minnesota Vikings'
        },
        {
            'name': 'trophy.png',
            'url': 'imageid_task/trophy.png',
            'question': 'What is the name of this award trophy?',
            'options': ['Golden Globe', 'Primetime Emmy Award', 'Daytime Emmy Award', 'Grammy Award', 'Tony Award', 'BAFTA Award', 'Screen Actors Guild (SAG) Award', 'Critics\' Choice Award', 'MTV Movie & TV Award', 'People\'s Choice Award', 'Independent Spirit Award', 'Cannes Palme d\'Or', 'Venice Film Festival Golden Lion', 'Berlin Film Festival Golden Bear', 'Goya Award', 'César Award', 'Hollywood Walk of Fame Star', 'Nickelodeon Kids\' Choice Award', 'BET Award', 'NAACP Image Award', 'Country Music Association (CMA) Award', 'Academy of Country Music (ACM) Award', 'Billboard Music Award', 'American Music Award', 'MTV Europe Music Award', 'Brit Award', 'Juno Award', 'Mercury Prize', 'Pulitzer Prize for Drama', 'Tony Award for Best Musical', 'Oscar', 'Golden Raspberry (Razzie) Award', 'Saturn Award', 'Hugo Award', 'Nebula Award', 'Clio Award', 'Peabody Award', 'Television Critics Association (TCA) Award', 'Drama Desk Award', 'Olivier Award', 'Hollywood Critics Association Award', 'Webby Award', 'Shorty Award', 'Streamy Award', 'Game Awards Trophy', 'Annie Award', 'Kidscreen Award', 'Producers Guild of America (PGA) Award', 'Writers Guild of America (WGA) Award', 'Directors Guild of America (DGA) Award'],
            'correct': 'Oscar'
        },
        {
            'name': 'Wonder.png',
            'url': 'imageid_task/Wonder.png',
            'question': 'Which Wonder of the World is this?',
            'options': ['Eiffel Tower', 'Statue of Liberty', 'Great Wall of China', 'Big Ben', 'Colosseum', 'Taj Mahal', 'Machu Picchu', 'Christ the Redeemer', 'Sydney Opera House', 'Mount Rushmore', 'Stonehenge', 'Petra', 'Angkor Wat', 'Burj Khalifa', 'Leaning Tower of Pisa', 'Chichen Itza', 'Neuschwanstein Castle', 'The Pyramids', 'Hagia Sophia', 'Sagrada Familia', 'Brandenburg Gate', 'Golden Gate Bridge', 'Tower of London', 'Acropolis of Athens', 'Alhambra', 'Versailles Palace', 'Moai Statues (Easter Island)', 'Mont Saint-Michel', 'CN Tower', 'Empire State Building', 'Kremlin', 'Edinburgh Castle', 'St. Basil’s Cathedral', 'Niagara Falls', 'Grand Canyon', 'Mount Fuji', 'Victoria Falls', 'Santorini (Oia Village)', 'Christchurch Cathedral', 'Forbidden City', 'Louvre Museum', 'The Blue Mosque', 'Tiananmen Square', 'Buckingham Palace', 'Hollywood Sign', 'Brooklyn Bridge', 'Pompeii', 'Guggenheim Museum', 'Red Square', 'Table Mountain', 'White House'],
            'correct': 'The Pyramids'
        },
        {
            'name': 'food.png',
            'url': 'imageid_task/food.png',
            'question': 'Which food chain owns this logo?',
            'options': ['Burger King', 'KFC', 'Wendy\'s', 'Taco Bell', 'Subway', 'Pizza Hut', 'Domino\'s', 'Papa John\'s', 'Dairy Queen', 'Starbucks', 'Chick-fil-A', 'Chipotle', 'Five Guys', 'Panda Express', 'Dunkin\' Donuts', 'Sonic Drive-In', 'Arby\'s', 'Jack in the Box', 'Little Caesars', 'Culver\'s', 'Shake Shack', 'In-N-Out Burger', 'Zaxby\'s', 'Raising Cane\'s', 'Bojangles', 'Whataburger', 'Hardee\'s', 'Carl\'s Jr.', 'Wingstop', 'Jersey Mike\'s Subs', 'Jimmy John\'s', 'Qdoba', 'Del Taco', 'El Pollo Loco', 'White Castle', 'Boston Market', 'Church\'s Chicken', 'Quiznos', 'Tim Hortons', 'Blaze Pizza', 'Checkers', 'Krystal', 'Freddy\'s Frozen Custard', 'Nando\'s', 'Sweetgreen', 'Firehouse Subs', 'Pret A Manger', 'McDonald\'s', 'McAlister\'s Deli', 'Portillo\'s'],
            'correct': 'McDonald\'s'
        },
        {
            'name': 'movie.png',
            'url': 'imageid_task/movie.png',
            'question': 'Which movie poster is this?',
            'options': ['The Godfather', 'The Shawshank Redemption', 'The Dark Knight', 'Forrest Gump', 'Inception', 'The Matrix', 'Titanic', 'The Lord of the Rings: The Return of the King', 'Gladiator', 'Schindler\'s List', 'The Silence of the Lambs', 'Saving Private Ryan', 'Interstellar', 'The Green Mile', 'Fight Club', 'The Departed', 'The Prestige', 'Goodfellas', 'The Usual Suspects', 'Django Unchained', 'Se7en', 'The Wolf of Wall Street', 'No Country for Old Men', 'There Will Be Blood', 'Casablanca', 'Braveheart', 'The Grand Budapest Hotel', 'A Beautiful Mind', 'The Social Network', 'Joker', 'La La Land', 'Whiplash', 'The Revenant', 'Mad Max: Fury Road', 'Once Upon a Time in Hollywood', 'The Truman Show', 'The Shining', 'Parasite', 'Oldboy', 'The Big Lebowski', 'Pulp Fiction', 'The Lion King', 'Avengers: Endgame', 'Spider-Man: Into the Spider-Verse', 'Guardians of the Galaxy', 'Logan', 'The Incredibles', 'Toy Story', 'Coco', 'Up', 'Inside Out'],
            'correct': 'Pulp Fiction'
        },
        {
            'name': 'sport.png',
            'url': 'imageid_task/sport.png',
            'question': 'Which Olympic sport is shown in this image?',
            'options': ['Soccer', 'Basketball', 'Tennis', 'Baseball', 'Football', 'Rugby', 'Cricket', 'Golf', 'Hockey', 'Lacrosse', 'Volleyball', 'Badminton', 'Table Tennis', 'Handball', 'Squash', 'Bowling', 'Darts', 'Archery', 'Shooting', 'Weightlifting', 'Powerlifting', 'Bodybuilding', 'Swimming', 'Diving', 'Water Polo', 'Sailing', 'Rowing', 'Kayaking', 'Fencing', 'Canoeing', 'Surfing', 'Skiing', 'Snowboarding', 'Skateboarding', 'Ice Skating', 'Speed Skating', 'Cycling', 'BMX', 'Motocross', 'Auto Racing', 'Equestrian', 'Wrestling', 'Boxing', 'Kickboxing', 'Judo', 'Karate', 'Taekwondo', 'Muay Thai', 'Brazilian Jiu-Jitsu', 'Sumo Wrestling'],
            'correct': 'Fencing'
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
