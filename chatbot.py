import random

# Define responses for the chatbot
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "hey": ["Hello!", "Hi there!", "Hey!"],
    "hello": ["Hello!", "Hi there!", "Hey!"],
    "how are you?": ["I'm good, thank you!", "I'm doing well, thanks for asking!"],
    "how are you": ["I'm good, thank you!", "I'm doing well, thanks for asking!"],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a great day!"],
    "thankyou": ["You are welcome!"],
    "when will the new session start":["14th Feb 2024"],
    "i want to know something":["it would be my pleasure if i was able to help you","please go ahead!"],
    "what is your name":["My name is Sivi"],
    "what is your name?":["My name is Sivi"],
    "syllabus of robotics and ai":["Sure you can visit at: (https://www.bing.com/ck/a?!&&p=e511528f99472acbJmltdHM9MTcwNzY5NjAwMCZpZ3VpZD0xY2ZjYjA1NS1hN2UzLTZjYTItMWZjZS1hMmJkYTZlNTZkNGUmaW5zaWQ9NTIxNw&ptn=3&ver=2&hsh=3&fclid=1cfcb055-a7e3-6ca2-1fce-a2bda6e56d4e&psq=jc+bose+university+syllabus+of+robotics&u=a1aHR0cHM6Ly9qY2Jvc2V1c3QuYWMuaW4vYXNzZXRzL3VwbG9hZHMvbWVkaWEvMjQyOWYyZGIyM2EwMDczMzk4NThkNjBiNGRiNTNjZjkucGRm&ntb=1)"],
    "syllabus of rai":["Sure you can visit at: (https://www.bing.com/ck/a?!&&p=e511528f99472acbJmltdHM9MTcwNzY5NjAwMCZpZ3VpZD0xY2ZjYjA1NS1hN2UzLTZjYTItMWZjZS1hMmJkYTZlNTZkNGUmaW5zaWQ9NTIxNw&ptn=3&ver=2&hsh=3&fclid=1cfcb055-a7e3-6ca2-1fce-a2bda6e56d4e&psq=jc+bose+university+syllabus+of+robotics&u=a1aHR0cHM6Ly9qY2Jvc2V1c3QuYWMuaW4vYXNzZXRzL3VwbG9hZHMvbWVkaWEvMjQyOWYyZGIyM2EwMDczMzk4NThkNjBiNGRiNTNjZjkucGRm&ntb=1)"],
    "courses available":["https://www.jcboseust.ac.in/admissions-courses"],
    "available courses":["https://www.jcboseust.ac.in/admissions-courses"],
    "what are the available courses":["https://www.jcboseust.ac.in/admissions-courses"],
    "syllabus of computer engineering":["https://www.jcboseust.ac.in/assets/uploads/media/0135a60d0310b33a480d06e86798f507.pdf"],
    "syllabus of ce":["https://www.jcboseust.ac.in/assets/uploads/media/0135a60d0310b33a480d06e86798f507.pdf"]
    }

def chat():
    print("Sivi: Hello! How can I help you today?")
    while True:
        user_input = input("You: ").lower()
        response = responses.get(user_input, ["I'm sorry, I don't understand that."])
        print("Sivi:", random.choice(response))

        if user_input == "bye":
            break

if __name__ == "__main__":
    chat()

