from decouple import config
import os

def load_config():
    """Load configuration from environment variables."""
    try:
        return {
            "OPENAI_API_KEY": config("OPENAI_API_KEY"),
            "MODEL_NAME": config("MODEL_NAME", default="gpt-4"),
            "MAX_TOKENS": config("MAX_TOKENS", default=500, cast=int),
            "TEMPERATURE": config("TEMPERATURE", default=0.7, cast=float),
        }
    except UnicodeDecodeError:
        # Fallback to environment variables if .env file has encoding issues
        return {
            "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY"),
            "MODEL_NAME": os.getenv("MODEL_NAME", "gpt-4"),
            "MAX_TOKENS": int(os.getenv("MAX_TOKENS", "500")),
            "TEMPERATURE": float(os.getenv("TEMPERATURE", "0.7")),
        }