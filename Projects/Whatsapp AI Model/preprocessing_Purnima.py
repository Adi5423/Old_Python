import json

def preprocess_chat_data(input_file):
    with open(input_file, "r", encoding="utf-8") as infile:
        lines = infile.readlines()

    data = []
    conversation = {}

    for line in lines:
        speaker, message = extract_speaker_and_message(line)
        if speaker:
            conversation = {"speaker": speaker, "message": message}
            data.append(conversation)

    return data

def extract_speaker_and_message(line):
    start_index = 0
    end_index = None
    for i in range(start_index, len(line)):
        if line[i:i+5] == "Purnima" or line[i:i+3] == "Adi":
            end_index = i
            break
    if end_index is None:
        return None, None
    line = line[end_index:].strip()
    speaker = None
    message = None
    if line.startswith("Adi5423_:"):
        speaker = "You"
        message = line.replace("Adi5423_: ", "").strip()
    elif line.startswith("Purnima LPS 10"):
        speaker = "Purnima"
        message = line.replace("Purnima LPS 10: ", "").strip()
    return speaker, message

input_file = "D:/Python/Projects/Whatsapp AI Model/Dataset/WhatsApp Chat with Purnima LPS 10.txt"
data = preprocess_chat_data(input_file)

output_file = "preprocessed_data_Purnima.json"
with open(output_file, "w", encoding="utf-8-sig") as outfile:
    json.dump(data, outfile, ensure_ascii=False, indent=4)