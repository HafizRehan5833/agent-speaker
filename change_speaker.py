import tts
import simpleaudio as sa

def speak(text):
    # Initialize TTS model
    tts_model = tts.TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)
    
    # Generate speech audio file
    tts_model.tts_to_file(text=text, file_path="output.wav")
    
    # Play the generated audio
    wave_obj = sa.WaveObject.from_wave_file("output.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()

if __name__ == "__main__":
    text_input = input("Enter text to speak: ")
    speak(text_input)
