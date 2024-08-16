# VTT to TXT Converter

A simple Python script that converts `.vtt` (WebVTT) files into `.txt` files. The script processes `.vtt` files stored in section folders within a main `captions` folder and saves the converted `.txt` files in their respective section folders.

## Project Structure

<img width="92" alt="image" src="https://github.com/user-attachments/assets/b6270ca1-eb9e-4fef-b6ca-7d373385aee0">

captions/ ├── section 1/ │ ├── example1.vtt │ ├── example2.vtt ├── section 2/ │ ├── example3.vtt │ ├── example4.vtt └── section 3/ ├── example5.vtt ├── example6.vtt


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
