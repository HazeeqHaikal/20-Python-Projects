if __name__ =="__main__":
    quiz = {
        "question1": {
            "question": "What is the capital of France?",
            "answer": "Paris"
        },
        "question2": {
            "question": "What is the capital of Germany?",
            "answer": "Berlin"
        },
        "question3": {
            "question": "What is the capital of Spain?",
            "answer": "Madrid"
        },
        "question4": {
            "question": "What is the capital of Italy?",
            "answer": "Rome"
        },
        "question5": {
            "question": "What is the capital of Poland?",
            "answer": "Warsaw"
        },
        "question6": {
            "question": "What is the capital of Portugal?",
            "answer": "Lisbon"
        },
        "question7": {
            "question": "What is the capital of Greece?",
            "answer": "Athens"
        },
        "question8": {
            "question": "What is the capital of Sweden?",
            "answer": "Stockholm"
        },
        "question9": {
            "question": "What is the capital of Norway?",
            "answer": "Oslo"
        },
        "question10": {
            "question": "What is the capital of Denmark?",
            "answer": "Copenhagen"
        },
        "question11": {
            "question": "What is the capital of Finland?",
            "answer": "Helsinki"
        },
        "question12": {
            "question": "What is the capital of Iceland?",
            "answer": "Reykjavik"
        },
        "question13": {
            "question": "What is the capital of Ireland?",
            "answer": "Dublin"
        },
        "question14": {
            "question": "What is the capital of the Malaysia?",
            "answer": "Kuala Lumpur"
        }
    }
    
    score = 0

    for key, value in quiz.items():
        print(value["question"])
        answer = input("Your answer: ")
        if answer.lower() == value["answer"].lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The real answer is {value['answer']}\n")

    print(f"Your score is {score}/{len(quiz)}")
    print(f"Your percentage is {score//len(quiz)*100}%")