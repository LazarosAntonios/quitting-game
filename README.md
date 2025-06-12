quitting-game

A simple oTree experiment to study quitting behavior in sequential games.

Table of Contents

Overview

Features

Prerequisites

Installation

Running the Experiment

Project Structure

Configuration

Contributing

License

Overview

This repository contains an oTree project named quitting-game. Participants play a sequential decision task where they decide whether to continue or quit at each stage. The design allows analysis of risk-taking and quitting thresholds.

Features

Interactive web interface built with oTree

Configurable number of stages and payoffs

Data export in CSV for analysis

Clean codebase following best practices (see codebase_experiment.md)

Prerequisites

Python 3.8 or higher

oTree 6.x

pip or venv for virtual environments

Installation

Clone the repo:

git clone https://github.com/LazarosAntonios/quitting-game.git
cd quitting-game

Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate    # Windows

Install dependencies:

pip install -r requirements.txt

Running the Experiment

Launch the oTree server:

otree devserver

Open your browser at http://localhost:8000.

Select quitting-game and start a session.

Project Structure

quitting-game/
├── quitting_game/           # oTree app folder
│   ├── __init__.py
│   ├── models.py            # Game logic and variables
│   ├── pages.py             # Page sequence and forms
│   ├── templates/
│   ├── static/
│   └── codebase_experiment.md
├── requirements.txt         # Python dependencies
├── settings.py              # oTree configuration
├── README.md                # This file
└── LICENSE

Configuration

Edit settings.py to adjust:

Number of players

Payoff parameters

Session settings

Contributing

Contributions are welcome. To propose changes:

Fork the repository.

Create a feature branch (git checkout -b feature-name).

Commit your changes (git commit -m "Add feature").

Push to your branch (git push origin feature-name).

Open a pull request.

License

This project is licensed under the MIT License. See LICENSE for details.

