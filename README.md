<div align="center">
    <img src="Python Code/Asset/icon/game.jpg" alt="Banner" width="300" height="300">
</div>

# Language Journey - Quiz & Maze Game

This is an interactive game developed in Python and Tkinter that combines questions with a maze-style adventure. The goal is to progress through the maze by answering questions correctly, avoiding crocodiles, and reaching the prize. High scores are saved in an SQLite database, allowing the top 10 players to view them. The project includes a login screen, a game screen, and sound effects for correct and incorrect answers.

## Table of Contents
- [Game Features](#game-features)
- [Setup](#setup)
- [How to Play](#how-to-play)
- [Folder Structure](#folder-structure)
- [Contributing](#contributing)
  
## Game Features
- **Login System**: Players can enter their names to start the game. Their names, true, false and blank numbers are recorded after each session.
- **Maze Navigation**: Players move through the maze by answering questions. Correct answers allow you to move forward, while incorrect answers lead to encounters with crocodiles.
- **Leaderboard**: A separate window displays the top 10 players by correct answers, with the option to clear all data.
- **Sound Effects**: Success and failure sound effects enhance the gaming experience.
- **Countdown Timer**: Each question has a time limit, adding a layer of difficulty.
  
## Setup
1. Install Python (I used Python version 3.10.11): `https://www.python.org/`
2. Install requirements : `pip install -r requirements.txt`
3. Run Dil_Yolculuğu.py script : `python Dil_Yolculuğu.py `

## Folder Structure
```
.
├── Asset                   
|   ├── Background
|   |   └── labirent.png
|   ├── Database
|   |   ├──oyuncu_skori.db
|   |   └── kullanici.txt
|   ├── İmages
|   |   ├──karakter.png
|   |   ├──odul.png
|   |   ├──son_odul.jpg
|   |   └──timsah.png
|   ├── Library
|   |   ├──database_save.py
|   |   ├──main.py
|   |   ├──quiz_data.py
|   |   └──son_odul.py
|   ├── Voice
|   |   ├──alkis_sesi.mp3
|   |   └──yanlis_cevap.mp3  
|   └── İcon
|       ├──game.jpg
|       └──icon.ico
├── Dil_Yolculuğu.py              

```
## How to Play

1. **Start Game**  
 Enter your name on the login screen and click the **Oyuna Başla** button.

2. **Answer Questions**  
  Answer questions true or false to advance through the maze. Each correct answer brings the character closer to the prize. 

3. **Avoid Obstacles**  
   Incorrect answers can lead to encounters with "crocodiles" in the maze. The game ends if you get too close to them.

4. **View Leaderboard**  
   Check the top 10 scores by clicking **En İyi 10 Kullanıcı** on the main screen.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

