print ("Welcome to this totally normal Game Show!")
print ("Now, what is your name")
name = input()
print ("Hello" , name, "!")
print ("The rules are simple, you will be asked a question and you will have to answer it. If you get it right, you get a point. If you get it wrong, you will lose a point")
print ("                                                               ")

questions = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is the highest mountain in the world?", "answer": "Mount Everest"},
    {"question": "What is the deadlist bear in the world?", "answer": "Polar Bears"},
    {"question": "What is the largest ocean in the world?", "answer": "Pacific Ocean"},
    {"question": "What is the name of the largest gas giant in our solar system?", "answer": "Jupiter"},
    {"question": "What is the chemical symbol for gold?", "answer": "Au"},
    {"question": "What is the name of the longest river in the world?", "answer": "Nile River"},
    {"question": "What is the name of the largest desert in the world?", "answer": "Antarctica"},
    {"question": "What is the name of the largest mammal in the world?", "answer": "Blue Whale"},
    {"question": "What is the name of the smallest bone in the human body?", "answer": "stapes"}
]

score = 0
for question in questions:
    print(question["question"])
    answer = input()
    if answer.lower() == question["answer"].lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is", question["answer"])

print(name + ", your final score is", score, "out of 10.")
