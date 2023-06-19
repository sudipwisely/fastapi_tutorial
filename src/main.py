from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data':{'name':'sudip'}}

@app.get('/about')
def about():
    return {'data':{'pagename':'about'}}

@app.get('/course')
def course():
    return {'data':'all courses'}

@app.get('/course/{id}')
def individualcourse(id: int):
    return {'course_id':id}