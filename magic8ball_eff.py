import random
import time
answers = ["Absolutely!", "No way, Jose!", "Go for it Tiger.", "Don't even think about it", "Isn't it obvious?"]

print("Welcome to the Magic 8 Ball game-use it to answer your questions...")
time.sleep(0.5)
question = input("Ask me for any advice and I'll help you out. Type in your question and then press Enter for an answer. ")
time.sleep(0.5)
print("shaking...\n"*4)

time.sleep(1)

print(answers[random.randint(0,4)])
