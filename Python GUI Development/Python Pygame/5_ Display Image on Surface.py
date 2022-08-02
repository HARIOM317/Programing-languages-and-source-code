import pygame
pygame.init()
width = 1024
height = 612

display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Displaying an Image")
image = pygame.image.load("D:\\photos\\ultra hd 8k resolution images\\Welcome Scan.jpg")

while True:
    display.fill("Red")
    display.blit(image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()
