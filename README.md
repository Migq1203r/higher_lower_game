# Instagram Follower Comparison Game

This is a fun and interactive game where you guess which celebrity has more followers on Instagram. The game presents two random celebrities, and you need to choose which one has more followers. Each correct answer increases your score, while a wrong answer resets it to zero.

## Features:

* Interactive text-based gameplay
* Random selection of celebrities and their Instagram follower count
* Option to keep track of your score

## Prerequisites:

To run this game, you'll need to have Python 3 installed on your machine. You also need to import the `game_data` that contains the details of celebrities, including their names, professions, countries, and follower counts.

### Required Libraries:

* `random` (standard Python library)

## Installation:

1. Clone or download the repository to your local machine.
2. Make sure you have the `game_data` file with the correct structure, as it's used to fetch celebrity details. Here's an example structure for the data:

   ```python
   data = [
       {
           "name": "Celebrity Name",
           "profession": "Profession",
           "country": "Country",
           "followers": 123456789
       },
       ...
   ]
   ```
3. Run the `game.py` file:

   ```bash
   python game.py
   ```

## How to Play:

1. The game will display two celebrities with their names, professions, and countries.
2. You need to guess who has more followers on Instagram by typing 'A' or 'B' (for the respective options).
3. If you guess correctly, your score increases by one. If you guess incorrectly, your score resets to zero.
4. The game will continue to ask you questions until you get one wrong.

## Example Gameplay:

```plaintext
     __  ___       __             
    / / / (_)___ _/ /_  ___  _____
   / /_/ / / __ `/ __ \/ _ \/ ___/
  / __  / / /_/ / / / /  __/ /    
 /_/ ///_/\__, /_/ /_/\___/_/     
    / /  /____/_      _____  _____
   / /   / __ \ | /| / / _ \/ ___/
  / /___/ /_/ / |/ |/ /  __/ /    
 /_____/\____/|__/|__/\___/_/     

Who has more Followers on Instagram?
Compare A: John Doe, a singer, from USA.

 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)

Against B: Jane Doe, an actress, from UK.

Who has more Followers? Type 'A' or 'B': A

You're right! Current score: 1
```

## Code Overview:

* **Main Functionality**:

  * The game randomly selects two celebrities from the data list and displays their details.
  * The user guesses which celebrity has more followers.
  * The score is updated based on the correctness of the guess.

* **`sortear()`**:

  * Randomly selects two unique celebrities from the data to be compared.

* **`check_answer()`**:

  * Compares the follower counts of the two celebrities and checks if the user's guess is correct.

* **Game Loop**:

  * After each guess, the screen is cleared, and a new round of celebrities is presented.

## Contributing:

If you'd like to contribute to this project, feel free to fork the repository, submit pull requests, or open issues. We'd love to have your feedback!
