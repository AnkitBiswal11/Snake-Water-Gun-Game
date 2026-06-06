import random
import json
import os
from datetime import datetime


# ==============================
# Constants
# ==============================

CHOICES = {
    "s": "Snake",
    "w": "Water",
    "g": "Gun"
}

WIN_RULES = {
    ("s", "w"),
    ("w", "g"),
    ("g", "s")
}

LEADERBOARD_FILE = "leaderboard.json"
HISTORY_FILE = "match_history.json"


# ==============================
# Color Class
# ==============================

class Colors:
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    RESET = "\033[0m"


# ==============================
# Player Class
# ==============================

class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.wins = 0
        self.losses = 0
        self.draws = 0

    def record_win(self):
        self.wins += 1
        self.score += 1

    def record_loss(self):
        self.losses += 1

    def record_draw(self):
        self.draws += 1


# ==============================
# Leaderboard Manager
# ==============================

class Leaderboard:

    @staticmethod
    def load():

        if not os.path.exists(LEADERBOARD_FILE):
            return {}

        with open(LEADERBOARD_FILE, "r") as file:
            return json.load(file)

    @staticmethod
    def save(data):

        with open(LEADERBOARD_FILE, "w") as file:
            json.dump(data, file, indent=4)

    @classmethod
    def update(cls, player_name):

        board = cls.load()

        board[player_name] = board.get(player_name, 0) + 1

        cls.save(board)

    @classmethod
    def display(cls):

        board = cls.load()

        print("\n🏆 LEADERBOARD")
        print("-" * 30)

        if not board:
            print("No records found.")
            return

        sorted_board = sorted(
            board.items(),
            key=lambda x: x[1],
            reverse=True
        )

        for rank, (player, wins) in enumerate(sorted_board, start=1):
            print(f"{rank}. {player} - {wins} Wins")


# ==============================
# History Manager
# ==============================

class MatchHistory:

    @staticmethod
    def save_record(player, user_move, ai_move, result):

        record = {
            "player": player,
            "user_move": CHOICES[user_move],
            "computer_move": CHOICES[ai_move],
            "result": result,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        history = []

        if os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, "r") as file:
                try:
                    history = json.load(file)
                except:
                    history = []

        history.append(record)

        with open(HISTORY_FILE, "w") as file:
            json.dump(history, file, indent=4)


# ==============================
# AI
# ==============================

class ComputerAI:

    def __init__(self, difficulty="easy"):
        self.difficulty = difficulty

    def move(self, player_history):

        options = list(CHOICES.keys())

        if self.difficulty == "easy":
            return random.choice(options)

        elif self.difficulty == "medium":

            if random.random() < 0.7:
                return random.choice(options)

        elif self.difficulty == "hard":

            if player_history:

                last_move = player_history[-1]

                counter = {
                    "s": "g",
                    "w": "s",
                    "g": "w"
                }

                return counter[last_move]

        return random.choice(options)


# ==============================
# Game Engine
# ==============================

class GameEngine:

    @staticmethod
    def determine_winner(user, computer):

        if user == computer:
            return "draw"

        if (user, computer) in WIN_RULES:
            return "user"

        return "computer"


# ==============================
# Main Game
# ==============================

class SnakeWaterGunGame:

    def __init__(self):

        self.player_name = input("Enter your name: ").strip()

        self.player = Player(self.player_name)

        self.player_history = []

        difficulty = input(
            "Choose difficulty (easy/medium/hard): "
        ).lower()

        if difficulty not in ["easy", "medium", "hard"]:
            difficulty = "easy"

        self.ai = ComputerAI(difficulty)

    def get_player_move(self):

        while True:

            choice = input(
                "\nChoose Snake(s), Water(w), Gun(g): "
            ).lower()

            if choice in CHOICES:
                return choice

            print("Invalid Choice!")

    def play_round(self):

        user_move = self.get_player_move()

        computer_move = self.ai.move(self.player_history)

        self.player_history.append(user_move)

        result = GameEngine.determine_winner(
            user_move,
            computer_move
        )

        print("\n" + "=" * 40)
        print(f"You      : {CHOICES[user_move]}")
        print(f"Computer : {CHOICES[computer_move]}")
        print("=" * 40)

        if result == "user":

            print(
                Colors.GREEN +
                "🎉 You Win!" +
                Colors.RESET
            )

            self.player.record_win()

            MatchHistory.save_record(
                self.player.name,
                user_move,
                computer_move,
                "Win"
            )

        elif result == "computer":

            print(
                Colors.RED +
                "💻 Computer Wins!" +
                Colors.RESET
            )

            self.player.record_loss()

            MatchHistory.save_record(
                self.player.name,
                user_move,
                computer_move,
                "Loss"
            )

        else:

            print(
                Colors.YELLOW +
                "🤝 Draw!" +
                Colors.RESET
            )

            self.player.record_draw()

            MatchHistory.save_record(
                self.player.name,
                user_move,
                computer_move,
                "Draw"
            )

    def show_stats(self):

        total = (
            self.player.wins +
            self.player.losses +
            self.player.draws
        )

        win_rate = (
            self.player.wins / total * 100
            if total else 0
        )

        print("\n📊 STATISTICS")
        print("-" * 30)

        print(f"Player : {self.player.name}")
        print(f"Wins   : {self.player.wins}")
        print(f"Losses : {self.player.losses}")
        print(f"Draws  : {self.player.draws}")
        print(f"Win %  : {win_rate:.2f}")

    def tournament(self):

        rounds = int(
            input(
                "\nBest of (3/5/7): "
            )
        )

        target = rounds // 2 + 1

        player_score = 0
        computer_score = 0

        while (
            player_score < target
            and computer_score < target
        ):

            user = self.get_player_move()
            ai = self.ai.move(self.player_history)

            result = GameEngine.determine_winner(user, ai)

            print(
                f"\nYou: {CHOICES[user]}"
            )
            print(
                f"Computer: {CHOICES[ai]}"
            )

            if result == "user":
                player_score += 1
                print("You Win Round")

            elif result == "computer":
                computer_score += 1
                print("Computer Wins Round")

            else:
                print("Round Draw")

        print("\n🏁 TOURNAMENT OVER")

        if player_score > computer_score:
            print("🎉 You Won Tournament!")
            Leaderboard.update(self.player.name)

        else:
            print("💻 Computer Won Tournament!")

    def run(self):

        while True:

            print("\n" + "=" * 40)
            print("🐍 SNAKE WATER GUN ARENA")
            print("=" * 40)

            print("1. Play Round")
            print("2. Tournament")
            print("3. Statistics")
            print("4. Leaderboard")
            print("5. Exit")

            choice = input("\nSelect Option: ")

            if choice == "1":
                self.play_round()

            elif choice == "2":
                self.tournament()

            elif choice == "3":
                self.show_stats()

            elif choice == "4":
                Leaderboard.display()

            elif choice == "5":

                print(
                    Colors.CYAN +
                    "\nThanks For Playing!" +
                    Colors.RESET
                )

                break

            else:
                print("Invalid Option")


# ==============================
# Driver Code
# ==============================

if __name__ == "__main__":
    game = SnakeWaterGunGame()
    game.run()