# tiktok_interaction.py
import random
import time

def get_random_comment():
    # Simulate random comments for the demo
    comments = [
        "Go Horse 1!",
        "Horse 2 for the win!",
        "Let's go Red!",
        "Blue is my favorite!",
    ]
    return random.choice(comments)

def listen_for_chat(callback):
    while True:
        time.sleep(random.randint(1, 3))
        comment = get_random_comment()
        print(f"New comment: {comment}")
        callback(comment)
