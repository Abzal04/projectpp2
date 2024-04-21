# Rainy day adventure
------
**Rainy Day Adventure** is a simple pygame-based game where the player controls a student character trying to avoid raindrops falling from the sky using an umbrella. The goal is to survive as long as possible without getting hit by the raindrops.
The player must use the umbrella to protect the student character from the falling raindrops. The game ends if the student character gets hit by a raindrop or if the time limit is reached. The ultimate goal is to achieve a high score by surviving for as long as possible and avoiding as many raindrops as you can.

## Running the game 
### To run the game you will need the pygame and python(3.6-newer versions) to be installed, also assets(images) from the repository.
``` python
python3 main.py
```
### To start the game, ``` main.py ``` file should be executed
## Code
### Libraries used: ```pygame```,```time```,```random```,```sys```,```datetime```
``` python 
def __init__(self):
 ```
#### Initializes a Raindrop, Umbrella, Student sprite with its image, position, movement direction, and animation-related attributes.
``` python 
 def move(self):
 ```
#### The movement logic for the Student sprite. It randomly selects a direction for movement and updates the sprite's position accordingly. It also handles collisions with the game window boundaries.
``` python 
def explosion(self):
 ```
#### Implements the explosion animation for the Student sprite when it collides with a raindrop.
``` python 
while running:
``` 
#### Manages the main game loop, including event handling, updating game objects, drawing the game screen, and controlling the frame rate.
``` Game Over and Win Conditions Handling ``` 
#### Handles the game over and win conditions. Displays appropriate text on the screen when the game ends due to collision with raindrops or when the win condition is met.
