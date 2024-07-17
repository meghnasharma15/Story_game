# Interactive Story Game

Welcome to the Interactive Story Game! This project is a text-based interactive story game created using Python and Pygame.

## Features

- **Text-Based Story**: Navigate through a series of choices to experience different story paths.
- **Visuals**: Display images that correspond to different parts of the story.
- **Sound**: Background music and sound effects to enhance the experience.
- **Character Stats**: Track character stats and inventory throughout the game.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/interactive-story-game.git
    cd interactive-story-game
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment**:

    - **Windows**:
      ```sh
      venv\Scripts\activate
      ```
    - **MacOS/Linux**:
      ```sh
      source venv/bin/activate
      ```

4. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Run the game**:
    ```sh
    python game.py
    ```

2. **Controls**:
    - **1**: Select the first choice.
    - **2**: Select the second choice.

## Story File Format

The story is defined in a JSON file (`story.json`). Each node in the story contains a description, choices, optional effects, and an optional image. Below is an example structure of a story node:

```json
{
    "start": {
        "description": "You find yourself in a dark forest. There are two paths in front of you.",
        "choices": {
            "1": {"text": "Take the left path", "next": "left_path"},
            "2": {"text": "Take the right path", "next": "right_path"}
        },
        "image": "forest.png"
    },
    ...
}
