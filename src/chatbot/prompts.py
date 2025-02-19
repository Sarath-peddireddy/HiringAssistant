PROMPT_TEMPLATES = {
    "greeting": """
    Hello! I'm the TalentScout Hiring Assistant. I'll help gather some information about your background and assess your technical skills. 
    Let's get started! Could you please tell me your full name?
    """,
    
    "ask_name": "Could you please tell me your full name?",
    
    "ask_email": "Nice to meet you, {name}! Could you please provide your email address?",
    
    "ask_phone": "Great! Now, could you please share your phone number?",
    
    "ask_experience": "How many years of professional experience do you have in your field?",
    
    "ask_position": "What position(s) are you interested in applying for?",
    
    "ask_location": "What is your current location (city and country)?",
    
    "ask_tech_stack": """
    Please list your tech stack, including:
    - Programming languages
    - Frameworks
    - Databases
    - Tools
    
    For example: "Python, Django, PostgreSQL, Docker"
    """,
    
    "exit": """
    Thank you for your time! I've recorded your information and our recruitment team will review your profile.
    You can expect to hear back from us within 2-3 business days.
    Have a great day!
    """,
    
    "invalid_input": "I'm sorry, but that input doesn't seem to be valid. Could you please try again?"
}

TECHNICAL_QUESTION_PROMPT = """
Generate 3-5 technical questions for a candidate with the following tech stack:
{tech_stack}

The questions should:
1. Be relevant to the specified technologies
2. Range from basic to advanced concepts
3. Include both theoretical and practical aspects
""" 