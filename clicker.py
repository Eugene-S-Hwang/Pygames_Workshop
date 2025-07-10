import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Clicker Game")

# Set up font
font = pygame.font.Font(None, 36)

# Circle settings
circle_radius = 30
circle_color = (255, 0, 0)  # red

# Start with circle in random place
circle_x = random.randint(circle_radius, WIDTH - circle_radius)
circle_y = random.randint(circle_radius, HEIGHT - circle_radius)

# Score
score = 0

# Clock for controlling frame rate
clock = pygame.time.Clock()

running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            # Compute distance from click to center of circle
            distance = ((mouse_x - circle_x)**2 + (mouse_y - circle_y)**2) ** 0.5
            if distance <= circle_radius:
                # Clicked inside circle
                score += 1
                # Move circle to new random position
                circle_x = random.randint(circle_radius, WIDTH - circle_radius)
                circle_y = random.randint(circle_radius, HEIGHT - circle_radius)

    # Draw background
    screen.fill((255, 255, 255))  # white background

    # Draw circle
    pygame.draw.circle(screen, circle_color, (circle_x, circle_y), circle_radius)

    # Draw score
    text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Limit frames per second
    clock.tick(60)

pygame.quit()
