import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

# Show all available voices
voices = speaker.GetVoices()
print("Available voices:")
for i, voice in enumerate(voices):
    print(f"{i}: {voice.GetDescription()}")

# Select voice by number
user_input = input("Enter the number of the voice you want to use: ")

try:
    speaker.Voice = voices.Item(int(user_input))
except:
    print("Invalid selection. Using default voice.")

# Speak loop
while True:
    s = input("Enter the sentence to speak (or 'q' to quit): ")
    if s.lower() == "q":
        break
    speaker.Speak(s)
