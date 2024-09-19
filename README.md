#Sorting Visualization Project

## Overview
This project provides a visual representation of two classic sorting algorithms: Selection Sort and Bubble Sort. Using Pygame, it creates a graphical interface where you can observe how these algorithms sort an array of bars, with real-time updates and customizable sorting durations.

## Features
Sorting Algorithms: Visualizes Selection Sort and Bubble Sort.
Interactive Controls: Allows users to start sorting, generate new arrays, and quit the program.
Performance Monitoring: Includes a time limit for sorting to prevent indefinite runs.
Installation
To run this project, ensure you have Python and Pygame installed. You can install the required Python library using pip:

bash
Copy code
pip install pygame
Usage
Clone the Repository:

bash
Copy code
git clone https://github.com/yourusername/sorting-visualization.git
Navigate to the Project Directory:

bash
Copy code
cd sorting-visualization
Run the Script:

bash
Copy code
python sort_visualization.py
Replace sort_visualization.py with the filename of your script if different.

## Controls:

Press 1: Start Selection Sort.
Press 2: Start Bubble Sort.
Press 0: Generate a new random array.
Press q: Quit the program.

## Code Description
Initialization:

Sets up Pygame and defines screen dimensions, colors, and fonts.
Initializes an array of random heights to be visualized.
Functions:

generate_array(): Generates a random array of heights for the bars.
render_text(text, position, color): Renders instructional text on the screen.
draw_bars(array, color_positions): Draws the bars on the screen, optionally using different colors for specific bars.
Sorting Algorithms:

selection_sort(array): Implements Selection Sort with visualization updates.
bubble_sort(array): Implements Bubble Sort with visualization updates.
Main Loop:

Handles user input and controls sorting processes.
Updates the display and manages sorting timing with a limit.
Contribution
Feel free to fork this repository and submit pull requests with improvements or bug fixes. Please ensure your code adheres to the existing style and includes appropriate comments.
