import pygame
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 400))
    pygame.display.set_caption("Ethiopian Flag")
    screen.fill((255, 255, 255))  # Fill the canvas with white color
   
    pygame.draw.rect(screen, (0, 128, 0), (50, 100, 400, 50))  # Green
    pygame.draw.rect(screen, (255, 255, 0), (50, 150, 400, 50))  # Yellow
    pygame.draw.rect(screen, (255, 0, 0), (50, 200, 400, 50))  # Red
    
    pygame.draw.circle(screen, (128, 0, 128), (250, 175), 5)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                running = False

        pygame.display.flip()

    pygame.quit()
    sys.exit()

# Call the function
main()
