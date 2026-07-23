# snake-game
Classic Snake Game built using Python and Pygame.

## Features

- Start menu
- Smooth keyboard controls
- Random food generation
- Collision detection
- Score tracking
- Persistent high score saved to `highscore.json`
- Pause and resume support
- Increasing game speed as the score increases
- Restart and quit options after game over

## Project Structure

```text
snake-game/
├── snake_game.py
├── requirements.txt
├── README.md
└── highscore.json
```

`highscore.json` is created automatically the first time a new high score is recorded.

## Requirements

- Python 3.10 or later
- Pygame

## Installation

1. Clone the repository.

```bash
git clone https://github.com/agentuser5232/snake-game.git
cd snake-game
```

2. Install the required package.

```bash
pip install -r requirements.txt
```

3. Start the game.

```bash
python snake_game.py
```

## Controls

| Key | Action |
|------|--------|
| Arrow Keys | Move the snake |
| P | Pause or resume the game |
| R | Restart after game over |
| Q | Quit the game |
