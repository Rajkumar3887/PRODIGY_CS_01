

# 🔐 PRODIGY\_CS\_01 — Caesar Security Tool (Simplified Version)

**Author:** Raj Kumar  
**Internship:** Prodigy InfoTech — Cyber Security Track  
**Task:** 01 — Caesar Cipher

## 📌 Project Overview

This project implements a simplified Caesar Cipher tool designed for cybersecurity learning under the **Prodigy InfoTech Internship (Cyber Security Track)**.

The goal is to understand:

  * How classical substitution ciphers work.
  * How encryption can be easily broken.
  * Why strong cryptography is needed today.

This version includes only the essential components:

  * ✔ Encrypt
  * ✔ Decrypt
  * ✔ Brute-force
  * ✔ Exit


## 🚀 Features

  * **Encrypt text** with a Caesar shift.
  * **Decrypt text** using the same shift.
  * **Brute-force attack** (automatically checks all 25 possible shifts).
  * **Lightweight, interactive CLI.**
  * **No external dependencies.**

## 📁 Repository Structure

```text
PRODIGY_CS_01/
│── caesar_cipher.py   # Main CLI tool
│── README.md          # Documentation
```

## 🛠 Requirements

  * **Python 3.8+**
  * No external packages required.

## 📦 Installation & Running

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/rajkumar3887/PRODIGY_CS_01.git
    ```

2.  **Navigate into the folder:**

    ```bash
    cd PRODIGY_CS_01
    ```

3.  **Run the script:**

    ```bash
    python caesar_cipher.py
    ```

## 🎮 How to Use

When you run the script, the following menu appears:

```text
1) Encrypt text
2) Decrypt text
3) Brute-force ciphertext (show all 25 shifts)
4) Exit
```

### 🔹 Example: Encrypt

> **Enter message:** hello
> **Shift:** 3
> **Output:** khoor

### 🔹 Example: Brute-force

If you have a ciphertext `khoor` but don't know the shift:

> Shift 03: hello    \<-- Correct plaintext
> Shift 04: gdkkn
> Shift 05: fcjjm
> ...

## 📚 Learning Outcome

By completing this project, you learn:

  * How classical ciphers work.
  * Why the Caesar Cipher is insecure.
  * How attackers use brute-force to reveal plaintext.
  * Foundation concepts in cybersecurity and cryptography.

## 🏅 Credits

Created by **Raj Kumar** For **Prodigy InfoTech Cyber Security Internship**

## ⭐ Support

If you like this project, please star ⭐ the repository on GitHub\!
