import tkinter as tk
from tkinter import scrolledtext
import re
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

def preprocess_input(user_input):
    user_input = user_input.lower()
    user_input = re.sub(r'[^a-z\s]', '', user_input)
    return user_input

def get_response(user_input):
    processed_input = preprocess_input(user_input)
    tokens = word_tokenize(processed_input)

    if "hello" in tokens or "hi" in tokens:
        return "Hi there! How can I help you?"
    elif "how" in tokens and "you" in tokens:
        return "I'm just a bunch of code, but thanks for asking!"
    elif "what" in tokens and "name" in tokens:
        return "I'm PyChatter, your friendly chat assistant."
    elif "bye" in tokens:
        return "Goodbye! Have a great day!"
    elif "help" in tokens:
        return "I can assist you with simple queries. Just ask me anything!"
    elif "thank" in tokens:
        return "You're welcome! If you have more questions, feel free to ask."
    elif "what" in tokens and "song" in tokens:
        return "A great song to listen to is 'Shape of You' by Ed Sheeran!"
    elif "what" in tokens and "your" in tokens and "favorite" in tokens and "song" in tokens:
        return "I don't have a favorite, but 'Bohemian Rhapsody' by Queen is a classic!"
    elif "tell" in tokens and "joke" in tokens:
        return "Why did the computer go to the doctor? Because it had a virus!"
    elif "time" in tokens:
        return "I can't tell the time, but you can check your device!"
    elif "favorite" in tokens and "color" in tokens:
        return "I don't have a favorite color, but I like all of them!"
    elif "favorite" in tokens and "food" in tokens:
        return "I don't eat, but I hear pizza is a favorite among many!"
    elif "what" in tokens and "movie" in tokens:
        return "I don't watch movies, but I hear 'The Matrix' is a popular one!"
    elif "what" in tokens and "book" in tokens:
        return "I don’t read books, but I know '1984' by George Orwell is a classic!"
    elif "how" in tokens and "improve" in tokens and "coding" in tokens:
        return "Practice regularly, work on projects, and learn from online resources!"
    elif "tell" in tokens and "about" in tokens and "yourself" in tokens:
        return "I'm PyChatter, an AI assistant here to chat with you!"
    elif "what" in tokens and "is" in tokens and "data" in tokens and "science" in tokens:
        return "Data science is the field of study that combines statistics, computer science, and domain knowledge to extract insights from data."
    elif "what" in tokens and "is" in tokens and "blockchain" in tokens:
        return "Blockchain is a distributed ledger technology that enables secure and transparent transactions."
    elif "tell" in tokens and "fun" in tokens and "fact" in tokens:
        return "Did you know that octopuses have three hearts?"
    elif "how" in tokens and "can" in tokens and "I" in tokens and "build" in tokens and "confidence" in tokens:
        return "Set small, achievable goals, and celebrate your successes to build confidence over time."
    elif "what" in tokens and "is" in tokens and "artificial" in tokens and "intelligence" in tokens:
        return "Artificial intelligence is the simulation of human intelligence processes by machines."
    elif "what" in tokens and "is" in tokens and "machine" in tokens and "learning" in tokens:
        return "Machine learning is a subset of AI that enables systems to learn from data."
    elif "how" in tokens and "start" in tokens and "exercising" in tokens:
        return "Start with activities you enjoy and gradually increase your activity level."
    elif "what" in tokens and "is" in tokens and "mindfulness" in tokens:
        return "Mindfulness is the practice of being present and fully engaged in the moment."
    elif "how" in tokens and "improve" in tokens and "mental" in tokens and "health" in tokens:
        return "Consider practicing mindfulness, talking to someone you trust, or seeking professional help."
    elif "what" in tokens and "is" in tokens and "self" in tokens and "care" in tokens:
        return "Self-care refers to activities and practices that individuals engage in to maintain and enhance their well-being."
    elif "what" in tokens and "is" in tokens and "healthy" in tokens and "eating" in tokens:
        return "Healthy eating includes consuming a balanced diet rich in fruits, vegetables, lean proteins, and whole grains."
    elif "what" in tokens and "is" in tokens and "the" in tokens and "meaning" in tokens and "of" in tokens and "life" in tokens:
        return "The meaning of life is a philosophical question that varies for each individual!"
    elif "can" in tokens and "you" in tokens and "give" in tokens and "advice" in tokens:
        return "Sure! Always keep learning and stay curious!"
    else:
        return "I'm sorry, I don't understand that."

def send():
    user_input = user_input_entry.get()
    if user_input.lower() == "bye":
        response = "Goodbye! Have a great day!"
        text_area.config(state=tk.NORMAL)
        text_area.insert(tk.END, "You: " + user_input + "\n")
        text_area.insert(tk.END, "PyChatter: " + response + "\n")
        text_area.config(state=tk.DISABLED)
        user_input_entry.delete(0, tk.END)
        root.quit()
    else:
        response = get_response(user_input)
        text_area.config(state=tk.NORMAL)
        text_area.insert(tk.END, "You: " + user_input + "\n")
        text_area.insert(tk.END, "PyChatter: " + response + "\n")
        text_area.config(state=tk.DISABLED)
        user_input_entry.delete(0, tk.END)

root = tk.Tk()
root.title("PyChatter")

text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED)
text_area.grid(row=0, column=0, columnspan=2)

user_input_entry = tk.Entry(root, width=100)
user_input_entry.grid(row=1, column=0)

send_button = tk.Button(root, text="Send", command=send)
send_button.grid(row=1, column=1)

root.mainloop()
