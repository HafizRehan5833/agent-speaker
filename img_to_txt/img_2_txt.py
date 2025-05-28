# from PIL import Image
# import pytesseract

# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# print("Done path")
# # Optional: Set tesseract path if it's not in your system's PATH
# # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# # Load the image
# image = Image.open("img_to_txt\Screenshot 2025-05-16 121647.png")  # replace with your image path

# # Use pytesseract to extract text
# text = pytesseract.image_to_string(image)

# print("Extracted Text:")
# print(text)


from PIL import Image
import pytesseract
import pandas as pd

# Set the tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

print("Done setting path")

# Load the image
image = Image.open(r"img_to_txt\Screenshot 2025-05-16 122427.png")  # Use raw string for path

# Extract text
text = pytesseract.image_to_string(image)

print("Extracted Text:")
print(text)

# Prepare data for Excel: create a DataFrame with one column 'Text'
df = pd.DataFrame([text], columns=['ExtractedText'])

# Save DataFrame to Excel file (it will create or overwrite 'extracted_text.xlsx')
df.to_excel('img_to_txt\extracted_text.xlsx', index=False)

print("Text saved to 'extracted_text.xlsx'")
