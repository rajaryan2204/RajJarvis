import webview
import threading
import os
import sys

from core.voice import listen
from core.speak import speak
from core.brain import process


# For PyInstaller path
def resource_path(path):
    try:
        base = sys._MEIPASS
    except:
        base = os.path.abspath(".")
    return os.path.join(base, path)


class JarvisAPI:

    def __init__(self):
        self.running = False
        self.window = None


    def start_jarvis(self):

        if self.running:
            return

        self.running = True

        threading.Thread(
            target=self.loop,
            daemon=True
        ).start()


    def loop(self):

        speak("Jarvis activated")

        # Show on UI
        if self.window:
            self.window.evaluate_js(
                'addMessage("System","Jarvis Activated")'
            )

        while self.running:

            cmd = listen()

            if not cmd:
                continue

            cmd = cmd.lower()

            print("You:", cmd)


            # Show user voice as text
            if self.window:
                safe_cmd = cmd.replace('"', "'")

                self.window.evaluate_js(
                    f'addMessage("You","{safe_cmd}")'
                )


            # Stop command
            if "stop" in cmd or "exit" in cmd:

                speak("Goodbye boss")

                if self.window:
                    self.window.evaluate_js(
                        'addMessage("Jarvis","Goodbye boss")'
                    )

                self.running = False
                break


            # Process command
            reply = process(cmd)


            # Show reply on UI
            if reply and self.window:

                safe_reply = reply.replace('"', "'")

                self.window.evaluate_js(
                    f'addMessage("Jarvis","{safe_reply}")'
                )



def main():

    api = JarvisAPI()

    html = resource_path("ui/web/index.html")

    window = webview.create_window(
        "RAJ JARVIS 🤖",
        html,
        js_api=api,
        width=1000,
        height=700,
        resizable=True
    )

    api.window = window


    # Auto start mic after window loads
    def start_after_load():
        api.start_jarvis()

    threading.Timer(1, start_after_load).start()


    webview.start()



if __name__ == "__main__":

    print("=== JARVIS STARTING ===")

    main()
