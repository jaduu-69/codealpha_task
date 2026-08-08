# CodeAlpha - Basic Chatbot

A simple rule-based chatbot that responds to predefined phrases using
pattern matching (regular expressions).

## Features
- Responds to greetings ("hello", "hi", "hey")
- Answers questions like "how are you", "what's your name", "what time is it"
- Tells a joke on request
- Handles thanks and goodbyes
- Falls back to a generic response for unrecognized input

## How to Run
```bash
python chatbot.py
```

## Example Conversation
```
You: hello
Bot: Hi there! What's on your mind?

You: how are you
Bot: I'm just a program, but I'm doing great! How about you?

You: tell me a joke
Bot: Why do programmers prefer dark mode? Because light attracts bugs!

You: bye
Bot: Goodbye! Have a great day!
```

## How It Works
The bot uses a list of `(pattern, responses)` rules. Each user message is
checked against these patterns using regex; if a match is found, a random
response from that rule is returned. If nothing matches, a default fallback
response is used.

## Author
Internship Project - CodeAlpha
