# 🐍 Snake Water Gun Arena

A professional and feature-rich implementation of the classic **Snake Water Gun** game built with Python.

This project goes beyond the traditional beginner-level game by incorporating Object-Oriented Programming (OOP), AI difficulty levels, persistent leaderboard storage, match history tracking, tournament mode, and player statistics.

---

## 🚀 Features

### 🎮 Gameplay
- Snake 🐍
- Water 💧
- Gun 🔫

### 🤖 AI Opponent
- Easy Mode – Completely random moves
- Medium Mode – Semi-random strategy
- Hard Mode – Predictive AI based on player history

### 🏆 Tournament Mode
- Best of 3
- Best of 5
- Best of 7

### 📊 Statistics
- Wins
- Losses
- Draws
- Win Rate Calculation

### 💾 Persistent Storage
- JSON-based leaderboard
- Match history saved automatically
- Player performance tracking

### 🎨 Enhanced User Experience
- Colored terminal output
- Menu-driven interface
- Input validation
- Clean and professional structure

---

## 📂 Project Structure

```text
Snake-Water-Gun-Arena/
│
├── snake_water_gun.py
├── leaderboard.json
├── match_history.json
├── README.md
└── .gitignore
```

---

## 🛠️ Technologies Used

- Python 3.x
- Object-Oriented Programming (OOP)
- JSON Data Storage
- File Handling
- Random Module
- Datetime Module

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/snake-water-gun-arena.git
```

### Navigate to Project

```bash
cd snake-water-gun-arena
```

### Run the Game

```bash
python snake_water_gun.py
```

---

## 🎯 How to Play

| Choice | Input |
|----------|--------|
| Snake | s |
| Water | w |
| Gun | g |

### Rules

- Snake drinks Water → Snake Wins
- Water damages Gun → Water Wins
- Gun kills Snake → Gun Wins
- Same choice → Draw

---

## 🏆 Leaderboard System

The game automatically stores tournament winners in:

```text
leaderboard.json
```

Example:

```json
{
    "Aryan": 5,
    "Rahul": 3,
    "Aman": 2
}
```

---

## 📝 Match History

Every match is saved with:

- Player Name
- User Move
- Computer Move
- Result
- Timestamp

Example:

```json
{
    "player": "Aryan",
    "user_move": "Snake",
    "computer_move": "Water",
    "result": "Win",
    "time": "2026-06-06 14:35:21"
}
```

---

## 📈 Statistics Dashboard

Track:

- Total Matches
- Wins
- Losses
- Draws
- Win Percentage

Example:

```text
Player : Aryan
Wins   : 12
Losses : 5
Draws  : 2
Win %  : 63.15
```

---

## 🔥 Future Enhancements

- SQLite Database Integration
- GUI Version using Tkinter
- Multiplayer Mode
- Online Leaderboards
- User Authentication
- Achievement System
- Sound Effects
- Web Version using Flask or Streamlit

---

## 🧪 Testing

Future versions will include:

```bash
python -m unittest
```

for automated testing.

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Add new feature"
```

4. Push to branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License.

Feel free to use, modify, and distribute this project.

---

## 👨‍💻 Author

Developed with Python as a portfolio project to demonstrate:

- OOP Concepts
- File Handling
- Data Persistence
- Game Logic Design
- Software Architecture

⭐ If you like this project, consider giving it a star on GitHub.
