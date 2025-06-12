# Quitting Game

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![oTree](https://img.shields.io/badge/oTree-6.x-orange)](https://otree.readthedocs.io/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

A web-based experiment built with oTree to study quitting decisions in sequential games.

---

## 🚀 Quick Start

1. **Clone the repo**

   ```bash
   git clone https://github.com/LazarosAntonios/quitting-game.git
   cd quitting-game
   ```
2. **Set up environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\Scripts\activate    # Windows
   pip install -r requirements.txt
   ```
3. **Run the server**

   ```bash
   otree devserver
   ```
4. **Open in browser**
   Navigate to `http://localhost:8000`, select **quitting-game**, start session.

---

## 🔍 Features

* Configurable stages and payoffs
* Clean UI with oTree pages
* Data export in CSV format
* Modular code for easy extension

---

## 📂 Project Structure

```plain
quitting-game/
├── quitting_game/           # oTree app
│   ├── __init__.py
│   ├── models.py            # core game logic
│   ├── pages.py             # page flow and forms
│   ├── templates/           # HTML templates
│   ├── static/              # CSS/JS assets
│   └── codebase_experiment.md  # design notes
├── requirements.txt         # dependencies
├── settings.py              # oTree settings
├── README.md                # project guide
└── LICENSE                  # MIT license
```

---

## ⚙️ Configuration

Edit `settings.py` to adjust:

* Number of players
* Payoff values
* Session parameters

---

## 🤝 Contributing

1. Fork the repo
2. Create a branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m "Add feature"`
4. Push branch: `git push origin feature-name`
5. Open a pull request

---

## 📄 License

This project uses the MIT License. See [LICENSE](LICENSE) for details.
