import tkinter as tk
import threading
import itertools

from core.voice import listen
from core.speak import speak
from core.brain import process


class JarvisUI:

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("RAJ JARVIS AI")
        self.root.geometry("700x500")
        self.root.configure(bg="black")

        # Title
        self.title_label = tk.Label(
            self.root,
            text="🤖 RAJ JARVIS",
            font=("Arial", 28, "bold"),
            fg="cyan",
            bg="black"
        )
        self.title_label.pack(pady=20)

        # Status
        self.status = tk.Label(
            self.root,
            text="Status: Idle",
            font=("Arial", 14),
            fg="white",
            bg="black"
        )
        self.status.pack()

        # Button
        start_btn = tk.Button(
            self.root,
            text="START JARVIS",
            font=("Arial", 14),
            bg="cyan",
            fg="black",
            width=15,
            height=2,
            command=self.start_jarvis
        )
        start_btn.pack(pady=20)

        # Log box
        self.log_box = tk.Text(
            self.root,
            width=70,
            height=12,
            bg="black",
            fg="lime",
            insertbackground="white"
        )
        self.log_box.pack(pady=10)

        # Start glow
        self.glow_title()


    def glow_title(self):

        colors = itertools.cycle([
    "#00ffff",   # cyan
    "#00ff00",   # green
    "#ff00ff",   # purple
    "#ff3333",   # red
    "#3399ff",   # blue
    "#ffff00"    # yellow
])


        def animate():
            self.title_label.config(fg=next(colors))
            self.root.after(300, animate)

        animate()


    def log(self, text):

        self.log_box.insert("end", text + "\n")
        self.log_box.see("end")


    def start_jarvis(self):

        self.status.config(text="Status: Listening...")
        threading.Thread(target=self.run_jarvis, daemon=True).start()


    def run_jarvis(self):

        speak("Jarvis activated")
        self.log("Jarvis started")

        while True:

            cmd = listen().lower()

            if not cmd:
                continue

            self.log("You: " + cmd)

            if "stop" in cmd:
                speak("Goodbye")
                self.status.config(text="Status: Stopped")
                break

            process(cmd)


    def run(self):
        self.root.mainloop()


if __name__ == "__main__":

    app = JarvisUI()
    app.run()
