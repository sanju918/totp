import logging
import pyotp

from colorama import init, Fore, Style
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
    init(autoreset=True)  # Initialize colorama for automatic reset of styles
    setup_logging()

    # Load environment variables
    env_path = find_dotenv()
    try:
        envs = load_env_file(env_path)
    except Exception as e:
        logging.critical(f"Exiting program due to failure in loading .env file: {e}")
        exit(1)

    # Print all environment keys as apps
    print(Fore.CYAN + "Your Apps:")
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
                # Using pyotp to generate the TOTP code
                totp = pyotp.TOTP(key_value)
                otp = totp.now()
                print("\n" + Fore.GREEN + Style.BRIGHT + f"TOTP for {selected_key}:",
                      Fore.YELLOW + Style.BRIGHT + f"{otp}\n")
                logging.info(f"Successfully generated TOTP for {selected_key}.")
            except Exception as e:
                logging.error(f"Error generating TOTP for key {selected_key}: {e}")
                print(Fore.RED + "Error: Unable to generate TOTP for the selected key.")
        else:
            logging.warning("User made an invalid selection.")
            print(Fore.RED + "Invalid selection. Please enter a number from the list.")
    except ValueError:
        logging.warning("User input was not a valid number.")
        print(Fore.RED + "Invalid input. Please enter a number.")
