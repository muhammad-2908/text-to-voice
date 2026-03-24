"""
PDF to Audiobook Converter
===========================

Project: PDF to Audiobook Converter
Author: Muhammad Usman
Last Updated: Tuesday, 24-March-2026
Course: 100 Days of Code - The Complete Python Pro Bootcamp
Instructor: Angela Yu
Course URL: https://www.udemy.com/course/100-days-of-code/learn/practice/1251140#overview

DISCLAIMER:
This software is provided "as is" without warranty of any kind.
The author is not responsible for any misuse of this software.
Users are responsible for ensuring they have legal rights to convert
and use any PDF files processed by this application.
Please respect copyright laws and only use this tool for PDFs you own
or have permission to convert.

LEGAL IMPLICATIONS:
- Only convert PDFs that you own or have permission to use
- Do not distribute converted audiobooks of copyrighted material
- This tool is for personal use only
- Respect intellectual property rights and copyright laws
"""

# Import the necessary libraries for our application
# pypdf is used to read and extract text from PDF files
# pyttsx3 is used to convert text to speech (works offline)
# os helps us work with file paths and the operating system
import pypdf
import pyttsx3
import os
import sys


def extract_text_from_pdf(pdf_file_path):
    """
    This function opens a PDF file and extracts all the text from it.

    How it works:
    1. Opens the PDF file
    2. Goes through each page one by one
    3. Extracts the text from each page
    4. Combines all the text together

    Parameters:
    pdf_file_path: The location of the PDF file on your computer

    Returns:
    A single string containing all the text from the PDF
    """

    # Initialize an empty string to store all the text we find
    full_text = ""

    try:
        # Open the PDF file in read binary mode
        # Binary mode is needed because PDFs are not simple text files
        with open(pdf_file_path, 'rb') as pdf_file:

            # Create a PDF reader object that can understand the PDF format
            pdf_reader = pypdf.PdfReader(pdf_file)

            # Get the total number of pages in the PDF
            total_pages = len(pdf_reader.pages)

            # Print a message to let the user know we are processing the file
            print(f"Found {total_pages} pages in the PDF file.")
            print("Extracting text from PDF...")

            # Loop through each page in the PDF
            for page_number in range(total_pages):

                # Get the current page
                page = pdf_reader.pages[page_number]

                # Extract the text from this page
                page_text = page.extract_text()

                # Add the text from this page to our full text collection
                full_text += page_text

                # Show progress to the user
                print(f"Processed page {page_number + 1} of {total_pages}")

            print("Text extraction complete!")

    except FileNotFoundError:
        # This error happens if the PDF file does not exist at the given location
        print(f"Error: Could not find the file at {pdf_file_path}")
        print("Please check the file path and try again.")
        sys.exit(1)

    except Exception as error:
        # This catches any other errors that might occur
        print(f"An error occurred while reading the PDF: {error}")
        sys.exit(1)

    # Return all the text we extracted from the PDF
    return full_text


def convert_text_to_speech(text, output_file_name="audiobook.mp3"):
    """
    This function converts text into speech and saves it as an audio file.

    How it works:
    1. Creates a text-to-speech engine
    2. Configures the voice settings (speed, volume, voice type)
    3. Converts the text to speech
    4. Saves the audio to a file

    Parameters:
    text: The text to convert to speech
    output_file_name: The name of the audio file to create (default is audiobook.mp3)
    """

    try:
        # Initialize the text-to-speech engine
        # This engine works offline and does not require an internet connection
        engine = pyttsx3.init()

        # Get the list of available voices on the system
        voices = engine.getProperty('voices')

        # Set the voice (0 is usually male, 1 is usually female)
        # You can change this number to try different voices
        engine.setProperty('voice', voices[0].id)

        # Set the speaking rate (speed of speech)
        # Default is 200 words per minute, we use 150 for clearer speech
        engine.setProperty('rate', 150)

        # Set the volume (0.0 to 1.0, where 1.0 is maximum)
        engine.setProperty('volume', 1.0)

        print(f"Converting text to speech...")
        print(f"This may take a while depending on the length of the text.")

        # Save the speech to a file
        engine.save_to_file(text, output_file_name)

        # Process the speech conversion
        # This actually performs the conversion and saves the file
        engine.runAndWait()

        print(f"Success! Audiobook saved as: {output_file_name}")

    except Exception as error:
        # This catches any errors that occur during speech conversion
        print(f"An error occurred during text-to-speech conversion: {error}")
        sys.exit(1)


def main():
    """
    This is the main function that runs when the program starts.

    How it works:
    1. Welcomes the user
    2. Asks for the PDF file location
    3. Asks for the output audio file name
    4. Extracts text from the PDF
    5. Converts the text to speech
    6. Saves the audiobook
    """

    # Print a welcome message
    print("=" * 60)
    print("PDF to Audiobook Converter")
    print("=" * 60)
    print("Author: Muhammad Usman")
    print("Course Credit: Angela Yu - 100 Days of Code")
    print("=" * 60)
    print()

    # Ask the user for the PDF file path
    # The user needs to provide the full path to their PDF file
    pdf_path = input("Enter the path to your PDF file: ").strip()

    # Remove quotes if the user copied the path with quotes
    pdf_path = pdf_path.strip('"').strip("'")

    # Check if the file exists before proceeding
    if not os.path.exists(pdf_path):
        print(f"Error: The file '{pdf_path}' does not exist.")
        print("Please check the path and try again.")
        sys.exit(1)

    # Check if the file is actually a PDF
    if not pdf_path.lower().endswith('.pdf'):
        print("Warning: The file does not have a .pdf extension.")
        print("This might not be a PDF file.")
        proceed = input("Do you want to continue anyway? (yes/no): ").strip().lower()
        if proceed not in ['yes', 'y']:
            print("Operation cancelled.")
            sys.exit(0)

    # Ask the user for the output file name
    print()
    output_name = input("Enter the output audio file name (press Enter for default 'audiobook.mp3'): ").strip()

    # If the user did not provide a name, use the default
    if not output_name:
        output_name = "audiobook.mp3"

    # Make sure the output file has an audio extension
    if not (output_name.endswith('.mp3') or output_name.endswith('.wav')):
        output_name += '.mp3'

    print()
    print("Starting conversion process...")
    print()

    # Step 1: Extract text from the PDF file
    extracted_text = extract_text_from_pdf(pdf_path)

    # Check if we actually got any text from the PDF
    if not extracted_text or len(extracted_text.strip()) == 0:
        print("Warning: No text was extracted from the PDF.")
        print("The PDF might be image-based or encrypted.")
        print("This tool only works with text-based PDFs.")
        sys.exit(1)

    # Show a preview of the extracted text
    print()
    print("Text Preview (first 200 characters):")
    print("-" * 60)
    print(extracted_text[:200])
    print("-" * 60)
    print()

    # Ask for confirmation before converting
    confirm = input("Do you want to proceed with audio conversion? (yes/no): ").strip().lower()
    if confirm not in ['yes', 'y']:
        print("Conversion cancelled.")
        sys.exit(0)

    print()

    # Step 2: Convert the extracted text to speech
    convert_text_to_speech(extracted_text, output_name)

    # Print success message with file location
    print()
    print("=" * 60)
    print("Conversion Complete!")
    print(f"Your audiobook is ready: {os.path.abspath(output_name)}")
    print("=" * 60)


# This is the entry point of the program
# When the script is run directly, this code executes
if __name__ == "__main__":
    main()
