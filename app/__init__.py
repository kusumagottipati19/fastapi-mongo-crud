from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

# Adjusted utility function to provide a default instead of raising an error if env variable is missing
def get_env_variable(key, default=""):
    # Load the value from environment; if not found, return default
    value = os.getenv(key)
    if value is None:
        # Instead of raising an error, return the default value
        return default
    return value

# Example usage for MongoDB URI
MONGO_URI = get_env_variable('MONGO_URI')

