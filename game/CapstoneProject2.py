# This is a game, with one 'Player' object,
# the player can be moved around the screen by using the up, down, left and right arrows.
# There are 3 'Enemies' and one 'Prize'. The enemies move across the screen from different positions.
# If the player object collides with any enemy object, they lose, and the game ends.
# If player collides with prize object they win with highest score and the game ends.

import pygame  # Imports a game library for specific functions in your program.
import random  # Import to generate random numbers.

# Initialize the pygame modules to get everything started.
pygame.init()

# Determining the screen width and a height.
screen_width = 1040
screen_height = 680
screen = pygame.display.set_mode((screen_width, screen_height))

# This creates the player, prize and enemies then gives it the image found in this folder.
player = pygame.image.load("image.png")
enemy = pygame.image.load("enemy.png")
enemy2 = pygame.image.load("monster.jpg")
prize = pygame.image.load("prize.jpg")
enemy3 = pygame.image.load("enemy3.jpg")

# Get the width and height of the images in order to do boundary detection
# (i.e. make sure the image stays within screen boundaries or know when the image is off the screen).
image_height = player.get_height()
image_width = player.get_width()
enemy_height = enemy.get_height()
enemy_width = enemy.get_width()
enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()
enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()
prize_width = prize.get_width()
prize_height = prize.get_height()

print("This is the height of the player image: " + str(image_height))
print("This is the width of the player image: " + str(image_width))

# Store the positions of the player and enemy as variables so that they can change later.
playerXPosition = 50
playerYPosition = 50

# Make the enemy 1 start off screen at any random y position.
enemyXPosition = screen_width
enemyYPosition = random.randint(0, screen_height - enemy_height)
# Make the enemy 2 start off screen at any random x position.
enemy2XPosition = random.randint(0, screen_width - enemy2_width)
enemy2YPosition = screen_height
# Make the prize start off screen at any random y position.
prizeXPosition = screen_width
prizeYPosition = random.randint(0, screen_height - prize_height)
# Make the enemy 3 start off screen at any random y position.
enemy3XPosition = random.randint(0, screen_width - enemy2_width)
enemy3YPosition = screen_height


# This checks if the up, down, left or right keys are pressed.
# Right now they are not so make them equal to the boolean value of False.
keyUp = False
keyDown = False
keyLeft = False
keyRight = False

# This is the game loop.
# In games you will need to run the game logic over and over again.
# You need to refresh/update the screen window and apply changes to 
# represent real time game play. 
while 1:
    # This is a looping structure that will loop the indented code until you tell it to stop by quitting a game
    # In Python the int 1 has the boolean value of 'true'.

    screen.fill(0)      # Clears the screen.
    # This draws the player image to the screen at the position specified. I.e. (100, 50).
    screen.blit(player, (playerXPosition, playerYPosition))
    screen.blit(enemy, (enemyXPosition, enemyYPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))

    pygame.display.flip()   # This updates the screen.
    
    # This loops through events in the game.
    for event in pygame.event.get():
    
        # This event checks if the user quits the program, then if so it exits the program.
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        # This event checks if the user press a key down.
        if event.type == pygame.KEYDOWN:
        
            # Test if the key pressed is the one we want.
            if event.key == pygame.K_UP:    # pygame.K_UP represents a keyboard key constant.
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:   # pygame.K_UP represents a keyboard key constant.
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True

        # This event checks if the key is up(i.e. not pressed by the user).
        
        if event.type == pygame.KEYUP:
        
            # Test if the key released is the one we want.
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False

    # After events are checked for in the for loop above and values are set,
    # check key pressed values and move player accordingly.
    
    # The coordinate system of the game window(screen) is that the top left corner is (0, 0).
    # This means that if you want the player to move down you will have to increase the y position. 
    
    if keyUp is True:
        if playerYPosition > 0:    # This makes sure that the user does not move the player above the window.
            playerYPosition -= 1
    if keyDown is True:            # This makes sure that the user does not move the player below the window.
        if playerYPosition < screen_height - image_height:
            playerYPosition += 1
    if keyLeft is True:
        if playerXPosition > 0:    # This makes sure that the user does not move the player out of the window.
            playerXPosition -= 1
    if keyRight is True:           # This makes sure that the user does not move the player out of the window.
        if playerXPosition < screen_width - image_width:
            playerXPosition += 1

    # Check for collision of the enemies and prize with the player.
    # To do this we need bounding boxes around the images of the player, enemy and prize.
    # We then need to test if these boxes intersect. If they do then there is a collision.
    
    # Bounding box for the player:
    playerBox = pygame.Rect(player.get_rect())
    
    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image. 
    
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
    # Bounding box for the enemy:
    enemyBox = pygame.Rect(enemy.get_rect())
    enemyBox.top = enemyYPosition
    enemyBox.left = enemyXPosition

    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition

    enemy3Box = pygame.Rect(enemy3.get_rect())
    enemy3Box.top = enemy3YPosition
    enemy3Box.left = enemy3XPosition

    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition
    
    # Test collision of the boxes:
    
    if playerBox.colliderect(enemyBox) or playerBox.colliderect(enemy2Box) or playerBox.colliderect(enemy3Box):
        print("You lose! try again")      # Display losing status to the user:
        pygame.quit()                     # Quite game and exit window:
        exit(0)

    if playerBox.colliderect(prizeBox):
        print("Excellent!, You won the prize!")
        print("5 stars for you!")
        pygame.quit()
        exit(0)

    # If the enemies are off the screen the user wins the game:
    
    if enemyXPosition < 0 - enemy_width and enemy2YPosition < 0 - enemy_height and enemy3YPosition < 0 - enemy_height:
        print("You win! but next time try to hit the prize, the berries")
        pygame.quit()       # Quite game and exit window:
        exit(0)
    
    # Make enemies approach the player at different speeds.
    enemyXPosition -= 0.20
    enemy2YPosition -= 0.90
    enemy3YPosition -= 0.90
    prizeXPosition -= 0.90
