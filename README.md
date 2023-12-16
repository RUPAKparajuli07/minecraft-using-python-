## Documentation for the Minecraft-style Game

### Overview

This code is a simple implementation of a Minecraft-style game using the Ursina game development framework. It includes a first-person perspective, a selection of block types, a hand with which to interact, and the ability to build and destroy blocks in the environment.

### Dependencies

Make sure you have Ursina installed to run this code. You can install it using:

```bash
pip install ursina
```

### Code Structure

The code consists of two parts. The first part is the main Minecraft-style game with blocks, a player, and a hand. The second part includes additional classes for testing cubes and buttons.

#### Main Game Code

1. **Initialization:**
   - Import necessary modules from Ursina.
   - Create an Ursina application instance.
   - Load textures for different block types, the skybox, and the arm texture.
   - Disable the FPS counter and exit button.

2. **Update Function:**
   - Check for keyboard input to change the active block type.
   - Handle left and right mouse button actions to build or destroy blocks.

3. **Voxel Class:**
   - Represents a block in the game.
   - Extends the `Button` class in Ursina.
   - Initializes with a specific texture and color.
   - Responds to left and right mouse clicks to build or destroy blocks.

4. **Sky Class:**
   - Represents the sky in the game.
   - Extends the `Entity` class.
   - Displays a textured sphere with double-sided rendering.

5. **Hand Class:**
   - Represents the player's hand.
   - Extends the `Entity` class.
   - Displays a textured model of an arm.
   - Adjusts position based on mouse input to simulate holding an item.

6. **Main Loop:**
   - Creates a grid of Voxel instances.
   - Initializes the FirstPersonController for player movement.
   - Creates instances of Sky and Hand.
   - Runs the Ursina application.

#### Additional Test Code

1. **Test_cube Class:**
   - Extends the `Entity` class.
   - Represents a test cube with a textured appearance.
   - Initialized with a rotation.

2. **Test_button Class:**
   - Extends the `Button` class.
   - Represents a test button with different colors for highlighting and pressing.
   - Responds to left mouse clicks with a punch sound.

3. **Update Function:**
   - Moves the cube to the left when the 'a' key is held down.

4. **Basic Window and Entities:**
   - Creates an Ursina application.
   - Initializes a colored cube (Entity) and a textured cube (Test_cube).
   - Initializes a Test_button and associates a punch sound with left mouse clicks.

### How to Run

1. Install Ursina: `pip install ursina`
2. Copy the code into a Python file (e.g., `minecraft_game.py`).
3. Run the file: `python minecraft_game.py`

### Additional Notes

- Adjust the paths to the asset files based on your project structure.
- The code includes basic movement controls, block selection, and block placement.
- Feel free to extend and modify the code to add more features or customize the game elements.

Now you have a basic understanding of how the Minecraft-style game is structured and how to run it. Enjoy exploring and building in the virtual world!
