from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return "Sample Method"

@app.get('/property/{id}')
def getProperty(id): 
    return {f"This is new property {id}"}