import pygame
pygame.init()
surface = pygame.display.set_mode((400, 400))
surface.fill("Green")
exit_game = False
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        pygame.display.flip()
pygame.quit()
quit()