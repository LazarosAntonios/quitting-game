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
