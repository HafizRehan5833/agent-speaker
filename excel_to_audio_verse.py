import pandas as pd
from gtts import gTTS
import os

file_path = "rehan_practice.xlsx"

df = pd.read_excel(file_path)

df.columns = df.columns.str.strip()

required_columns = ["GUID", "Left_B", "Right_B"]

df = df[required_columns]  

output_dir = "audio_files"
os.makedirs(output_dir, exist_ok=True)

# Generate audio files
for index, row in df.iterrows():
        guid = str(row["GUID"]).strip()  

        for col in required_columns:  
            text = str(row[col]).strip()  
        
        if text:  
            tts = gTTS(text, lang="ur")
            
            mp3_path = f"GUID_{guid}_verse_{index + 1}_{col}.wav"
            
            
            tts.save(os.path.join(output_dir, mp3_path))            
            print(f"Saved: {mp3_path}")
