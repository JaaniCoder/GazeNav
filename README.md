# GazeNav

**GazeNav** is a Python project that enables controlling a computer mouse using eye movements. Leveraging libraries such as OpenCV, MediaPipe, and PyAutoGUI, this project provides a unique and innovative way to interact with your computer by tracking eye movements and using blinks to simulate mouse clicks.

## Features

- **Eye Movement Tracking:** Move the cursor by shifting your eyes.
- **Blink Detection:** Click by blinking your left eye.
- **Real-Time Interface:** Provides an intuitive interface for interacting with your computer using eye movements.

## Installation

To get started with GazeNav, you need to have Python installed on your system. Follow these steps to set up the project:

1. **Clone the Repository**

   git clone https://github.com/JaaniCoder/GazeNav.git
   cd GazeNav

2. **Create a Virtual Environment (optional but recommended)**

   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install Dependencies**

   pip install -r requirements.txt

   The `requirements.txt` file includes the following dependencies:
   - `opencv-python`
   - `mediapipe`
   - `pyautogui`

## Usage

1. **Run the GazeNav Script**

   python main.py

2. **Adjust Settings (if necessary)**

   You can tweak the parameters in `gaze_nav.py` to fit your preferences and improve accuracy.

3. **Use the Interface**

   - **Move Cursor:** Shift your eyes to control the cursor's movement.
   - **Click:** Blink your left eye to perform a click.

## Project Structure

- **`main.py`**: Main script for running the eye-controlled mouse interface.
- **`requirements.txt`**: List of required Python packages.
- **`README.md`**: This file.

## Contributing

Feel free to contribute to GazeNav by submitting issues or pull requests. If you have suggestions for improvements or new features, please let me know!

1. **Fork the Repository**
2. **Create a New Branch**

   git checkout -b feature/YourFeatureName

3. **Commit Your Changes**

   git commit -am 'Add new feature'

4. **Push to the Branch**

   git push origin feature/YourFeatureName

5. **Create a New Pull Request**

   Visit [GitHub](https://github.com/JaaniCoder/GazeNav) and create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **OpenCV:** For image processing and computer vision capabilities.
- **MediaPipe:** For efficient and robust eye tracking.
- **PyAutoGUI:** For simulating mouse movements and clicks.
