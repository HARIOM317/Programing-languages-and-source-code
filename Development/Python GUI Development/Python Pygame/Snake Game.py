import pygame
import random
import os

pygame.mixer.init()
pygame.init()
# Play background music on wellcome screen
pygame.mixer.music.load('wellcome.mp3')
pygame.mixer.music.play()

# Define colors with RGB values
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

screen_width = 1000
screen_height = 550
gameWindow = pygame.display.set_mode((screen_width, screen_height))   # Set screen width and height

# Put a logo on wellcome screen
logo = pygame.image.load('Snake_icon.png')
logo = pygame.transform.scale(logo, (screen_width/4, screen_height/4)).convert_alpha()

pygame.display.set_caption("Snake Game")    # Set a title
pygame.display.update()  # Updating screen

clock = pygame.time.Clock()
font = pygame.font.SysFont("Poor Richard", 50)
font2 = pygame.font.SysFont("Georgia", 20)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)    # Fix Resolution
    gameWindow.blit(screen_text, [x, y])    # Update screen using blit

def text_screen2(text, color, x, y):
    screen_text = font2.render(text, True, color)    # Fix Resolution
    gameWindow.blit(screen_text, [x, y])    # Update screen using blit

def plot_snake(gameWindow, color, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def wellcome():
    Exit_game = False
    while not Exit_game:
        gameWindow.fill("#5eba99")
        gameWindow.blit(logo, (330, 50))
        text_screen("Well Come To Snake Game", white, 225, 200)
        text_screen2("Press space to play...", black, 380, 270)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                Exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('background.mp3')
                    pygame.mixer.music.play()
                    gameloop()

        pygame.display.update()
        clock.tick(70)

# Game loop
def gameloop():
    # Creating some game specific variables
    Exit_game = False
    Game_Over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    init_velocity = 1
    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    snake_size = 20
    fps = 70

    snake_list = []
    snake_length = 1

    # Check if highScore.txt is exists or not
    if (not os.path.exists("high_score.txt")):
        with open("high_score.txt", 'w') as f:
            f.write('0')

    with open('high_score.txt', 'r') as f:
        highScore = f.read()

    while not Exit_game:
        with open('high_score.txt', 'w') as f:
            f.write(str(highScore))

        if Game_Over:
            gameWindow.fill("#95e42a")
            gameWindow.blit(logo, (330, 60))
            text_screen("Game Over! Press Enter To Continue", red, 165, 220)
            text_screen2("Score :  " + str(score) + "   ( High Score :  " + str(highScore) + ")", "blue", 350, 300)

            for event in pygame.event.get():
                # Handling Quit event
                if event.type == pygame.QUIT:
                    Exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.load('background.mp3')
                        pygame.mixer.music.play()
                        gameloop()
        else:
            for event in pygame.event.get():
                # Handling Quit event
                if event.type == pygame.QUIT:
                    Exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x) < 15 and abs(snake_y - food_y) < 15:
                score += 1
                if score % 10 == 0:
                    # fps += 1
                    init_velocity += 1
                food_x = random.randint(50, screen_width/2)
                food_y = random.randint(50, screen_height/2)
                snake_length += 5
                if score > int(highScore):
                    highScore = score

            # Fill display with this color code
            gameWindow.fill("#c0b707")
            text_screen2("Score :  " + str(score), "dark blue", 450, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                Game_Over = True
                pygame.mixer.music.load('game_over.mp3')
                pygame.mixer.music.play()

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                Game_Over = True
                pygame.mixer.music.load('game_over.mp3')
                pygame.mixer.music.play()
            # Draw a rectangle for snake's head
            plot_snake(gameWindow, black, snake_list, snake_size)

        # Updating display
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

if __name__ == '__main__':
    wellcome()
