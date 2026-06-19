import json
import random
import re
from collections import Counter
from pathlib import Path


class CustomerServiceBot:
    """Simple NLP chatbot using token matching and cosine similarity."""

    def __init__(self, intents_path=None):
        base_dir = Path(__file__).resolve().parent
        self.intents_path = Path(intents_path) if intents_path else base_dir / "data" / "intents.json"
        self.intents = self._load_intents()

    def _load_intents(self):
        with self.intents_path.open("r", encoding="utf-8") as file:
            return json.load(file)["intents"]

    def _tokenize(self, text):
        text = text.lower()
        return re.findall(r"[a-z0-9]+", text)

    def _vectorize(self, tokens):
        return Counter(tokens)

    def _cosine_similarity(self, first, second):
        common_words = set(first) & set(second)
        numerator = sum(first[word] * second[word] for word in common_words)
        first_length = sum(value * value for value in first.values()) ** 0.5
        second_length = sum(value * value for value in second.values()) ** 0.5

        if first_length == 0 or second_length == 0:
            return 0

        return numerator / (first_length * second_length)

    def _find_best_intent(self, user_message):
        user_vector = self._vectorize(self._tokenize(user_message))
        best_intent = None
        best_score = 0

        for intent in self.intents:
            for pattern in intent["patterns"]:
                pattern_vector = self._vectorize(self._tokenize(pattern))
                score = self._cosine_similarity(user_vector, pattern_vector)
                if score > best_score:
                    best_score = score
                    best_intent = intent

        return best_intent, best_score

    def get_response(self, user_message):
        if not user_message or not user_message.strip():
            return {
                "reply": "Please type your question so I can help.",
                "intent": "empty_message",
                "confidence": 0
            }

        intent, score = self._find_best_intent(user_message)

        if intent and score >= 0.35:
            return {
                "reply": random.choice(intent["responses"]),
                "intent": intent["tag"],
                "confidence": round(score, 2)
            }

        return {
            "reply": "I am sorry, I did not understand that. You can ask about orders, returns, refunds, delivery, payments, or support hours.",
            "intent": "fallback",
            "confidence": round(score, 2)
        }


def run_cli():
    bot = CustomerServiceBot()
    print("Customer Service Chatbot")
    print("Type 'exit' to close the chatbot.")

    while True:
        user_message = input("You: ")
        if user_message.lower().strip() in {"exit", "quit"}:
            print("Bot: Goodbye!")
            break

        result = bot.get_response(user_message)
        print(f"Bot: {result['reply']}")


if __name__ == "__main__":
    run_cli()
