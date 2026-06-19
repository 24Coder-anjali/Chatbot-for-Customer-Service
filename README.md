# Customer Service Chatbot

This project is a rule-based/simple NLP chatbot for answering common customer service queries. It is suitable for an Artificial Intelligence internship project because it demonstrates chatbot design, intent classification, text preprocessing, confidence scoring, and a user-friendly chat interface.

## Features

- Answers basic customer queries about orders, returns, refunds, payments, delivery, cancellations, support hours, and human agent support.
- Uses simple NLP techniques such as lowercasing, tokenization, bag-of-words, and cosine similarity.
- Shows detected intent and confidence score for each bot reply.
- Includes a browser-based interface and a command-line mode.
- Uses only Python standard library, so no external package installation is required.

## Project Structure

```text
CHATBOT FOR CUSTOMER SERVICE/
├── app.py
├── chatbot.py
├── data/
│   └── intents.json
├── static/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── docs/
│   └── project_report.md
└── README.md
```

## How to Run

### Web chatbot

Open a terminal in this folder and run:

```bash
python app.py
```

Then open this URL in a browser:

```text
http://localhost:8000
```

On Windows, you can also double-click `start_web_chatbot.bat`.

### Command-line chatbot

```bash
python chatbot.py
```

Type `exit` to close the chatbot.

## How It Works

1. The user enters a question.
2. The chatbot cleans the text and splits it into tokens.
3. Each user message is compared with stored training patterns in `data/intents.json`.
4. The best matching intent is selected using cosine similarity.
5. If confidence is high enough, the bot returns a matching response.
6. If confidence is low, the bot returns a fallback response.

## Example Queries

- Where is my order?
- What is your return policy?
- When will I get my refund?
- My payment failed but money was deducted.
- How long does delivery take?
- Talk to a human support agent.

## Future Enhancements

- Add more intents and training phrases.
- Store customer queries in a database.
- Add login and order ID lookup.
- Use machine learning models for intent classification.
- Add speech-to-text and text-to-speech support.
