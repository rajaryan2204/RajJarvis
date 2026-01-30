import subprocess
import webbrowser


# Known Apps (Mac)
APPS = {
    "safari": "Safari",
    "chrome": "Google Chrome",
    "google chrome": "Google Chrome",
    "spotify": "Spotify",
    "notes": "Notes",
    "calculator": "Calculator",
    "terminal": "Terminal",
    "whatsapp": "WhatsApp",
    "vlc": "VLC",
    "discord": "Discord"
}


# Popular websites
WEBSITES = {
    "youtube": "https://www.youtube.com",
    "google": "https://www.google.com",
    "instagram": "https://www.instagram.com",
    "facebook": "https://www.facebook.com",
    "amazon": "https://www.amazon.in",
    "flipkart": "https://www.flipkart.com",
    "twitter": "https://twitter.com",
    "x": "https://twitter.com",
    "gmail": "https://mail.google.com",
    "chatgpt": "https://chat.openai.com"
}


def open_app(app):

    subprocess.run(["open", "-a", app], check=False)
    print("Opened app:", app)


def close_app(app):

    subprocess.run(
        ["osascript", "-e", f'tell application "{app}" to quit'],
        check=False
    )
    print("Closed app:", app)


def open_website(url):

    webbrowser.open(url)
    print("Opened website:", url)


def find_and_open(cmd):

    cmd = cmd.lower()

    # CLOSE APP
    if "close" in cmd or "quit" in cmd:

        for key in APPS:
            if key in cmd:
                close_app(APPS[key])
                return True


    # OPEN APP
    if "open" in cmd:

        for key in APPS:
            if key in cmd:
                open_app(APPS[key])
                return True


        # OPEN WEBSITE
        for key in WEBSITES:
            if key in cmd:
                open_website(WEBSITES[key])
                return True


    return False
