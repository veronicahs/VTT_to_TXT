import os

def convert_vtt_to_txt(vtt_content):
    # Remove timestamps and formatting from VTT content
    lines = vtt_content.splitlines()
    txt_lines = []
    for line in lines:
        # Only add the line if it's not empty and does not contain a timestamp
        if line and not line.startswith("NOTE") and not line[0].isdigit():
            txt_lines.append(line)
    return "\n".join(txt_lines)

def process_vtt_files(main_folder):
    # Create a new folder for all txt files
    captions_txt_folder = os.path.join(main_folder, "captions - txt")
    os.makedirs(captions_txt_folder, exist_ok=True)

    for section in os.listdir(main_folder):
        section_path = os.path.join(main_folder, section)

        # Check if it's a directory
        if os.path.isdir(section_path):
            # Create a "section XX - txt" folder inside the captions - txt folder
            txt_folder_name = f"{section} - txt"
            txt_folder = os.path.join(captions_txt_folder, txt_folder_name)
            os.makedirs(txt_folder, exist_ok=True)

            for file in os.listdir(section_path):
                if file.endswith('.vtt'):
                    vtt_file_path = os.path.join(section_path, file)
                    with open(vtt_file_path, 'r', encoding='utf-8') as vtt_file:
                        vtt_content = vtt_file.read()

                    # Convert VTT content to TXT
                    txt_content = convert_vtt_to_txt(vtt_content)
                    txt_file_name = os.path.splitext(file)[0] + '.txt'
                    txt_file_path = os.path.join(txt_folder, txt_file_name)

                    # Save the TXT file
                    with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
                        txt_file.write(txt_content)
                    print(f'Converted {vtt_file_path} to {txt_file_path}')

if __name__ == '__main__':
    main_folder = 'captions'  # Change this to your main folder path if needed
    process_vtt_files(main_folder)
