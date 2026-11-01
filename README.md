# Personal Book Manager
![Static Badge](https://img.shields.io/badge/Python-3.12%2B-blue)

A simple personal book manager written in Python. 

## Features
- Add multiple books
- Show books
- Save books
- Read saved books
- Admin Mode

## Requirements
Running the program requires the following:
- Python
- python-dotenv

## Installation
Install the required pacakges via the `requirements.txt` file:
```bash
python -m pip install -r requirements.txt
```

## Environment Setup
To run the program, you will have to first create a `.env` file in the project folder/directory.

Use the `.env.example` file as a template.

Add your admin password to the `.env` file as below:
```env
BOOK_MANAGER_ADMIN_PASSWORD=your_password_here
```

Replace `your_password_here` with your own admin password.

## Run the Program
Run the program using the main file:
```bash
python main.py
```

## Screenshot
![personal_book_manage_screenshot](images/screenshot.png)

## Demo
![personal_book_manage_demo](images/demo.gif)