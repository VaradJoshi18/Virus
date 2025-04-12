# 💣 Virus

**Virus** is a Python script designed to repeatedly open command prompt windows and create directories with unique names. This example demonstrates how to execute system commands and manipulate the file system programmatically. **Use responsibly and only within controlled, legal environments.**

---

## Table of Contents

- [Features](#features-)
- [Requirements](#requirements-)
- [Installation](#installation-)
- [Usage](#usage-)
- [How It Works](#how-it-works-)
- [Disclaimer & Legal Notice](#disclaimer-%EF%B8%8F)


---

## Features ✨

- **Automated CMD Launch:**  
  Repeatedly opens the command prompt using the system's command line.
  
- **Random Directory Creation:**  
  Creates uniquely named folders using random hexadecimal values.
  
- **Looping Behavior:**  
  Continuously performs actions in an infinite loop.

---

## Requirements 🛠

- **Python 3.x:**  
  Make sure you have Python 3 installed on your system.

- **Operating System:**  
  Designed to work on Windows systems due to the use of `cmd` commands and `os.system("start cmd")`.

---

## Installation 💾

1. **Clone or Download the Repository:**

   ```bash
   git clone https://github.com/yourusername/virus.git
   cd virus
   ```

2. **Set Up a Virtual Environment (Optional but Recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows, use `venv\Scripts\activate`
   ```

3. **No External Dependencies:**  
   This project only uses Python standard libraries, so no additional installations are necessary.

---

## Usage 🚀

1. **Run the Script:**

   Open your terminal or command prompt, navigate to the project directory, and run:

   ```bash
   python virus.py
   ```

2. **Observe the Behavior:**

   - The script will continuously launch new command prompt windows.
   - It will also create directories with randomly generated names (e.g., `VVV_ab3f2c1d`).

3. **Stop the Process:**

   Since the script runs in an infinite loop, you may need to manually terminate the process (using `Ctrl+C` in the terminal or ending the process in Task Manager).

---

## How It Works 🔍

- **Command Execution:**  
  The `os.system("start cmd")` command is used to spawn new command prompt windows.
  
- **Random Folder Creation:**  
  Each folder is created using a unique name generated with `os.urandom(4).hex()`, prefixed by `VVV_`.

- **Infinite Loop:**  
  The `while True:` loop ensures that these actions are repeated continuously until the program is manually stopped.

---

## Disclaimer ⚠️

> **Warning:**  
> **This script is for educational purposes only!**  
> The **Virus** project is intended to demonstrate how system commands and file operations can be executed using Python. **Unauthorized or malicious use of this code is illegal and unethical.**  
> Use it only in controlled, isolated environments (e.g., virtual machines or test labs) where you have permission to do so.  
> The author is not responsible for any harm or damage caused by misuse of this code.

---

💡 **Important:**  
Always exercise ethical behavior and remain within legal boundaries when testing or deploying any code. Use your skills wisely and responsibly!

---
