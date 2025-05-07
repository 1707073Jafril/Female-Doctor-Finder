from fastapi import FastAPI

app = FastAPI(title = "Female Doctor Finder")

@app.get("/")
def home():
    return "Find female doctor for you"