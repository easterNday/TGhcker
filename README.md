# Telegram Phone Number Checker GUI

[![GitHub Stars](https://img.shields.io/github/stars/easterNday/TGhcker.svg?style=social)](https://github.com/easterNday/TGhcker)
[![GitHub Issues](https://img.shields.io/github/issues/easterNday/TGhcker.svg)](https://github.com/easterNday/TGhcker/issues)
[![License](https://img.shields.io/github/license/easterNday/TGhcker.svg)](https://github.com/easterNday/TGhcker/blob/master/LICENSE)

## Introduction

`Telegram Phone Number Checker GUI` is a user-friendly graphical interface application designed to help users verify the validity of phone numbers on the Telegram platform. By inputting API credentials and the phone number to be queried, the tool connects to the Telegram API, verifies the status of the specified number, and presents the result in a friendly JSON format.

## Features

- **Graphical Interface**: User-friendly, no command-line operations required.
- **Instant Feedback**: Query results are instantly displayed in the GUI.
- **Security Awareness**: Emphasizes input validation to enhance security.
- **Cross-Platform**: Built on Python and Tkinter, compatible with Windows, macOS, and Linux.

## Quick Start

### Install Dependencies

Make sure you have Python 3.6+ installed, then use pip to install the necessary dependencies:

```bash
pip install telegram-phone-number-checker
```

### Run the Project

Clone this repository locally:

```bash
git clone https://github.com/easterNday/TGhcker.git
cd TGhcker
```

Run the main script to start the application:

```bash
python main.py
```

## User Guide

Enter your Telegram phone number, API ID, API Hash, and the phone number to be queried in the GUI.
Click the "Confirm" button; the program will automatically verify the number and display the result.

### Note

- **Security Tips**: Do not disclose your API ID and API Hash in public.
- **API Limits**: Overuse may lead to Telegram API restrictions. Please manage your query frequency reasonably.

## Contributing

We warmly welcome your contributions! Whether it’s reporting issues, suggesting features, or submitting code, your support is valuable.

1. **Report Bugs**: Please submit issues on the Issues page.
2. **Feature Requests**: Similarly, submit new issues on the Issues page and label them as “enhancement”.
3. **Code Contributions**: Follow these steps:
   - Fork this repository.
   - Create a new branch (`git checkout -b feature/your-feature`).
   - Commit your changes (`git commit -am 'Add feature'`).
   - Push your branch to GitHub (`git push origin feature/your-feature`).
   - Create a new Pull Request.

## License

This project is licensed under the Apache 2.0 License. See the LICENSE file for details.
