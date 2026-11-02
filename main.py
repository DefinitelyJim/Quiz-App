from fastapi import FastAPI
from pydantic import BaseModel
import httpx, random, html, uuid


app = FastAPI()

rounds = {}

class Answer(BaseModel):
    question_number: int
    choice: str

@app.get("/")
def home():
    return {"message": "Quiz app is running"}

@app.get("/greeting/{name}")
def greeting(name):
    return {"message": f"Welcome {name} to the Quiz App!"}

@app.get("/questions")
async def get_questions():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://opentdb.com/api.php?amount=3&type=multiple")

    data = response.json()
    questions = []
    round_id = str(uuid.uuid4())
    answer_sheet = []

    #q is short for question
    for q in data["results"]:

        incorrect_answers = q["incorrect_answers"] # Grabs incorrect answer from api
        correct_answer = q["correct_answer"] # Grabs correct answer from api
        complete_answers = incorrect_answers + [correct_answer] # Combines the two
        random.shuffle(complete_answers) # Shuffles the answers
        clean_options = [] # Empty list to store answers for cleaning
        answer_sheet.append(html.unescape(correct_answer))

        # Cleans answer of HTML bullshit ready for presentation
        for option in complete_answers:
            clean_options.append(html.unescape(option))

        #Card dictionary
        card = {
            "question": html.unescape(q["question"]),
            "category": html.unescape(q["category"]),
            "difficulty": html.unescape(q["difficulty"]),
            "options": clean_options,
        }

        questions.append(card)

    rounds[round_id] = answer_sheet

    return {"round_id": round_id, "questions": questions}

@app.post("/rounds/{round_id}/answer")
def check_answer(round_id: str, answer: Answer):
    answer_sheet = rounds[round_id]
    correct_answer = answer_sheet[answer.question_number]
    is_correct = answer.choice == correct_answer
    return{"correct": is_correct, "correct_answer": correct_answer}
