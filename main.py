from fastapi import FastAPI
import httpx
import random

app = FastAPI()

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



    #q is short for question
    for q in data["results"]:

        incorrect_answers = q["incorrect_answers"] # Grabs incorrect answer from api
        correct_answer = q["correct_answer"] # Grabs correct answer from api
        complete_answers = incorrect_answers + [correct_answer] # Combines the two
        random.shuffle(complete_answers) # Shuffles the answers

        #Card dictionary
        card = {
            "question": q["question"],
            "category": q["category"],
            "difficulty": q["difficulty"],
            "options": complete_answers,
        }

        questions.append(card)

    return questions