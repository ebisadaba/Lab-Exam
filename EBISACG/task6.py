import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_line(x1, y1, x2, y2):
    """Draw a line between two points P1(x1, y1) and P2(x2, y2)."""
    glBegin(GL_LINES)
    glColor3f(0.0, 1.0, 0.0)  # Set line color to green
    glVertex2f(x1, y1)        # Start point (x1, y1)
    glVertex2f(x2, y2)        # End point (x2, y2)
    glEnd()

def main():
    # Initialize PyGame and create an OpenGL context
    pygame.init()
    display = (800, 600)  # Set the window size
    pygame.display.set_mode(display, pygame.OPENGL | pygame.DOUBLEBUF)
    pygame.display.set_caption("Draw Line with PyGame and OpenGL")

    # Set up the OpenGL viewport and orthographic projection
    glViewport(0, 0, display[0], display[1])
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1, 1, -1, 1, -1, 1)  # Define a 2D orthographic projection
    glMatrixMode(GL_MODELVIEW)

    # Main rendering loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        # Example: Draw a line between (-0.7, -0.7) and (0.7, 0.7)
        draw_line(-0.7, -0.7, 0.7, 0.7)

        # Swap the buffers to update the display
        pygame.display.flip()

    pygame.quit()

# Run the program
if __name__ == "__main__":
    main()
