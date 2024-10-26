'''
import subprocess
import pandas as pd


def check_threats_in_audio(transcribed_text):
    detected_threats = []
    for word in threatening_words:
        if word.lower() in transcribed_text:
            detected_threats.append(word)
    if detected_threats:
        print(f"Threats detected: {', '.join(detected_threats)} found in the audio.")
        return True
    else:
        print("No threats detected in the audio.")
        return False
    

# Step 1: Run the sound recording script
subprocess.run(['python', 'sound record.py'])

# Step 2: Run the transcription script and capture the output
result = subprocess.run(['python', 'transcript.py'], capture_output=True, text=True)
transcribed_text = result.stdout.strip()  # Get the transcribed text and remove any extra whitespace
if isinstance(transcribed_text, float):
    transcribed_text = str(transcribed_text)
transcribed_text =  transcribed_text.lower()
print(transcribed_text)

# Step 3: Check if the transcribed text is in the CSV file
def check_text_in_csv(text, csv_file):
    # Read the CSV file
    df = pd.read_csv(csv_file)
    
    # Check if the transcribed text is in any of the columns
    for column in df.columns:
        if df[column].astype(str).str.contains(text, case=False).any():
            return True
    return False



# Specify the CSV file name
csv_file = 'all_data.csv'


def load_threatening_words(csv_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file, header=None)  # Assuming no header
    # Flatten the DataFrame to a list of words/phrases
    return df[0].tolist()

def check_threatening_words(transcribed_text, threatening_words):
    for word in threatening_words:
        if word.lower() in transcribed_text.lower():  # Case insensitive check
            return True, word  # Return the found word
    return False, None

threatening_words = load_threatening_words(csv_file)

is_threatening, found_word = check_threatening_words(transcribed_text, threatening_words)

if is_threatening:
    print(f"The transcribed text contains a threatening word: '{found_word}'.")
else:
    print("The transcribed text does not contain any threatening words.")
'''
