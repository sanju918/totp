# TOTP Generator (Secure One-Time Passwords)

## Description 
Generate time-based one-time passwords (TOTP) for secure two-factor authentication, similar to Google Authenticator. This Python script provides a convenient way to add an extra layer of security to your accounts.

## Installation

### Prerequisites
- **Python 3** (Download from [official Python download page](https://www.python.org/downloads/))
- **pip** (Python package manager)

### Steps:

1. **Install Python**: If you don't have Python installed, download and install it from the official website.

2. **Install Dependencies**: Open a terminal or command prompt and navigate to the directory containing the `requirements.txt` file. Then, run the following command to install the required libraries:

    ```bash
    pip install -r requirements.txt
    ```

3. **Environment Variables**:
   - Create a `.env` File: Create a file named `.env` in the root directory of your project. This file will store your secret key securely.
   - Add Secrets: Inside the `.env` file, add your secret key as a key-value pair.
     
     ```plaintext
     # Example (replace with your actual secret key)
     SECRET_KEY=your_secret_key_here
     ```

4. **Run the Script**: Open a terminal or command prompt and navigate to the directory containing the `source/main.py` script. Then, run the following command to execute the script:

    ```bash
    python3 path/to/source/main.py
    ```

## Usage

### Using TOTP with Your Account:
1. Open your account security settings.
2. Look for the option to add a two-factor authentication method (e.g., 2FA, TOTP).
3. Choose the option to use a time-based one-time password app.
4. Scan the QR code provided by your account (if available) or enter the secret key you retrieved from the `.env` file.
5. Use the generated TOTP code from this script when prompted during login.

## Contributors
Sanjay Kumar Patel (cenzer2@gmail.com)

## Additional Enhancements

### Screenshots/GIFs
TBD

### Contributing Guidelines
TBD

### License
Open Source - MIT License.
