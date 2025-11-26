# 💀 File Roulette: The Anti-Termination Experiment

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6.svg)
![Risk](https://img.shields.io/badge/Risk-High-red.svg)

> **⚠️ CRITICAL DISCLAIMER**
>
> This software is a **Proof of Concept (PoC)** designed to demonstrate **Anti-Termination** and **Dead Man's Switch** techniques using the Windows API and Process Spawning.
>
> **RUN AT YOUR OWN RISK.** This program **permanently deletes files**.
> By running this software, you acknowledge that the developer is not responsible for any data loss, damages, or frustration caused.
> *It is highly recommended to run this inside a Virtual Machine (VM).*

---

## 📖 Overview

**File Roulette** is a terminal-based gambling game with a twist: **The currency is your files.**
You gamble with virtual money, but if you lose—or worse, if you try to cheat—the files get deleted.
For every money you have left in the end , you will lose 1 file from your desktop

### The "Trap"
The core feature of this project is its **Anti-Evasion System**.
The program is designed to detect *any* attempt to forcibly close it.
* **Clicking 'X'?** -> Immediate deletion.
* **Ctrl+C?** -> Immediate deletion.
* **Task Manager (End Task)?** -> Immediate deletion via a Watchdog process.

The only way to save your files is to play the game and exit gracefully via the menu.

<img width="1085" height="358" alt="image" src="https://github.com/user-attachments/assets/c9bbcb68-b48b-4e8a-be59-ca26d7b1bb54" />


---

## ⚙️ Technical Architecture

This project demonstrates advanced OS-level interaction and process management techniques:

### 1. 🐕 The Watchdog Process (Self-Spawning)
Upon execution, the main program uses `subprocess.Popen` to spawn a **hidden clone of itself** with a special flag (`--watchdog`).
* **Main Process:** Handles the Game UI and logic.
* **Watchdog Process:** Runs invisibly in the background, monitoring the Main Process PID.
* **Mechanism:** If the Main Process dies *without* creating a cryptographic "Safe Exit" lock file, the Watchdog assumes a forced termination and triggers the `panic_delete()` function.

---

## 🎮 How to Play

1.  **Launch:** Run the executable. A CMD window opens with a red theme.
2.  **Gamble:** You start with **$20**.
    * **Goal:** Reach **$0** (Yes, you want to lose money to "pay off" the debt).
    * **Exit:** Type `exit` at any time to quit.
3.  **Consequences:**
    * If you exit with money remaining (e.g., $15), **15 files** will be deleted.
    * If you reach $0, **0 files** are deleted.
    * **IF YOU CLOSE THE WINDOW:** **ALL** files are deleted immediately.

---

## 🚀 Installation & Build

### Prerequisites
* Python 3.x
* Windows OS (Required for `ctypes` hooks)
* `psutil` library (For process monitoring)

```bash
pip install psutil pyinstaller
