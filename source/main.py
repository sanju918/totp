import hmac
import time
import base64
import logging
from dotenv import dotenv_values, find_dotenv


def setup_logging():
    """Set up logging configuration."""
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("app.log"),
            logging.StreamHandler()
        ]
    )


def totp(key: bytes) -> str:
    """
    Calculate TOTP using the provided key.

    Args:
        key (bytes): The shared secret key in bytes.

    Returns:
        str: The generated TOTP code as a 6-digit string.
    """
    now = int(time.time() // 30)
    msg = now.to_bytes(8, "big")
    digest = hmac.new(key, msg, "sha1").digest()
    offset = digest[19] & 0xF
    code = digest[offset: offset + 4]
    code = int.from_bytes(code, "big") & 0x7FFFFFFF
    code = code % 1000000
    return "{:06d}".format(code)


def load_env_file(file_path: str) -> dict:
    """
    Load the environment variables from a .env file.

    Args:
        file_path (str): The path to the .env file.

    Returns:
        dict: A dictionary containing the environment variables.
    """
    try:
        envs = dotenv_values(file_path)
        if not envs:
            raise ValueError("The .env file is empty or not found.")
        logging.info("Successfully loaded environment variables.")
        return envs
    except Exception as e:
        logging.error(f"Failed to load .env file: {e}")
        raise


if __name__ == "__main__":
    setup_logging()

    # Load environment variables
    env_path = find_dotenv()
    try:
        envs = load_env_file(env_path)
    except Exception as e:
        logging.critical(f"Exiting program due to failure in loading .env file: {e}")
        exit(1)

    # Print all environment keys as apps
    print("Your Apps:")
    keys = list(envs.keys())
    for i, key in enumerate(keys, start=1):
        print(f"{i}. {key}")

    # Let the user select an app by entering the serial number
    try:
        selection = int(input("\nEnter the serial number of the app: ")) - 1
        if 0 <= selection < len(keys):
            selected_key = keys[selection]
            key_value = envs[selected_key]
            try:
                key_bytes = base64.b32decode(key_value)
                totp_ = totp(key_bytes)
                print(f"TOTP for {selected_key}: {totp_}")
                logging.info(f"Successfully generated TOTP for {selected_key}.")
            except base64.binascii.Error as e:
                logging.error(f"Decoding error for key {selected_key}: {e}")
                print("Error: The key is not a valid base32 encoded string.")
        else:
            logging.warning("User made an invalid selection.")
            print("Invalid selection. Please enter a number from the list.")
    except ValueError:
        logging.warning("User input was not a valid number.")
        print("Invalid input. Please enter a number.")