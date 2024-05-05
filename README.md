# sharepyfx
Telegram File Sharing Bot is a simple Python script that allows you to share files with your friends on Telegram effortlessly. With this bot, you can share individual files, share the content of text files as text messages, or share all files from a specific directory.

Certainly! Below is a Markdown file template for your project on GitHub:

# Telegram File Sharing Bot

Telegram File Sharing Bot is a simple Python script that allows you to share files with your friends on Telegram effortlessly. With this bot, you can share individual files, share the content of text files as text messages, or share all files from a specific directory.

# Used telegram bot
- [BotFather](https://t.me/BotFather)
- [UserInfo](https://t.me/userinfobot)

## Features

- Share individual files with your friends on Telegram.
- Share the content of text files as text messages.
- Share all files from a specific directory recursively.
- Simple and easy-to-use command-line interface.

## Usage

### Prerequisites

- Python 3.x
- Python Telebot library

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/telegram-file-sharing-bot.git
```

2. Install the required Python Telebot library:

```bash
pip install pyTelegramBotAPI
```

### Usage Instructions

Run the script `sharefx.py` with the appropriate options:

- `-h`: Display the help menu.
- `-all <directory>`: Share all files from the specified directory.
- `-c <file_path>`: Share the content of the specified text file as a text message.
- `-f <file_path>`: Share the specified file.

Example usages:

```bash
python3 sharefx.py -all ~/Documents
python3 sharefx.py -c ~/Documents/example.txt
python3 sharefx.py -f ~/Pictures/photo.jpg
```


## Acknowledgements

- The need for a simple file-sharing solution on Telegram inspired this project.
