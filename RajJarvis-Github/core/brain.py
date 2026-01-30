import webbrowser
import subprocess
import shutil

from core.speak import speak
from core.ai import ask_ai


# Check if app exists
def app_exists(app):

    return shutil.which(app) is not None


# Open App
def open_app(app):

    try:
        subprocess.Popen(["open", "-a", app])
        return True
    except:
        return False


# Close App
def close_app(app):

    try:
        subprocess.Popen([
            "osascript",
            "-e",
            f'tell application "{app}" to quit'
        ])
        return True
    except:
        return False



def process(command):

    command = command.lower().strip()


    # EXIT
    if "stop" in command or "exit" in command:
        speak("Goodbye boss")
        return "Goodbye boss"



    # CLOSE APP
    if command.startswith("close") or command.startswith("quit"):

        app = command.replace("close", "").replace("quit", "").strip()

        speak(f"Closing {app}")

        if close_app(app):
            return f"Closed {app}"
        else:
            speak("App not found")
            return "App not found"



    # OPEN ANYTHING
    if command.startswith("open"):

        target = command.replace("open", "").strip()

        speak(f"Opening {target}")


        # Try app first
        if open_app(target):
            return f"Opened {target}"


        # Try website
        if "." in target:

            url = "https://" + target.replace(" ", "")

            webbrowser.open(url)

            return f"Opened {url}"


        # Google fallback
        webbrowser.open(
            f"https://www.google.com/search?q={target}"
        )

        return f"Searching {target}"



    # YOUTUBE DIRECT
    if "youtube" in command:

        speak("Opening YouTube")

        webbrowser.open("https://youtube.com")

        return "Opened YouTube"



    # SEARCH
    if command.startswith("search"):

        query = command.replace("search", "").strip()

        speak("Searching " + query)

        webbrowser.open(
            f"https://www.google.com/search?q={query}"
        )

        return f"Searched {query}"



    # PLAY
    if command.startswith("play"):

        song = command.replace("play", "").strip()

        speak("Playing " + song)

        webbrowser.open(
            f"https://www.youtube.com/results?search_query={song}"
        )

        return f"Playing {song}"



    # AI fallback
    speak("Let me think")

    answer = ask_ai(command)

    speak(answer)

    return answer
