
import re
import random
from datetime import datetime

def chatbot():
    print("NOVA - Personal Student Assistant")
    print("Hello! How can I help you?")
    print("Type 'bye' to exit.")

    while True:
        user = input("\nYou: ").lower().strip()

        if re.search(r"\b(hi|hello|hey)\b", user):
            print("NOVA:", random.choice([
                "Hello! How can I help you?",
                "Hey! Ready to study?",
                "Hi! What's on your mind?"
            ]))

        elif re.search(r"\b(how are you|how r u)\b", user):
            print("NOVA: I'm doing great! How can I help you?")

        elif re.search(r"\b(your name|who are you)\b", user):
            print("NOVA: I am NOVA, your personal student assistant.")

        elif re.search(r"\b(study|learn)\b", user):
            print("NOVA: What would you like to study?")
            print("1. Artificial Intelligence")
            print("2. Machine Learning")
            print("3. Python")
            print("4. OOP")
            print("5. Computer Networks")
            print("6. Data Structures")

        elif re.search(r"\b(ai|artificial intelligence)\b", user):
            print("NOVA: AI enables machines to perform tasks that require human intelligence.")

        elif re.search(r"\b(machine learning|ml)\b", user):
            print("NOVA: Machine Learning allows computers to learn patterns from data.")

        elif re.search(r"\b(python|programming)\b", user):
            print("NOVA: Python is a simple, high-level programming language.")

        elif re.search(r"\b(oop|object oriented)\b", user):
            print("NOVA: OOP is based on classes and objects. Its four concepts are Encapsulation, Inheritance, Polymorphism and Abstraction.")

        elif re.search(r"\b(computer networks|networking|cn)\b", user):
            print("NOVA: Computer Networks deals with communication between computers and devices.")

        elif re.search(r"\b(data structures|dsa|arrays|stack|queue|tree|graph)\b", user):
            print("NOVA: Data Structures organize data efficiently. Examples include Arrays, Linked Lists, Stacks, Queues, Trees and Graphs.")

        elif re.search(r"\b(exam|test|revision|revise|prepare)\b", user):
            print("NOVA: Study important topics, practice questions and revise your mistakes.")

        elif re.search(r"\b(motivation|motivate|inspire)\b", user):
            print("NOVA:", random.choice([
                "Small progress is still progress.",
                "Believe in yourself and keep working.",
                "Every step brings you closer to your goal."
            ]))

        elif re.search(r"\b(tired|stressed|sleepy)\b", user):
            print("NOVA: Take a short break, drink some water and relax.")

        elif re.search(r"\b(time|current time)\b", user):
            print("NOVA: Current time is", datetime.now().strftime("%I:%M %p"))

        elif re.search(r"\b(joke|funny|laugh)\b", user):
            print("NOVA:", random.choice([
                "Why do programmers prefer dark mode? Because light attracts bugs!",
                "Why was the computer cold? Because it left its Windows open!",
                "My code works, but I don't know why!"
            ]))

        elif re.search(r"\b(help|commands|features)\b", user):
            print("NOVA: I can help with AI, ML, Python, OOP, Networks, DSA, exams, motivation and jokes.")

        elif re.search(r"\b(bye|goodbye|exit|quit|stop)\b", user):
            print("NOVA: Goodbye! Keep learning!")
            break

        else:
            print("NOVA: Sorry, I don't understand. Type 'help' to see what I can do.")

chatbot()
