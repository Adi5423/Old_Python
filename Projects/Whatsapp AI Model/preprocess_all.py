import json
import re

def preprocess_chat_data(input_file):
    with open(input_file, "r", encoding="utf-8") as infile:
        lines = infile.readlines()

    data = []
    conversation = {}

    for line in lines:
        speaker, message = extract_speaker_and_message(line)
        if speaker:
            # Remove the timestamp and whitespaces before the name
            speaker = re.sub(r'^\d{2}/\d{2}/\d{2},\s+\d{1,2}:\d{1,2}\s+', '', speaker)
            conversation = {"speaker": speaker, "message": message}
            data.append(conversation)

    return data

def extract_speaker_and_message(line):
    pattern = r"^(?P<speaker>.*?):\s*(?P<message>.*)$"
    match = re.match(pattern, line)
    if match:
        speaker = match.group("speaker").strip()
        message = match.group("message").strip()
        return speaker, message
    else:
        # Return a default speaker name and te original line as the message
        return "Unknown", line

input_files = [
    "D:/Python/Projects/Whatsapp AI Model/Dataset/WhatsApp Chat with Naina Avadh....txt",
    "D:/Python/Projects/Whatsapp AI Model/Dataset/WhatsApp Chat with Anushka Mishra ✨.txt",
    "D:/Python/Projects/Whatsapp AI Model/Dataset/WhatsApp Chat with Arohi Lps Prsnl💙.txt",
    "D:/Python/Projects/Whatsapp AI Model/Dataset/WhatsApp Chat with Arsh💌 Amritsar.txt",
    "D:/Python/Projects/Whatsapp AI Model/Dataset/WhatsAppChat with Bandaid 🩹.txt",
    "D:/Python/Projects/Whatsapp AI Model/Dataset/WhatsApp Chat with Chuwii 👻.txt",
    "D:/Python/Projects/Whatsapp AI Model/Dataset/WhatsApp Chat with Nikita Lps.txt",
    "D:/Python/Projects/Whatsapp AI Model/Dataset/WhatsApp Chat with Purnima LPS 10.txt",
    # Add more input file paths here
]

for input_file in input_files:
    data = preprocess_chat_data(input_file)
    output_file = f"preprocessed_data_{input_file.split('/')[-1].split('.')[0]}.json"
    with open(output_file, "w", encoding="utf-8-sig") as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)