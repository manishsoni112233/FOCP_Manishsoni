import random
import json
import time
from datetime import datetime
from pathlib import Path

class Chatbot:
    def __init__(self, config_file="chat_config.json"):
        self.config = self.load_config(config_file)
        self.agent_name = self.get_agent_name()
        self.user_name = None

    def load_config(self, file):
        config_path = Path(file)
        if not config_path.exists():
            raise FileNotFoundError(f"Configuration file '{file}' not found.")
        with config_path.open("r") as f:
            return json.load(f)

    def log_interaction(self, user_input, bot_response):
        log_path = Path("chat_log.txt")
        with log_path.open("a") as log_file:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_file.write(f"[{now}] User: {user_input}\n")
            log_file.write(f"[{now}] Bot: {bot_response}\n")

    def get_agent_name(self):
        agent_names = self.config.get("agent_names", ["Alex", "Sam", "Taylor", "Jordan", "Morgan"])
        return random.choice(agent_names)

    def generate_response(self, user_input):
        keywords = self.config.get("keywords", {})
        random_responses = self.config.get("random_responses", [
            "I'm not sure I understand that. Could you clarify?",
            "Interesting question! Let me check.",
            "Hmm, that's beyond my expertise.",
            "I'm here to help, but could you provide more details?",
            "That’s a great question! Let me find out.",
            "I'm not sure about that, but I recommend checking the official website.",
            "Could you explain that a bit more?",
            "I don't have that information right now, but I'll make a note of it!"
        ])
        
        response = None
        for keyword, replies in keywords.items():
            if keyword in user_input:
                response = random.choice(replies)
                break
        if not response:
            response = random.choice(random_responses)
        return response

    def stream_response(self, response):
        words = response.split()
        for word in words:
            print(word, end=' ', flush=True)
            time.sleep(0.1)  # Adjust the delay as needed
        print()  # Print a newline at the end

    def suggest_questions(self, user_input):
        # Suggest questions based on the context of user input
        suggested_questions = []
        if "library" in user_input:
            suggested_questions = [
                "Would you like to know about the library's resources?",
                "Do you need information on how to reserve a study room?",
                "Are you interested in the library's digital resources?"
            ]
        elif "courses" in user_input:
            suggested_questions = [
                "Would you like to know more about the courses we offer?",
                "Are you interested in knowing the prerequisites for a course?",
                "Do you need information about the course registration process?"
            ]
        elif "scholarships" in user_input:
            suggested_questions = [
                "Would you like to know the eligibility criteria for scholarships?",
                "Are you interested in the application process for scholarships?",
                "Do you need information on the types of scholarships available?"
            ]
        else:
            suggested_questions = [
                "Would you like to know about our scholarship programs?",
                "Do you need information about the campus library hours?",
                "Are you interested in learning more about our sports facilities?",
                "Would you like to know about the upcoming campus events?",
                "Do you need help with information about student parking?"
            ]
        
        print("\nHere are some questions you might find useful:")
        for question in suggested_questions:
            print(f"- {question}")

    def handle_command(self, user_input):
        # Remove or reduce the probability of random disconnection
        if user_input in ["bye", "quit", "exit"]:
            farewell_message = f"Goodbye, {self.user_name}! Have a great day!"
            self.stream_response(farewell_message)
            self.log_interaction(user_input, farewell_message)
            return False

        # Reconnection logic
        if user_input.lower() in ["reconnect", "connect"]:
            reconnection_message = "Reconnected successfully. How can I assist you further?"
            self.stream_response(reconnection_message)
            self.log_interaction(user_input, reconnection_message)
            return True

        response = self.generate_response(user_input)
        response = response.replace("{user}", self.user_name)
        self.stream_response(response)
        self.log_interaction(user_input, response)
        self.suggest_questions(user_input)  # Suggest questions based on user input
        return True

    def run(self):
        print("Welcome to the University of ledds becket chatbot!")
        self.user_name = input("What's your name? ").strip()
        print(f"Hi {self.user_name}! I'm {self.agent_name}, your virtual assistant.")

        while True:
            user_input = input("You: ").strip().lower()
            if not self.handle_command(user_input):
                break

if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.run()