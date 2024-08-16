# VTT to TXT Converter

A simple Python script that converts `.vtt` (WebVTT) files into `.txt` files. The script processes `.vtt` files stored in section folders within a main `captions` folder and saves the converted `.txt` files in their respective section folders.

## Project Structure

<img width="92" alt="image" src="https://github.com/user-attachments/assets/b6270ca1-eb9e-4fef-b6ca-7d373385aee0">

captions/ 
         ├── section 01/ │ ├── example1.vtt │ ├── example2.vtt 
         ├── section 02/ │ ├── example3.vtt │ ├── example4.vtt 
         └── section 03/ ├── example5.vtt ├── example6.vtt


## Features

- Converts `.vtt` files to `.txt` format.
- Maintains the original folder structure, saving `.txt` files in the same section folder as the original `.vtt` files.
- Removes timestamps and any other formatting from the `.vtt` files.

## Requirements

- **Python 3.x**: Make sure you have Python installed on your machine.
- No additional libraries are required as the script uses built-in Python modules.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/vtt-to-txt-converter.git
   cd vtt-to-txt-converter

2. Create a folder named captions in the project directory.

3. Within the captions folder, create section folders (e.g., section 1, section 2, section 3) and place your .vtt files inside these folders.

4. Open the terminal and run the script:

   ```bash
   python convert_vtt_to_txt.py

5. The converted .txt files will be saved in their respective section folders.

## Contributing

If you have suggestions for improvements or find any issues, feel free to open an issue or submit a pull request.

## Contact
For any inquiries, please reach out to veronicahernandezphd@gmail.com
