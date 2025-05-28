import pandas as pd
from gtts import gTTS
import os

file_path = "perveen_shakir\pervenn_shakir.xlsx"
df = pd.read_excel(file_path)

df.columns = df.columns.str.strip()
required_columns = ["GUID", "left_verse", "right_verse"]
df = df[required_columns]

output_dir = "perveen_shakir\\perveenn_shakir_audio_files"
os.makedirs(output_dir, exist_ok=True)

# Generate merged audio files
for index, row in df.iterrows():
    left_text = str(row["left_verse"]).strip()
    right_text = str(row["right_verse"]).strip()

    if right_text or left_text:
        combined_text = ""
        if right_text:
            combined_text += right_text + "۔ "  # Urdu period for pause
        if left_text:
            combined_text += left_text

        tts = gTTS(combined_text, lang="ur")
        combined_filename = f"{row['GUID']}_{index + 1:02}.mp3"
        tts.save(os.path.join(output_dir, combined_filename))
        print(f"Saved: {combined_filename}")
