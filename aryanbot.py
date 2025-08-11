from datetime import datetime

print("🤖 AryanBot: नमस्ते! मैं AryanBot हूं — AI और Daily Life का Expert Bot 🤖\n")

while True:
    user_input = input("You: ").lower()

    if user_input in ["bye", "exit", "quit"]:
        print("अलविदा! फिर मिलेंगे 👋")
        break

    if user_input in ["hello", "hi"]:
        print("Hello! कैसे हो आप?")

    elif user_input == "how are you":
        print("मैं बढ़िया हूं! आप कैसे हो?")

    elif user_input in ["your name", "who are you"]:
        print("मेरा नाम AryanBot है, मुझे Aryan Sharma ने बनाया है।")

    elif user_input == "time":
        now = datetime.now().strftime("%H:%M")
        print("अभी का समय है", now)

    elif user_input == "date":
        today = datetime.now().strftime("%A, %d %B %Y")
        print("आज की तारीख है", today)

    elif user_input in ["what is ai", "artificial intelligence"]:
        print("AI यानी Artificial Intelligence — मशीन को इंसान जैसा सोचने की क्षमता देना।")

    elif user_input == "what is machine learning":
        print("Machine Learning AI का हिस्सा है जिसमें सिस्टम डेटा से खुद सीखता है।")

    elif user_input == "what is nlp":
        print("NLP यानी Natural Language Processing — मशीन को इंसानी भाषा समझना सिखाना।")

    elif user_input == "sad":
        print("चिंता मत करो, मैं यहां हूं 😊")

    elif user_input == "happy":
        print("बहुत अच्छा! खुश रहो 🌟")

    else:
        print("माफ करना, मैं उस सवाल को नहीं समझ पाया।")