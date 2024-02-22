# Sudoku Web App

This is a simple web application built with Flask for generating Sudoku boards. The app allows users to select the difficulty level (easy, medium, or hard) and the output format(UI or JSON). It then generates a Sudoku board accordingly. This can be used by services like Newspapers, magazines, games, etc to generate boards regularly.

## Getting Started

Follow the instructions below to set up and run the Sudoku web app on your local machine.

### Prerequisites

- Python 3.x
- Flask

### Installation

1. Clone the repository:

    ```bash
    git clone [https://github.com/your-username/sudoku-web-app.git](https://github.com/shivamgutgutia/sudokuBoardGenerator.git)
    cd sudoku-web-app
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. Run the Flask application:

    ```bash
    flask run
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000/`.

3. Choose a difficulty level (easy, medium, or hard) and start playing Sudoku!

## Project Structure

- **app.py**: The main Flask application file.
- **templates**: Folder containing HTML templates.
    - `selection.html`: Home page with difficulty selection buttons.
    - `output.html`: Template for displaying the Sudoku board for the selected difficulty.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Authors

- [@shivamgutgutia](https://www.github.com/shivamgutgutia)

## Contact

For any inquiries or feedback, please contact [Shivam Gutgutia](mailto:shivamgutgutia159@gmail.com).

