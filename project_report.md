# Project Report: Customer Service Chatbot

## 1. Project Title

Customer Service Chatbot Using Rule-Based and Simple NLP Techniques

## 2. Objective

The objective of this project is to develop a chatbot that can answer basic customer service queries automatically. The project helps understand core Artificial Intelligence and Natural Language Processing concepts such as intent detection, text preprocessing, pattern matching, and response generation.

## 3. Problem Statement

Customer support teams often receive repeated questions about order tracking, refunds, returns, payment issues, delivery time, and support availability. Manually answering these repeated queries takes time. A chatbot can handle common queries instantly and reduce the workload on human support agents.

## 4. Proposed Solution

The proposed system is a customer service chatbot that accepts a user query, identifies the most relevant intent, and returns a suitable response. The chatbot uses predefined intents and training phrases stored in a JSON file. It applies simple NLP techniques to compare the user query with known patterns.

## 5. Technologies Used

- Python
- HTML
- CSS
- JavaScript
- JSON
- Python HTTP server

## 6. NLP Techniques Used

- Lowercasing: Converts all text into lowercase to avoid case mismatch.
- Tokenization: Splits sentences into individual words.
- Bag-of-words: Represents a sentence using word frequency counts.
- Cosine similarity: Measures how similar the user query is to each stored pattern.
- Intent matching: Selects the intent with the highest similarity score.

## 7. System Modules

### Chatbot Engine

The chatbot engine is implemented in `chatbot.py`. It loads intents, preprocesses user input, calculates similarity scores, and returns the best response.

### Intent Dataset

The intent dataset is stored in `data/intents.json`. Each intent contains:

- Tag
- Example user patterns
- Bot responses

### Web Interface

The web interface is implemented using HTML, CSS, and JavaScript. It allows users to interact with the chatbot in a clean browser-based chat screen.

### Server

The server is implemented in `app.py` using Python's built-in HTTP server. It receives chat messages from the browser and sends chatbot responses back as JSON.

## 8. Algorithm

1. Start the chatbot.
2. Load all intents from the JSON file.
3. Accept a user query.
4. Convert the query to lowercase.
5. Tokenize the query into words.
6. Compare the query with each training pattern using cosine similarity.
7. Select the intent with the highest score.
8. Return a random response from the selected intent.
9. If the score is below the threshold, return a fallback response.

## 9. Sample Input and Output

| User Query | Bot Response |
| --- | --- |
| Where is my order? | To track an order, please enter your order ID on the tracking page or share it with a support agent. |
| What is your return policy? | Most products can be returned within 7 days of delivery if they are unused and in original packaging. |
| My payment failed. | If payment failed but money was deducted, it is usually reversed by the bank within 3 to 5 business days. |

## 10. Advantages

- Simple and easy to understand.
- Does not require external libraries.
- Fast response time.
- Easy to expand by adding more intents.
- Useful for learning chatbot design basics.

## 11. Limitations

- It depends on predefined patterns.
- It may not understand very complex user queries.
- It does not connect to a real order database.
- It does not store conversation history.

## 12. Future Scope

- Add machine learning-based intent classification.
- Integrate with a real customer database.
- Add multilingual support.
- Add voice input and voice output.
- Improve fallback handling with generative AI.

## 13. Conclusion

This project successfully demonstrates a simple customer service chatbot using rule-based and NLP techniques. It can answer common customer queries and provides a practical introduction to chatbot development, intent recognition, and conversational AI design.
