# PDF to Audiobook Converter

## Project Information


**Course URL:** https://www.udemy.com/course/100-days-of-code/learn/practice/1251140#overview

## What This Project Does

This is a Python application that converts PDF files into audiobooks. The program reads the text content from any PDF file you provide and converts it into spoken audio that you can listen to. This is useful for people who prefer listening to content instead of reading, or for those who want to consume written content while doing other activities.

## How It Works

The application follows a simple process:

1. You provide the path to a PDF file on your computer
2. The program opens the PDF and extracts all the text from every page
3. The extracted text is then converted into speech using text-to-speech technology
4. The audio is saved as an audio file that you can play on any media player

## Features

**PDF Text Extraction:** The program can read and extract text from any text-based PDF file. It processes each page individually and combines all the text together.

**Text-to-Speech Conversion:** The extracted text is converted into natural-sounding speech using your computer's built-in speech engine. This works completely offline without requiring an internet connection.

**Cross-Platform Compatibility:** The application works on both Windows 11 and above, as well as Ubuntu 24.04 and above.

**User-Friendly Interface:** The program guides you through each step with clear instructions and progress updates.

**Customizable Output:** You can choose your own name for the output audio file.

**Error Handling:** The program includes comprehensive error checking to handle common issues like missing files or unreadable PDFs.

## System Requirements

**Operating Systems:**
- Windows 11 or newer
- Ubuntu 24.04 or newer

**Python Version:**
- Python 3.7 or higher

**Required Libraries:**
- pypdf (for reading PDF files)
- pyttsx3 (for text-to-speech conversion)

**Additional Requirements for Linux:**
- eSpeak or eSpeak-NG speech engine (usually pre-installed, but may need manual installation)

## Installation Instructions

### Step 1: Install Python

Make sure you have Python 3.7 or higher installed on your computer. You can check this by opening a terminal or command prompt and typing:

```
python --version
```

If Python is not installed, download it from the official Python website at python.org.

### Step 2: Install Required Libraries

Open a terminal or command prompt in the project folder and run:

```
pip install -r requirements.txt
```

This will automatically install all the necessary Python libraries.

### Step 3: Additional Setup for Linux Users

If you are using Ubuntu or another Linux distribution, you may need to install the eSpeak speech engine:

```
sudo apt-get update
sudo apt-get install espeak espeak-ng
```

Windows users do not need any additional setup as the speech engine is built into Windows.

## How to Use the Application

### Step 1: Open Terminal or Command Prompt

Navigate to the folder where you saved the application files.

### Step 2: Run the Program

Type the following command:

```
python text_to_voice.py
```

### Step 3: Provide the PDF File Path

When prompted, enter the full path to the PDF file you want to convert. For example:

On Windows:
```
C:\Users\YourName\Documents\mybook.pdf
```

On Linux:
```
/home/yourname/Documents/mybook.pdf
```

### Step 4: Choose Output File Name

Enter a name for your audiobook file, or press Enter to use the default name "audiobook.mp3".

### Step 5: Confirm and Convert

The program will show you a preview of the extracted text. If everything looks correct, confirm to proceed with the audio conversion.

### Step 6: Wait for Completion

The conversion process may take some time depending on the length of your PDF. The program will show you progress updates as it works.

### Step 7: Enjoy Your Audiobook

Once complete, you will find your audiobook file in the same folder as the program. You can play it using any media player.

## Important Limitations

**Text-Based PDFs Only:** This tool only works with PDFs that contain actual text. It cannot extract text from PDFs that are just scanned images of documents. If your PDF is a scanned image, you would need to use OCR (Optical Character Recognition) software first.

**Encrypted or Protected PDFs:** The application cannot process PDF files that are password-protected or encrypted.

**Speech Quality:** The quality of the audio depends on the text-to-speech engine available on your system. The speech may sound robotic compared to human narration.

**Processing Time:** Large PDF files with many pages will take longer to process. Be patient and let the program complete its work.

## Legal Information and Disclaimer

**DISCLAIMER:** This software is provided "as is" without warranty of any kind. The author is not responsible for any misuse of this software. Users are responsible for ensuring they have legal rights to convert and use any PDF files processed by this application.

**Legal Implications:**

Only use this tool with PDF files that you own or have explicit permission to convert.

Do not distribute converted audiobooks of copyrighted material without proper authorization.

This tool is intended for personal use only.

You must respect intellectual property rights and copyright laws at all times.

The author assumes no liability for any legal issues arising from the use or misuse of this software.

By using this application, you agree to use it responsibly and in compliance with all applicable laws.

## Troubleshooting

**Problem: The program says it cannot find the PDF file**

Solution: Make sure you typed the correct path to your PDF file. You can copy the full path by right-clicking on the file and selecting "Copy as path" (Windows) or using the file properties (Linux).

**Problem: No text was extracted from the PDF**

Solution: Your PDF might be image-based rather than text-based. Try opening the PDF and checking if you can select and copy text. If not, the PDF contains images and this tool will not work with it.

**Problem: The audio file is not created**

Solution: Make sure you have write permissions in the folder where you are running the program. Try running the program in a folder where you have full access rights.

**Problem: On Linux, I get an error about missing speech engine**

Solution: Install eSpeak using the command provided in the installation section above.

**Problem: The speech sounds too fast or too slow**

Solution: You can modify the speaking rate in the code by editing the line that says `engine.setProperty('rate', 150)`. Increase the number to make it faster, or decrease it to make it slower.

## File Structure

The project contains the following files:

**text_to_voice.py:** The main Python script that performs the PDF to audiobook conversion.

**requirements.txt:** A list of Python libraries required to run the application.

**license.dat:** Detailed information about the project license, third-party library credits, and legal disclaimers.

**README.md:** This file, containing comprehensive documentation about the project.

## Credits and Acknowledgments

This project was created as part of Angela Yu's "100 Days of Code: The Complete Python Pro Bootcamp" course on Udemy. Special thanks to Angela Yu for providing excellent Python education and project ideas.

The project uses the following free and open source libraries:

**pypdf:** A Python library for reading and extracting text from PDF files.

**pyttsx3:** A text-to-speech conversion library that works offline.

All third-party libraries are properly credited in the license.dat file included with this project.

## Support and Contributions

This is an educational project created for learning purposes as part of a coding course. It demonstrates fundamental Python programming concepts including file handling, text processing, and working with external libraries.

For detailed information about licenses and legal disclaimers, please refer to the license.dat file included in this project.

## Version History

**Version 1.0 (Tuesday, 24-March-2026):** Initial release with basic PDF to audiobook conversion functionality.

## Final Notes

Thank you for using this PDF to Audiobook Converter. This project represents practical application of Python programming skills learned through structured education. Always use this tool responsibly and respect copyright laws and intellectual property rights.
