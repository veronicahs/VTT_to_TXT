import os
import re

def convert_vtt_to_txt():
    main_folder = 'captions'  # Main folder containing section folders with .vtt files

    # Check if the main folder exists
    if not os.path.exists(main_folder):
        print(f"Folder '{main_folder}' does not exist. Please create it and add your section folders with .vtt files.")
        return

    # Iterate through each subfolder (section) in the main folder
    for root, dirs, files in os.walk(main_folder):
        for filename in files:
            if filename.endswith('.vtt'):
                vtt_file_path = os.path.join(root, filename)
                # Create the output .txt file path in the same section folder
                txt_file_path = os.path.join(root, filename.replace('.vtt', '.txt'))

                with open(vtt_file_path, 'r', encoding='utf-8') as vtt_file:
                    # Read the contents and process the text
                    content = vtt_file.read()
                    # Remove VTT formatting (timestamps and cues)
                    text_only = re.sub(r'(?<=\n)\d{1,2}:\d{2}:\d{2}\.\d{3} --> \d{1,2}:\d{2}:\d{2}\.\d{3}\n?', '', content)
                    text_only = re.sub(r'\n{2,}', '\n', text_only)  # Remove extra newlines
                    text_only = text_only.strip()  # Remove leading/trailing whitespace

                # Write the cleaned text to a .txt file in the same section folder
                with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
                    txt_file.write(text_only)

    print(f"Conversion complete! All .txt files are saved in their respective section folders within: {main_folder}")

# Run the function
convert_vtt_to_txt()
