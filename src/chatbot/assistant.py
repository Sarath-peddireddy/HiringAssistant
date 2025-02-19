from typing import Dict, Any
from .prompts import PROMPT_TEMPLATES
from .utils import validate_email, validate_phone
from openai import OpenAI
from src.config import load_config

class HiringAssistant:
    def __init__(self):
        config = load_config()
        self.client = OpenAI(api_key=config["OPENAI_API_KEY"])
        self.model = config["MODEL_NAME"]
        self.conversation_steps = [
            "greeting",
            "name",
            "email",
            "phone",
            "experience",
            "position",
            "location",
            "tech_stack",
            "technical_questions",
            "farewell"
        ]
        self.candidate_info = {}
    
    def get_greeting(self) -> str:
        return PROMPT_TEMPLATES["greeting"]
    
    def process_input(self, user_input: str, current_step: str) -> tuple[str, str]:
        # Check for conversation ending keywords
        if user_input.lower() in ["exit", "quit", "bye", "goodbye"]:
            return self._handle_exit(), "farewell"
        
        # Process input based on current conversation step
        if current_step == "greeting":
            return self._process_name_step(), "name"
            
        elif current_step == "name":
            self.candidate_info['name'] = user_input
            return self._process_email_step(user_input), "email"
            
        elif current_step == "email":
            if validate_email(user_input):
                self.candidate_info['email'] = user_input
                return self._process_phone_step(), "phone"
            return "Please provide a valid email address.", "email"
            
        elif current_step == "phone":
            if validate_phone(user_input):
                self.candidate_info['phone'] = user_input
                return self._process_experience_step(), "experience"
            return "Please provide a valid phone number.", "phone"
            
        elif current_step == "experience":
            self.candidate_info['experience'] = user_input
            return self._process_position_step(), "position"
            
        elif current_step == "position":
            self.candidate_info['position'] = user_input
            return self._process_location_step(), "location"
            
        elif current_step == "location":
            self.candidate_info['location'] = user_input
            return self._process_tech_stack_step(), "tech_stack"
            
        elif current_step == "tech_stack":
            self.candidate_info['tech_stack'] = user_input
            return self._process_technical_questions(user_input), "technical_questions"
            
        elif current_step == "technical_questions":
            return self._handle_exit(), "farewell"
        
        return "I'm sorry, I didn't understand that. Could you please try again?", current_step
    
    def _handle_exit(self) -> str:
        return PROMPT_TEMPLATES["exit"]
    
    def _process_name_step(self) -> str:
        return PROMPT_TEMPLATES["ask_name"]
    
    def _process_email_step(self, name: str) -> str:
        return PROMPT_TEMPLATES["ask_email"].format(name=name)
    
    def _process_phone_step(self) -> str:
        return PROMPT_TEMPLATES["ask_phone"]
    
    def _process_experience_step(self) -> str:
        return PROMPT_TEMPLATES["ask_experience"]
    
    def _process_position_step(self) -> str:
        return PROMPT_TEMPLATES["ask_position"]
    
    def _process_location_step(self) -> str:
        return PROMPT_TEMPLATES["ask_location"]
    
    def _process_tech_stack_step(self) -> str:
        return PROMPT_TEMPLATES["ask_tech_stack"]
    
    def _process_technical_questions(self, tech_stack: str) -> str:
        try:
            # Create a prompt for the LLM
            prompt = f"""Generate 3-5 technical interview questions for a candidate with the following tech stack: {tech_stack}

            Requirements for the questions:
            1. Questions should be specific to the mentioned technologies
            2. Include a mix of theoretical and practical questions
            3. Vary in difficulty (basic to advanced)
            4. Focus on real-world applications and problem-solving
            5. Cover both fundamental concepts and best practices

            Format the response as:
            1. [First Question]
            2. [Second Question]
            ...

            Make sure each question is relevant and would help assess the candidate's proficiency in the specified technologies."""

            # Get response from OpenAI
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": """You are a technical interviewer. 
                    Generate relevant and insightful technical questions based on the candidate's tech stack.
                    Focus on practical applications and real-world scenarios."""},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=500
            )

            # Extract the generated questions
            questions = response.choices[0].message.content.strip()

            # Format the final response
            final_response = f"""Based on your tech stack ({tech_stack}), here are some technical questions:

{questions}

Please provide detailed answers and feel free to include examples from your experience."""

            return final_response

        except Exception as e:
            # Fallback response in case of API errors
            fallback_questions = f"""I apologize, but I'm having trouble generating specific questions. 
            Here are some general questions about your tech stack ({tech_stack}):

1. Could you explain your experience with these technologies and how you've used them in real projects?
2. What are some challenging problems you've solved using these technologies?
3. How do you stay updated with the latest developments in these technologies?
4. Can you describe a project where you had to integrate multiple technologies from your stack?

Please provide detailed answers and include specific examples from your experience."""
            
            print(f"Error generating questions: {str(e)}")
            return fallback_questions 