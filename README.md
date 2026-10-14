# 🎙️ AI Voice Assistant with Python

A Python-based AI Voice Assistant that listens to voice commands, responds using text-to-speech, opens websites, tells the current time, plays local music, and searches for weather information using Google.

## ✨ Features

- 🗣️ **Speech Recognition:** Converts spoken commands into text using Google's speech recognition service.
- 🔊 **Text-to-Speech:** Responds verbally using the `pyttsx3` library.
- 👋 **Smart Greeting:** Greets the user according to the current time of day.
- 🕒 **Time Information:** Announces the current time.
- ▶️ **Website Navigation:** Opens YouTube and Google through voice commands.
- 🎵 **Music Playback:** Plays a randomly selected file from the local music directory.
- 🌦️ **Weather Search:** Opens Google weather results for a specified city.
- 🔎 **Web Search:** Searches Google automatically when a command is not recognized as a built-in action.
- 🛑 **Voice-Controlled Exit:** Stops the assistant when the user says commands such as "exit", "quit", or "stop".

## 🛠️ Technologies Used

| Technology           | Purpose                                             |
| -------------------- | --------------------------------------------------- |
| Python               | Core programming language                           |
| `speech_recognition` | Converts speech into text                           |
| `pyttsx3`            | Converts text into spoken responses                 |
| `datetime`           | Retrieves the current time and determines greetings |
| `webbrowser`         | Opens websites and Google search results            |
| `os`                 | Accesses local files and launches music             |
| `random`             | Selects a random music file                         |

## 📁 Project Structure

```text
AI-Voice-Assistant/
├── assistant.py
├── requirements.txt
└── README.md
```

## ⚙️ Prerequisites

Before running the project, install:

- Python 3.9 or later
- A working microphone
- Speakers or headphones
- An internet connection for online speech recognition and web searches

**Note:** The assistant uses `pyttsx3.init('sapi5')`, which is intended for Windows' Speech API. The music playback implementation also uses `os.startfile()`, which is Windows-specific.

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd AI-Voice-Assistant
```

Replace `<YOUR_GITHUB_REPOSITORY_URL>` with your repository's URL.

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

Create a `requirements.txt` file containing:

```text
SpeechRecognition
pyttsx3
PyAudio
```

Then install the dependencies:

```bash
python -m pip install -r requirements.txt
```

If PyAudio installation fails, check the installation instructions for your Python version and operating system.

### 4. Configure the music directory

In `assistant.py`, locate:

```python
music_dir = "C:\\Users\\Public\\Music"
```

Change the path to the folder containing your music files. Ensure that the folder exists before running the assistant.

### 5. Run the assistant

```bash
python assistant.py
```

The assistant will greet you and start listening for voice commands.

## 🎤 Supported Voice Commands

| Voice command             | Action                                               |
| ------------------------- | ---------------------------------------------------- |
| "What is the time?"       | Announces the current time                           |
| "Open YouTube"            | Opens YouTube                                        |
| "Open Google"             | Opens Google                                         |
| "Play music"              | Plays a random file from the configured music folder |
| "Weather"                 | Asks for a city and opens Google weather results     |
| "Search Python tutorials" | Opens Google search results for the command          |
| "Exit" / "Quit" / "Stop"  | Closes the assistant                                 |

## 🔄 How It Works

1. **Initialization:** Sets up the speech engine and microphone recognizer.
2. **Greeting:** Identifies the current time and speaks an appropriate greeting.
3. **Listening:** Captures audio from the microphone.
4. **Recognition:** Sends the audio to Google's speech recognition service and receives recognized text.
5. **Command Processing:** Matches the recognized text against supported commands.
6. **Execution:** Performs the requested action, such as opening a website or playing music.
7. **Voice Response:** Provides spoken feedback to the user.
8. **Continuous Operation:** Repeats the process until an exit command is detected.

## ⚠️ Troubleshooting

- **Microphone not detected:** Check microphone permissions and confirm that the correct input device is connected.
- **Speech not recognized:** Speak clearly, reduce background noise, and check your internet connection.
- **Network error:** Google's speech recognition service requires internet connectivity.
- **No music files found:** Verify that the configured music directory exists and contains playable files.
- **Text-to-speech not working:** Confirm that Windows audio output is working and the SAPI5 speech engine is available.
- **PyAudio installation error:** Check compatibility with your installed Python version.

## 🔐 Privacy and Limitations

- Voice recognition uses Google's online speech recognition service, so captured audio may be transmitted to that service.
- The assistant currently relies on predefined command rules rather than a conversational AI model.
- Weather information is retrieved through Google search; the application does not directly call a dedicated weather API.
- The current implementation is designed primarily for Windows.

## 🔮 Future Enhancements

- Integrate a dedicated weather API for structured forecasts.
- Add an LLM-based conversational interface.
- Support reminders, alarms, and application launching.
- Add multilingual voice recognition and responses.
- Introduce improved error handling and configurable voice settings.
- Add a graphical user interface.

## 👨‍💻 Author

AZMEERA THARUN

Python Developer | AI Enthusiast

- GitHub: https://github.com/azmeeratharun
- Portfolio: https://azmeeratharunportfolio.vercel.app/

## 📄 License

This project is intended for educational and personal development purposes. You may add an MIT License if you want to distribute it under that license.
