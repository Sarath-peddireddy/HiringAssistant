import json
from typing import Dict, List
from datetime import datetime
import os

class DataHandler:
    def __init__(self, storage_path: str = "data/candidates.json"):
        self.storage_path = storage_path
        self._ensure_storage_exists()

    def _ensure_storage_exists(self):
        """Create storage directory and file if they don't exist."""
        os.makedirs(os.path.dirname(self.storage_path), exist_ok=True)
        if not os.path.exists(self.storage_path):
            with open(self.storage_path, 'w') as f:
                json.dump([], f)

    def save_candidate_info(self, candidate_info: Dict) -> bool:
        """Save candidate information to storage."""
        try:
            candidate_info['timestamp'] = datetime.now().isoformat()
            
            # Read existing data
            with open(self.storage_path, 'r') as f:
                candidates = json.load(f)
            
            # Add new candidate
            candidates.append(candidate_info)
            
            # Write back to file
            with open(self.storage_path, 'w') as f:
                json.dump(candidates, f, indent=2)
            
            return True
        except Exception as e:
            print(f"Error saving candidate info: {str(e)}")
            return False

    def get_candidate_by_email(self, email: str) -> Dict:
        """Retrieve candidate information by email."""
        try:
            with open(self.storage_path, 'r') as f:
                candidates = json.load(f)
            
            for candidate in candidates:
                if candidate.get('email') == email:
                    return candidate
            return {}
        except Exception as e:
            print(f"Error retrieving candidate info: {str(e)}")
            return {}

    def get_all_candidates(self) -> List[Dict]:
        """Retrieve all candidates."""
        try:
            with open(self.storage_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error retrieving candidates: {str(e)}")
            return []