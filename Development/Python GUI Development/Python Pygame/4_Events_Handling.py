import pygame
pygame.init()
pygame.display.set_mode((1000, 500))
pygame.display.set_caption("My Game")

exit_Game = False
while not exit_Game:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            exit_Game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("You Pressed Right arrow key.")
        pygame.display.flip()

pygame.quit()
quit()

'''
Let's understand the basic syntax of the above program line by line:

1. import pygame - This provides access to the pygame framework and imports all functions of pygame.

2. pygame.init() - This is used to initialize all the required module of the pygame.

3. pygame.display.set_mode((width, height)) - This is used to display a window of the desired size. The return value is a Surface object which is the object where we will perform graphical operations.

4. pygame.event.get()- This is used to empty the event queue. If we do not call this, the window messages will start to pile up and, the game will become unresponsive in the opinion of the operating system.

5. pygame.QUIT - This is used to terminate the event when we click on the close button at the corner of the window.

6. pygame.display.flip() - Pygame is double-buffered, so this shifts the buffers. It is essential to call this function in order to make any updates that you make on the game screen to make visible.

'''