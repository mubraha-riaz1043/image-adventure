import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# Define the story structure
story = {
    "start": {
        "text": "You awaken in a misty forest. Two paths lie ahead:",
        "options": [("Follow the glowing path", "glowing_path"),
                    ("Enter the dark cave", "dark_cave")]
    },
    "glowing_path": {
        "text": "The glowing path lights up with strange runes. You see a friendly fox and a broken bridge.",
        "options": [("Follow the fox", "follow_fox"),
                    ("Try to cross the bridge", "cross_bridge")]
    },
    "dark_cave": {
        "text": "The cave echoes with whispers. You find a torch and a tunnel.",
        "options": [("Take the torch", "torch_path"),
                    ("Enter the tunnel blind", "blind_path")]
    },
    "follow_fox": {
        "text": "The fox leads you to a hidden grove where a tree whispers your name. You found a place of peace. 🌿",
        "options": []
    },
    "cross_bridge": {
        "text": "The bridge collapses and you fall into a ravine! Ouch. Your adventure ends here. 🌊",
        "options": []
    },
    "torch_path": {
        "text": "With the torch, you find ancient writings revealing your destiny. You were meant to protect the forest. 🔥",
        "options": []
    },
    "blind_path": {
        "text": "You stumble in darkness and find a glowing orb. It transports you to another realm. 🌀",
        "options": []
    }
}

encouragements = [
    "You're doing great! Keep going!",
    "Trust your instincts. Adventure awaits!",
    "Every choice is a new discovery.",
    "Be brave—this forest holds many secrets."
]

class StoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Forest of Echoes 🌲")
        self.current_node = "start"

        self.canvas = tk.Canvas(root, width=600, height=300, bg="white")
        self.canvas.pack()

        self.story_text = tk.Label(root, text="", wraplength=580, font=("Arial", 14))
        self.story_text.pack(pady=10)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack()

        self.image_label = tk.Label(root)
        self.image_label.pack()

        self.update_story()

    def update_story(self):
        node = story[self.current_node]
        self.canvas.delete("all")

        self.story_text.config(text=node["text"] + "\n\n" + random.choice(encouragements))

        for widget in self.button_frame.winfo_children():
            widget.destroy()

        for option_text, next_node in node.get("options", []):
            btn = tk.Button(self.button_frame, text=option_text, font=("Arial", 12),
                            command=lambda n=next_node: self.make_choice(n))
            btn.pack(pady=5, fill="x")

        # Show a different image for each scene (optional)
        self.show_image(self.current_node)

    def show_image(self, scene_name):
        try:
            img = Image.open(f"images/{scene_name}.png")  # Example: images/glowing_path.png
            img = img.resize((400, 200))
            photo = ImageTk.PhotoImage(img)
            self.image_label.config(image=photo)
            self.image_label.image = photo
        except:
            self.image_label.config(image="", text="")

    def make_choice(self, next_node):
        self.current_node = next_node
        self.update_story()

# Run the app
root = tk.Tk()
app = StoryGame(root)
root.mainloop()
