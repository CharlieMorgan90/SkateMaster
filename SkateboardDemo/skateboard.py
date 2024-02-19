import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Gradual Skateboard Ollie Simulation')

# Load and resize the skateboard image
skateboard_image_path = 'skateboard.png'  # Ensure this path is correct
skateboard_img_original = pygame.image.load(skateboard_image_path)
skateboard_img_original = pygame.transform.scale(skateboard_img_original, (300, 200))  # Adjust size as needed

# Skateboard state
skateboard_pos = [screen_width // 2, screen_height // 2]
original_y = skateboard_pos[1]  # Keep track of the original Y position to return to
is_ollieing = False
ollie_progress = 0
angle = 0  # Skateboard tilt angle

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Start the ollie on spacebar press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_ollieing:
                is_ollieing = True
                ollie_progress = 0
                angle = 0

    screen.fill((255, 255, 255))  # Fill the screen with white

    if is_ollieing:
        # Further slow down the increment for a more gradual rise
        ollie_progress += 0.25  # Very slow increment for gradual rise

        # Simulate front lifting
        if ollie_progress <= 20:
            angle = -ollie_progress * 1.2  # Tilt up gently
        # Simulate leveling out at the peak
        elif ollie_progress <= 40:
            angle = -(20 - (ollie_progress - 20)) * 1.2
        # Simulate coming back down
        else:
            angle = 0
            if ollie_progress > 60:  # Extend duration before resetting
                is_ollieing = False  # Reset ollie

        skateboard_img = pygame.transform.rotate(skateboard_img_original, angle)

    else:
        skateboard_img = skateboard_img_original

    # Adjust vertical position for a more gradual rise
    vertical_pos = original_y
    if ollie_progress > 0 and ollie_progress <= 40:
        vertical_movement = (40 - abs(20 - ollie_progress)) * 2  # Slower, more gradual rise
        vertical_pos -= vertical_movement
    elif ollie_progress > 40:
        vertical_pos = original_y  # Ensure it returns to the original position gently

    # Draw the skateboard
    img_rect = skateboard_img.get_rect(center=(skateboard_pos[0], vertical_pos))
    screen.blit(skateboard_img, img_rect)

    pygame.display.flip()  # Update the display

# Quit Pygame
pygame.quit()
sys.exit()
