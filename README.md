🦷 DentalBot – Rule-Based Chatbot (Console Version)
📌 Description
DentalBot is a simple, rule-based chatbot built in Python using Regular Expressions (re module). It simulates a basic dental clinic assistant that can answer frequently asked questions (FAQs) about the clinic's services, timings, and location.

🧠 Features
Responds to greetings like hello, hi, good morning, etc.

Answers  FAQ-type questions, including:

Working hours

Clinic location

Walk-in appointments

Services offered

Contact details

Pediatric care

Gracefully handles unknown or unsupported questions

Terminates on commands like bye, exit, terminate, or quit

Uses regex to match patterns in the input text (more flexible than exact word matching)

🔧 Requirements
Python 3.x 
regEx module

▶️ How to Run
Save the code in a file named chatbot.py

Open a terminal or command prompt in that directory

Run the script:
pip install regex
python chatbot.py
Interact with the bot via the command line

📋 Example Questions to Try
"What are your working hours?"

"Where is your clinic located?"

"Do you treat kids?"

"How can I contact you?"

"What services do you offer?"

"Do you accept walk-in appointments?"

"Hello"

"Bye"

💡 How It Works
The chatbot uses regular expressions (re.search) to match key phrases or patterns in user input.

Based on the matched pattern, a response is returned from the faq_responses dictionary.

If no pattern matches, a default fallback response is used.

😅 Limitations
Only matches predefined patterns

Cannot learn or understand outside its rule set

No natural language understanding (NLU)

🚀 Future Improvements
Add fuzzy matching using fuzzywuzzy

Build a GUI version using Tkinter

Expand the FAQ list and support synonyms

Integrate with OpenAI for advanced language understandin
