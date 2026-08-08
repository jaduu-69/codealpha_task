"""
CodeAlpha - Task 3: Task Automation
A script that automates simple actions:
  1. Organize files by moving all image files (.jpg, .jpeg, .png) into an
     "Images" folder.
  2. Extract all email addresses found in a text file.

Author: <your name here>
"""

import os
import re
import shutil


# ---------------------------------------------------------------------------
# Automation 1: Organize image files into a folder
# ---------------------------------------------------------------------------
IMAGE_EXTENSIONS = (".jpg", ".jpeg", ".png", ".gif", ".bmp")


def organize_images(source_folder, destination_folder="Images"):
    """Move all image files from source_folder into destination_folder."""
    if not os.path.isdir(source_folder):
        print(f"Error: '{source_folder}' is not a valid folder.")
        return

    dest_path = os.path.join(source_folder, destination_folder)
    os.makedirs(dest_path, exist_ok=True)

    moved_count = 0
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        # Skip directories and the destination folder itself
        if os.path.isdir(file_path):
            continue

        if filename.lower().endswith(IMAGE_EXTENSIONS):
            shutil.move(file_path, os.path.join(dest_path, filename))
            print(f"Moved: {filename} -> {destination_folder}/")
            moved_count += 1

    print(f"\nDone! Moved {moved_count} image file(s) into '{dest_path}'.")


# ---------------------------------------------------------------------------
# Automation 2: Extract email addresses from a text file
# ---------------------------------------------------------------------------
EMAIL_PATTERN = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")


def extract_emails_from_file(input_file, output_file="extracted_emails.txt"):
    """Read a text file, find all emails, and save the unique ones."""
    if not os.path.isfile(input_file):
        print(f"Error: '{input_file}' does not exist.")
        return

    with open(input_file, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    emails_found = sorted(set(EMAIL_PATTERN.findall(content)))

    if not emails_found:
        print("No email addresses found.")
        return

    with open(output_file, "w") as f:
        for email in emails_found:
            f.write(email + "\n")

    print(f"Found {len(emails_found)} unique email(s):")
    for email in emails_found:
        print(f"  - {email}")
    print(f"\nSaved to '{output_file}'.")


# ---------------------------------------------------------------------------
# Simple menu to run either automation
# ---------------------------------------------------------------------------
def main():
    print("=" * 50)
    print("TASK AUTOMATION SCRIPT")
    print("=" * 50)
    print("1. Organize image files into an 'Images' folder")
    print("2. Extract email addresses from a text file")
    print("0. Exit")

    choice = input("\nChoose an option (0/1/2): ").strip()

    if choice == "1":
        folder = input("Enter the folder path to organize: ").strip()
        organize_images(folder)
    elif choice == "2":
        file_path = input("Enter the path of the text file: ").strip()
        extract_emails_from_file(file_path)
    elif choice == "0":
        print("Goodbye!")
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
