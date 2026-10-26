from fastapi import FastAPI
import httpx

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
        questions.append(q["question"])
    return questions