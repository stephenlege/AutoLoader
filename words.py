import pyautogui
import time
import random
import signal
import sys
import nltk
from nltk.corpus import brown
from nltk.tokenize import word_tokenize

# Download necessary NLTK data
nltk.download('brown')
nltk.download('punkt')

def generate_sentence():
    # Get a list of words from the Brown corpus
    words = brown.words()
    sentence_length = random.randint(5, 15)  # Random sentence length between 5 and 15 words
    sentence = ' '.join(random.choices(words, k=sentence_length))  # Generate a random sentence
    return sentence

def type_sentence(sentence):
    pyautogui.typewrite(sentence, interval=random.uniform(0.05, 0.2))
    pyautogui.press('enter')

# Function to handle cleanup on interrupt
def signal_handler(sig, frame):
    print("Interrupted! Cleaning up and exiting.")
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

# Start typing sentences every 3 minutes
while True:
    sentence = generate_sentence()
    type_sentence(sentence)
    time.sleep(180)  # Wait for 3 minutes (180 seconds)
