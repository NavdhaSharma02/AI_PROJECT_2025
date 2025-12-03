import random
import pandas as pd
normal_sentences = [
    "I want to go home.",
    "Can we watch a movie tonight?",
    "This is a beautiful day.",
    "Thank you very much.",
    "How are you doing today?",
    "Please give me a moment.",
    "Let's go to the park.",
    "I really like this song.",
    "Where are you going?",
    "It is time to start working.",
    "I love programming in Python.",
    "She is reading a new book.",
    "We are planning a trip tomorrow.",
    "The weather feels amazing today.",
    "He forgot to bring his phone.",
    "I am excited to learn something new.",
    "Could you please repeat that?",
    "My favorite color is blue.",
    "I am feeling very happy.",
    "The internet connection is slow today."
]

# ✨ Step 2: Helper functions to create realistic stuttering
def add_repetition(word):
    # Example: w-want or I-I-I
    rep_count = random.choice([1, 2, 3])
    if len(word) > 2:
        return '-'.join([word[0]] * rep_count) + "-" + word
    else:
        return (word + "-") * rep_count + word

def add_prolongation(word):
    # Example: sssso or nnnnice
    if len(word) > 3:
        return word[0] * random.randint(2, 5) + word
    return word

def add_filler(sentence):
    # Example: "uh" or "um" randomly inserted
    fillers = ["uh", "um", "er"]
    words = sentence.split()
    insert_pos = random.randint(0, len(words)-1)
    words.insert(insert_pos, random.choice(fillers))
    return " ".join(words)

def stutterify(sentence):
    words = sentence.split()
    stuttered = []
    for w in words:
        if random.random() < 0.25:  # 25% chance to stutter a word
            choice = random.choice(['rep', 'prolong', 'skip'])
            if choice == 'rep':
                stuttered.append(add_repetition(w))
            elif choice == 'prolong':
                stuttered.append(add_prolongation(w))
            else:
                stuttered.append(w)
        else:
            stuttered.append(w)
    new_sentence = " ".join(stuttered)
    # 10% chance to add a filler
    if random.random() < 0.1:
        new_sentence = add_filler(new_sentence)
    return new_sentence

# Step 3: Generate dataset
data = []
for s in normal_sentences:
    for _ in range(5):  # Generate 5 variations of each sentence
        stuttered = stutterify(s)
        data.append({"stuttered_text": stuttered, "normal_text": s})

df = pd.DataFrame(data)
#  Step 4: Save to CSV
df.to_csv("stutter_text_dataset.csv", index=False, encoding='utf-8')
print(" Generated dataset saved as 'stutter_text_dataset.csv'")
print(df.sample(10))
