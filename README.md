# Watcher of Friends Online

The script allows to get your currently online friends.

# How to Install

Python 3 should be already installed. 
Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```
Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.

# Example of usage

After you've installed the dependencies run script in terminal.
You'll be asked to input your login and your password. Your password will be hidden.

```bash
python vk_friends_online.py
Login: <your_vk_login>
Password: <your_vk_pass>
```
Output:
```bash
Now online:
Sherlok Holmes
Bill Gates
Sasha Grey
Sara Connor
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
