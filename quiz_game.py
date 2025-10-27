quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. Rome", "C. Madrid", "D. Berlin"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B"
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["A. William Wordsworth", "B. Charles Dickens", "C. William Shakespeare", "D. Jane Austen"],
        "answer": "C"
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Orca"],
        "answer": "B"
    },
    {
        "question": "Which language is primarily used for web development?",
        "options": ["A. Python", "B. JavaScript", "C. C++", "D. Java"],
        "answer": "B"
    },
    {
        "question": "In which year did India gain independence?",
        "options": ["A. 1945", "B. 1947", "C. 1950", "D. 1952"],
        "answer": "B"
    },
    {
        "question": "Which gas do plants absorb during photosynthesis?",
        "options": ["A. Oxygen", "B. Carbon Dioxide", "C. Nitrogen", "D. Hydrogen"],
        "answer": "B"
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["A. Oxygen", "B. Osmium", "C. Gold", "D. Ozone"],
        "answer": "A"
    },
    {
        "question": "What is the square root of 81?",
        "options": ["A. 9", "B. 8", "C. 7", "D. 6"],
        "answer": "A"
    },
    {
        "question": "Who is known as the Father of the Nation in India?",
        "options": ["A. Bhagat Singh", "B. Mahatma Gandhi", "C. Jawaharlal Nehru", "D. Sardar Patel"],
        "answer": "B"
    }
]

score = 0  
for i, q in enumerate(quiz_data, start=1):
    print(f'Questaions {i}: {q["question"]}')
    for options in q["options"]:
        print(options)
    take_ans = input("Enter the option: ").strip().upper()
    if take_ans == q["answer"]:
        score+=1
        print("Yeee!!! Right Answer")
    else:
        print(f'Wrong The correct option is {q["answer"]}')
print(f'Ypur final score is {score}')