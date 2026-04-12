questions = [
	{"question": "What is the capital of France?", "answer": "paris"},
	{"question": "How many sides does a triangle have?", "answer": "3"},
	{"question": "What planet is closest to the sun?", "answer": "mercury"},
	{"question": "What language are you coding right now?", "answer": "python baby"}
]

score = 0

print("Welcome to the Quiz Game!")
print(f"Ther are {len(questions)} questions.  Good luck!\n")

for item in questions:
	answer = input(item["question"] + "\nYour answer: ").lower().strip()
	
	if answer == item["answer"]:
		print("Correct! yass queen!\n")
		score += 1
	else:
		print(f"WRONG!!! omg wow smh. The answer was{item['answer']}\n")
		
percentage = (score / len(questions)) * 100

print(f"Quiz Over! You got {score} out of {len(questions)} correct.")
print(f"Your score: {percentage}%")

if percentage == 100:
	print("Wow Perfect Score! Absolute baddie yesss!")
elif percentage >= 60:
	print("Not bad, you passed.")
else:
	print("Womp womp, do it over")