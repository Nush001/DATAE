#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame
import random
import time


# In[2]:


# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Optimized Sorting Visualization")

# Colors (Soft and visually appealing)
BACKGROUND_COLOR = (40, 40, 40)
BAR_COLOR = (100, 200, 255)
ACTIVE_COLOR = (255, 100, 100)
COMPLETED_COLOR = (100, 255, 100)
TEXT_COLOR = (255, 255, 255)

# Font for instructions
font = pygame.font.SysFont('Arial', 20)

# Number of bars and their width
NUM_BARS = 100  # Adjust number of bars
BAR_WIDTH = WIDTH // NUM_BARS


# In[ ]:


# Create random array
def generate_array():
    return [random.randint(20, HEIGHT - 20) for _ in range(NUM_BARS)]

# Function to render text on screen
def render_text(text, position, color=TEXT_COLOR):
    label = font.render(text, True, color)
    screen.blit(label, position)

# Draw bars on the screen
def draw_bars(array, color_positions=None):
    screen.fill(BACKGROUND_COLOR)
    
    for i, height in enumerate(array):
        color = BAR_COLOR
        if color_positions and i in color_positions:
            color = color_positions[i]
        pygame.draw.rect(screen, color, (i * BAR_WIDTH, HEIGHT - height, BAR_WIDTH - 2, height))
    
    pygame.display.update()

# Sorting algorithms

# Selection Sort
def selection_sort(array):
    for i in range(len(array)):
        min_idx = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_idx]:
                min_idx = j
            if (j % 10 == 0 or j == len(array) - 1):  # Update every 10 iterations or last iteration
                draw_bars(array, {i: ACTIVE_COLOR, min_idx: COMPLETED_COLOR, j: TEXT_COLOR})
                yield True
        
        array[i], array[min_idx] = array[min_idx], array[i]
        draw_bars(array, {i: COMPLETED_COLOR})
        yield True

# Bubble Sort
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
            if (j % 10 == 0 or j == n - i - 2):  # Update every 10 iterations or last iteration
                draw_bars(array, {j: ACTIVE_COLOR, j + 1: COMPLETED_COLOR})
                yield True

# Main function
def main():
    running = True
    clock = pygame.time.Clock()
    FPS = 100  # Increased frame rate for faster updates

    array = generate_array()
    sorting = False
    sort_generator = None
    start_time = None
    sort_time = 30  # Time limit for sorting (seconds)

    while running:
        screen.fill(BACKGROUND_COLOR)
        draw_bars(array)
        
        render_text("Press 1 for Selection Sort", (10, 10))
        render_text("Press 2 for Bubble Sort", (20, 40))
        render_text("Press 0 for New Array", (10, 70))
        render_text("Press q to Quit", (10, 100))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 and not sorting:
                    sort_generator = selection_sort(array)
                    sorting = True
                    start_time = time.time()
                if event.key == pygame.K_2 and not sorting:
                    sort_generator = bubble_sort(array)
                    sorting = True
                    start_time = time.time()
                if event.key == pygame.K_0 and not sorting:
                    array = generate_array()
                if event.key == pygame.K_q:
                    running = False

        if sorting:
            current_time = time.time()
            if current_time - start_time >= sort_time:  # Check if sorting time exceeded
                sorting = False
                continue

            try:
                next(sort_generator)
            except StopIteration:
                sorting = False

        clock.tick(FPS)  # Control the speed of visualization

    pygame.quit()

if __name__ == "__main__":
    main()


# In[ ]:




