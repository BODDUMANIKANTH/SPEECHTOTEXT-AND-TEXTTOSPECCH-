import tkinter as tk
import pyttsx3
import speech_recognition as sr

def text_to_speech():
    text = text_entry.get()
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak something...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        text_entry.delete(0, tk.END)
        text_entry.insert(tk.END, text)
    except sr.UnknownValueError:
        print("Sorry, I could not understand.")
    except sr.RequestError as e:
        print("Sorry, an error occurred. {0}".format(e))

# Create the main window
window = tk.Tk()
window.title("Text-to-Speech & Speech-to-Text")
window.geometry("400x200")
# Create a label and entry for text input
text_label = tk.Label(window, text="Enter Text:")
text_label.pack()
text_entry = tk.Entry(window, width=40)
text_entry.pack()

# Create buttons for text-to-speech and speech-to-text
tts_button = tk.Button(window, text="Text-to-Speech", command=text_to_speech)
tts_button.pack()
stt_button = tk.Button(window, text="Speech-to-Text", command=speech_to_text)
stt_button.pack()

# Start the main event loop
window.mainloop()
