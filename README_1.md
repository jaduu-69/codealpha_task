# CodeAlpha - Task Automation

A Python script that automates two simple everyday tasks:

1. **Organize Images** – Scans a folder and moves all image files
   (`.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`) into a subfolder called `Images`.
2. **Extract Emails** – Scans a text file and extracts all unique email
   addresses into a new file called `extracted_emails.txt`.

## How to Run
```bash
python task_automation.py
```

You'll see a menu:
```
1. Organize image files into an 'Images' folder
2. Extract email addresses from a text file
0. Exit
```

## Example: Organizing Images
```
Enter the folder path to organize: C:/Users/you/Downloads
Moved: photo1.jpg -> Images/
Moved: screenshot.png -> Images/
Done! Moved 2 image file(s) into 'C:/Users/you/Downloads/Images'.
```

## Example: Extracting Emails
```
Enter the path of the text file: contacts.txt
Found 2 unique email(s):
  - jane.doe@example.com
  - john@company.org
Saved to 'extracted_emails.txt'.
```

## Author
Internship Project - CodeAlpha
