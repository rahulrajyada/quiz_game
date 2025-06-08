quiz = {
    "What is the capital of Nepal?":"kathmandu",
    "How many provience are there in Nepal":"7",
    "How many district are there in Nepal":"77",
    "what is the chemical sysmbol of water":"H2O",
    "Which Planet is known as Red Planet":"Mars",
    "What is the tallest mountain in the world?": "mount everest",
    "In which year did Nepal become a republic?": "2008",
    "What is the national flower of Nepal?": "rhododendron",
    "Which river is the longest in Nepal?": "karnali",
    "What is the currency of Nepal?": "rupee",
    "Which festival is known as the festival of lights in Nepal?": "tihar",
    "What is the official language of Nepal?": "nepali",
    "Who wrote 'Romeo and Juliet'?":"Shakespeare"
        }
  
score = []

for question,correct_answer in quiz.items():
    print(question)
    user_answer = input("Enter your answer: ").strip().lower()
    
    if user_answer.lower() == correct_answer.lower():
        print("Correct answer! \n")
        score.append(1)
    else:
        print(f"Incorrect answer!The correct answer was {correct_answer} \n")
        score.append(0)
        
total_question = len(score)
correct_answers = sum(score)
percentage = (correct_answers/total_question) * 100

print(f"Your Score: {correct_answers} / {total_question} ")
print(f"Percentage: {percentage}")
        
