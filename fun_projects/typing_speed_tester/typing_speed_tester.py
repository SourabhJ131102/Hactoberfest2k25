#!/usr/bin/env python3
"""
typing_speed_tester.py

A fun CLI-based typing speed test game.
Measures WPM (words per minute) and accuracy.
"""

import time
import random

SENTENCES = [
    "Hacktoberfest encourages open source contributions.",
    "Python makes programming enjoyable and efficient.",
    "Artificial intelligence is shaping the future of technology.",
    "GitHub is a great platform to share and collaborate on code.",
    "Typing fast requires practice, accuracy, and focus."
]

def calculate_accuracy(target: str, typed: str) -> float:
    correct = 0
    for t_char, y_char in zip(target, typed):
        if t_char == y_char:
            correct += 1
    return round((correct / len(target)) * 100, 2)

def typing_test():
    sentence = random.choice(SENTENCES)
    print("\n⚡ Typing Speed Tester ⚡")
    print("-" * 60)
    print(f"Type the following sentence exactly as shown:\n\n'{sentence}'")
    print("-" * 60)

    input("Press Enter when ready to start typing...")

    start_time = time.time()
    typed = input("\nStart typing: \n> ")
    end_time = time.time()

    elapsed_time = end_time - start_time
    words = len(sentence.split())
    wpm = (words / elapsed_time) * 60
    accuracy = calculate_accuracy(sentence, typed)

    print("\n⏱️ Time taken: {:.2f} seconds".format(elapsed_time))
    print("💨 Your typing speed: {:.2f} WPM".format(wpm))
    print("🎯 Accuracy: {:.2f}%".format(accuracy))

    if accuracy == 100:
        print("🔥 Perfect typing!")
    elif accuracy >= 80:
        print("✨ Great job! Keep practicing!")
    else:
        print("💪 Don't worry, keep practicing to improve your accuracy!")

if __name__ == "__main__":
    typing_test()
