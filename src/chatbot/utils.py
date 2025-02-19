import re

def validate_email(email: str) -> bool:
    """Validate email format."""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

def validate_phone(phone: str) -> bool:
    """Validate phone number format."""
    pattern = r'^\+?1?\d{9,15}$'
    return bool(re.match(pattern, phone))

def sanitize_input(user_input: str) -> str:
    """Sanitize user input to prevent injection attacks."""
    # Remove any potentially harmful characters
    return re.sub(r'[<>{}]', '', user_input)