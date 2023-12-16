## Minecraft-Style Game with Ursina

This repository contains the source code for a simple Minecraft-style game implemented using the Ursina game development framework. The game features a first-person perspective, block selection, and the ability to build and destroy blocks in the environment.

### Getting Started

1. **Install Ursina:**
   ```bash
   pip install ursina
   ```

2. **Run the Game:**
   - Copy the code from `minecraft_game.py` into a Python file.
   - Execute the file: `python your_file.py`

### Code Structure

The main game code is organized into several components:

- **Initialization:** Set up the Ursina application, load textures, and configure the environment.
  
- **Update Function:** Handle input and update the game state.

- **Voxel Class:** Represents a block in the game, allowing for building and destruction.

- **Sky Class:** Represents the sky in the game.

- **Hand Class:** Represents the player's hand and adjusts its position based on mouse input.

- **Main Loop:** Creates a grid of Voxel instances, initializes player controls, and runs the Ursina application.

Additionally, there is test code for cubes and buttons to demonstrate additional features.

### Test Code

- **Test_cube Class:** Represents a textured cube for testing.

- **Test_button Class:** Represents a button with highlighting and pressing effects for testing.

- **Update Function:** Moves a cube to the left when the 'a' key is held down.

### How to Contribute

1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m "Description of changes"`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

### Notes

- Adjust asset paths based on your project structure.
- The code is a starting point; feel free to customize and extend it.

### Acknowledgments

- This project utilizes the Ursina game development framework.

Enjoy exploring and building in this simple Minecraft-style game!
