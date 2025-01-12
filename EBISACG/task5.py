import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_triangle():
    # Clear the screen
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    # Draw a purple triangle
    glBegin(GL_TRIANGLES)
    glColor3f(0.5, 0.0, 0.5)  # Purple color
    glVertex2f(-0.5, -0.5)    # Bottom-left vertex
    glVertex2f(0.5, -0.5)     # Bottom-right vertex
    glVertex2f(0.0, 0.5)      # Top vertex
    glEnd()
    
    # Swap the buffers to display the triangle
    pygame.display.flip()

def main():
    # Initialize PyGame and create an OpenGL context
    pygame.init()
    display = (800, 600)  # Set window size
    pygame.display.set_mode(display, pygame.OPENGL | pygame.DOUBLEBUF)
    pygame.display.set_caption("Purple Triangle")

    # Set up the OpenGL viewport and orthographic projection
    glViewport(0, 0, display[0], display[1])
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1, 1, -1, 1, -1, 1)  # Orthographic projection
    glMatrixMode(GL_MODELVIEW)

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        draw_triangle()  # Call the triangle drawing function
    
    pygame.quit()

# Run the program
if __name__ == "__main__":
    main()
