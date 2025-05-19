# MonkeyType Typing Bot

This Python script automates logging in and typing on [MonkeyType](https://monkeytype.com) using Playwright.

---

## Features

* Handles cookie consent popup by clicking **Reject** automatically.
* Optional login support by entering username and password.
* Waits for page navigation after login.
* Types words automatically on the MonkeyType typing test.
* Optionally limits typing speed by specifying a target word count.
* Works in headed mode to show browser UI.

---

## ScreeShots

![Screenshot from 2025-05-19 15-12-12](https://github.com/user-attachments/assets/676778e6-c613-4910-b5ad-26c6d76e93f4)

After Setting the Typing Speed:

![Screenshot from 2025-05-19 15-17-17](https://github.com/user-attachments/assets/3d162973-961f-43ba-8a65-4be444572bb6)

---

## Requirements

* Python 3.7+
* Playwright Python package

---

## Installation

1. Install Playwright and its browsers:

```bash
>> pip install playwright
```
```bash
>> playwright install
```

2. Save the script (e.g., `monkeytype_bot.py`).

---

## Usage

Run the script:

```bash
>> python monkeytype_bot.py
```

* When prompted, choose whether to log in (`y` or `n`).
* If logging in, enter your username and password.
* Choose whether to set a particular typing speed (`y` or `n`).
* If yes, enter the desired speed as an integer (word count target).
* The bot will automatically type words on the page.
* Press Enter to stop the script after the test.

---

## Notes

* The script opens a Chromium browser window (not headless) so you can watch the bot.
* Make sure your credentials are correct for login to work.
* Typing speed control approximates the number of words typed.
* If the Speed is too high, it will invalidate the WPM and not add it as a legit test.

