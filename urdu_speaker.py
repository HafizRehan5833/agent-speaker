from gtts import gTTS
import os

text = input("Enter the text in Urdu and q for exit: ")
if text.lower() != "q":
    tts = gTTS(text, lang="ur")

    # Ensure directory exists
    output_dir = "urdu_files"
    os.makedirs(output_dir, exist_ok=True)

    # Save the speech file
    tts.save(os.path.join(output_dir, "urdu_speech.wav"))
    print("Speech saved successfully!")
else:
    print("Exiting...")  #TODO: This will run when exit
    exit()

    

 