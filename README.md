# Email Sending Script

This repository contains a Python script that sends emails at scheduled times. The main functionalities include sending a daily to-do list along with a Bible verse, and a reminder to update the to-do list.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
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

## Automation.
So as to automate this scripts and get them running at specified times, you need to schedule a cron job for Linux/Unix machines or Task Scheduler for Windows machines.

1 **Linux/Unix Machines**

For Linux/Unix machines, we will use ```cron``` to schedule cron jobs to run our scripts at specified times.

a. Install ```cron```.
To install cron on your Linux machine, navigate to the command line and run:

```bash

sudo apt update && sudo apt install cron

```
b. Launch the crontab.
To launch the crontab, run:
```bash

crontab -e

```

c. Scheduling the cronjob.
For this cronjob, I scheduled the script to be run at 7:30AM everyday for script.py and 10:30PM everday for reminder.py. Add the following lines of code into your crontab:
```bash
# Basic Syntax
# minute hour dom month weekday command
#   *     *    *   *      *     echo 'hello world' >> hello.txt

30 7 * * * /usr/bin/python3 /mnt/c/Users/LENOVO/mymachine/mydocs/script.py
30 22 * * * /usr/bin/python3 /mnt/c/Users/LENOVO/mymachine/mydocs/reminder.py

```

d. Start the cron service.
To start the cron service and check its status, run:
```bash

sudo service cron start
sudo service cron status

```
2. **Windows Machines**
To schedule this job on your Windows machine, run ```Win + R``` and search for the Task Scheduler.

## Note
Make sure to enable "Less secure app access" in your Google account settings to allow the script to send emails. Alternatively, consider using an App Password if you have 2-Step Verification enabled.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
