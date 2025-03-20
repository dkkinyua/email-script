# Email Sending Script

This repository contains a Python script that sends emails at scheduled times. The main functionalities include sending a daily to-do list along with a Bible verse, and a reminder to update the to-do list.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Automation](#automation)
- [File Descriptions](#file-descriptions)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/dkkinyua/email-script.git
   cd email-script
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```bash
   pip install python-dotenv requests
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root directory of the project and add the following lines:
   ```plaintext
   GMAIL_USERNAME=your_email@gmail.com
   GMAIL_PWD=your_password
   EMAIL_SENDER=your_email@gmail.com
   EMAIL_RECEIVER=receiver_email@gmail.com
   ```

## Usage

- **To send the daily to-do list and Bible verse:**
  Run the `script.py` file. This will fetch the to-do list from `todo.json` and a Bible verse from an API, then send them via email.
```bash

python script.py

```

- **To send a reminder to update the to-do list:**
  Run the `reminder.py` file. This will send a reminder email at 10:30 PM.
```bash

python reminder.py

```

- **To test the connection to the Gmail SMTP server:**
  Run the `test.py` file. This will check if the credentials are correct and if the connection can be established.
```bash

python test.py

```

## File Descriptions

- **`script.py`**: 
  This script sends an email containing the daily to-do list and a Bible verse. It fetches the Bible verse from an external API and reads the to-do list from a JSON file named `todo.json`. The email is sent in HTML format for better presentation.

- **`reminder.py`**: 
  This script sends a reminder email at 10:30 PM, prompting the user to update their to-do list. The email includes a friendly message and is sent to the specified receiver.

- **`test.py`**: 
  This script tests the connection to the Gmail SMTP server using the provided credentials. It verifies if the login is successful and handles authentication errors.

## Automation

To automate the execution of these scripts and have them run at specified times, you can use the Task Scheduler in Windows. Here's how to set it up:

### Scheduling Tasks in Windows using Task Scheduler

1. **Open Task Scheduler:**
   - Press `Win + R` to open the Run dialog.
   - Type `taskschd.msc` and press Enter. This will open the Task Scheduler.

2. **Create a New Task:**
   - In the Task Scheduler, click on "Create Basic Task" in the right-hand Actions pane.
   - Give your task a name (e.g., "Send Daily To-Do List") and a description, then click "Next."

3. **Set the Trigger:**
   - Choose how often you want the task to run (Daily, Weekly, etc.) and click "Next."
   - Set the start date and time (e.g., 7:30 AM for the daily to-do list) and click "Next."

4. **Action to Perform:**
   - Select "Start a program" and click "Next."
   - In the "Program/script" field, enter the path to your Python executable (e.g., `C:\Path\To\Python\python.exe`).
   - In the "Add arguments (optional)" field, enter the path to your script (e.g., `C:\Path\To\Your\Script\script.py`).
   - Click "Next."

5. **Finish:**
   - Review your settings and click "Finish" to create the task.

6. **Repeat for Other Scripts:**
   - Repeat the above steps to create another task for the reminder script, setting it to run at 10:30 PM.

### Note
Make sure to enable "Less secure app access" in your Google account settings to allow the script to send emails. Alternatively, consider using an App Password if you have 2-Step Verification enabled.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
