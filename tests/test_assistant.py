import unittest
from src.chatbot.assistant import HiringAssistant
from src.chatbot.utils import validate_email, validate_phone
from src.data.data_handler import DataHandler
import os

class TestHiringAssistant(unittest.TestCase):
    def setUp(self):
        self.assistant = HiringAssistant()
        self.test_data_path = "tests/test_data.json"
        self.data_handler = DataHandler(self.test_data_path)

    def tearDown(self):
        # Clean up test data file
        if os.path.exists(self.test_data_path):
            os.remove(self.test_data_path)

    def test_greeting(self):
        greeting = self.assistant.get_greeting()
        self.assertIsInstance(greeting, str)
        self.assertGreater(len(greeting), 0)

    def test_email_validation(self):
        self.assertTrue(validate_email("test@example.com"))
        self.assertFalse(validate_email("invalid-email"))
        self.assertFalse(validate_email("test@.com"))

    def test_phone_validation(self):
        self.assertTrue(validate_phone("1234567890"))
        self.assertTrue(validate_phone("+1234567890"))
        self.assertFalse(validate_phone("123"))
        self.assertFalse(validate_phone("abcdefghij"))

    def test_conversation_flow(self):
        # Test greeting to name step
        response = self.assistant.process_input("", "greeting")
        self.assertIn("name", response.lower())

        # Test name to email step
        response = self.assistant.process_input("John Doe", "name")
        self.assertIn("email", response.lower())

    def test_exit_handling(self):
        response = self.assistant.process_input("exit", "any_step")
        self.assertIn("thank you", response.lower())

    def test_data_handler(self):
        test_candidate = {
            "name": "John Doe",
            "email": "john@example.com",
            "phone": "1234567890"
        }
        
        # Test saving candidate
        self.assertTrue(self.data_handler.save_candidate_info(test_candidate))
        
        # Test retrieving candidate
        retrieved = self.data_handler.get_candidate_by_email("john@example.com")
        self.assertEqual(retrieved["name"], "John Doe")
        
        # Test getting all candidates
        all_candidates = self.data_handler.get_all_candidates()
        self.assertEqual(len(all_candidates), 1)

if __name__ == '__main__':
    unittest.main()