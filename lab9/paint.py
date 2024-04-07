# Draw square
# Draw right triangle
# Draw equilateral triangle
# Draw rhombus
# Comment code


import pygame  
import math  

# Define the main function that controls the program flow
def main():  
    # Initialize Pygame 
    pygame.init()  
    # Set up the display screen 
    screen = pygame.display.set_mode((640, 480))  
    # to control the frame rate
    clock = pygame.time.Clock()  
    
    # Initialize variables for drawing
    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []
    drawing_shape = None
    color = (255, 255, 255)

    # Main loop 
    while True:  
        # Get the state of all keyboard keys
        pressed = pygame.key.get_pressed()  
        # Check if Alt key is held
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]  
        # Check if Ctrl key is held
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]  
        
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                return  
            if event.type == pygame.KEYDOWN:  
                # Exit the program if Ctrl + W is pressed
                if event.key == pygame.K_w and ctrl_held:  
                    return  
                # Exit the program if Alt + F4 is pressed
                if event.key == pygame.K_F4 and alt_held:  
                    return  
                # Exit the program if Escape key is pressed
                if event.key == pygame.K_ESCAPE:  
                    return  
                # Change drawing color to red if 'R' key is pressed
                if event.key == pygame.K_r:  
                    mode = 'red'  
                # Change drawing color to green if 'G' key is pressed
                elif event.key == pygame.K_g:  
                    mode = 'green'  
                # Change drawing color to blue if 'B' key is pressed
                elif event.key == pygame.K_b:  
                    mode = 'blue'  
                # black if 'C' key is pressed  
                elif event.key == pygame.K_c:  
                    color = pygame.color.Color("black")  
                # black if 'E' key is pressed
                elif event.key == pygame.K_e:  
                    color = (0, 0, 0)
                #rectangle if '1' key is pressed
                elif event.key == pygame.K_1:  
                    drawing_shape = 'rectangle'  
                #circle if '2' key is pressed
                elif event.key == pygame.K_2:  
                    drawing_shape = 'circle'  
                #square if '3' key is pressed
                elif event.key == pygame.K_3:  
                    drawing_shape = 'square'  
                #right triangle if '4' key is pressed
                elif event.key == pygame.K_4:  
                    drawing_shape = 'right_triangle'  
                #equilateral triangle if '5' key is pressed
                elif event.key == pygame.K_5:  
                    drawing_shape = 'equilateral_triangle'  
                #rhombus if '6' key is pressed
                elif event.key == pygame.K_6:  
                    drawing_shape = 'rhombus'  
            
            # If a mouse button is pressed
            if event.type == pygame.MOUSEBUTTONDOWN:  
                # Increase radius of drawing tool if left mouse button is pressed
                if event.button == 1:   
                    radius = min(200, radius + 1)  
                # Decrease radius of drawing tool if right mouse button is pressed
                elif event.button == 3:  
                    radius = max(1, radius - 1)  
            
            # If the mouse is moved
            if event.type == pygame.MOUSEMOTION:  
                # Get the current mouse position
                position = event.pos  
                # Add the position to the list of points and keep only the last 256 points
                points.append(position)  
                points = points[-256:]  
        
        # Fill the screen with black color
        screen.fill((0, 0, 0))  
        
        # Loop through all points except the last one
        for i in range(len(points) - 1):  
            # Draw shapes based on the selected drawing shape
            if drawing_shape == 'rectangle':  
                # Draw a rectangle
                pygame.draw.rect(screen, color, (points[i], (points[i+1][0]-points[i][0], points[i+1][1]-points[i][1])), 2)
            elif drawing_shape == 'circle':  
                # Draw a circle
                pygame.draw.circle(screen, color, points[i], radius)
            elif drawing_shape == 'square':  
                # Draw a square
                side_length = max(abs(points[i][0] - points[i+1][0]), abs(points[i][1] - points[i+1][1]))
                pygame.draw.rect(screen, color, (points[i], (side_length, side_length)), 2)
            elif drawing_shape == 'right_triangle':  
                # Draw a right triangle
                pygame.draw.polygon(screen, color, [(points[i][0], points[i][1]), (points[i+1][0], points[i][1]), (points[i][0], points[i+1][1])], 2)
            elif drawing_shape == 'equilateral_triangle':  
                # Draw an equilateral triangle
                side_length = max(abs(points[i][0] - points[i+1][0]), abs(points[i][1] - points[i+1][1]))
                height = math.sqrt(3) / 2 * side_length
                pygame.draw.polygon(screen, color, [(points[i][0], points[i][1]), (points[i+1][0], points[i][1]), ((points[i][0] + points[i+1][0]) / 2, points[i][1] - height)], 2)
            elif drawing_shape == 'rhombus':  
                # Draw a rhombus
                width = abs(points[i+1][0] - points[i][0])
                height = abs(points[i+1][1] - points[i][1])
                pygame.draw.polygon(screen, color, [(points[i][0] + width / 2, points[i][1]), (points[i+1][0], points[i][1] + height / 2), (points[i][0] + width / 2, points[i+1][1]), (points[i][0], points[i][1] + height / 2)], 2)
            else:  
                # Draw lines with gradient colors
                drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
        
        # Update the display
        pygame.display.flip()  
        # Cap the frame rate at 60 frames per second
        clock.tick(60)

# Function to draw lines between two points with gradient colors
def drawLineBetween(screen, index, start, end, width, color_mode):
    # Calculate color values for gradient effect
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    # Set color based on drawing mode
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    
    # Calculate the change in x and y coordinates
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    # Determine the number of iterations based on the longer distance
    iterations = max(abs(dx), abs(dy))
    
    # Iterate over the line and draw circles at intermediate points with gradient color
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        # Calculate the x and y coordinates of the current point
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        # Draw a circle at the current point with the calculated color
        pygame.draw.circle(screen, color, (x, y), width)

# Call the main function to run the program
main()
