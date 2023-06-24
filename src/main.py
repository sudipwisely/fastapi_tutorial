from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data':{'name':'sudip'}}

@app.get('/contact')
def contact():
    return {'data':{'page':'this is contact page'}}

@app.get('/contact')
def contact():
    return {'data':{'page':'this is contact page'}}

@app.get('/all_courses')
def all_courses():
    return {'data':{'page':'all courses list'}}

@app.get('/course/unpublished')
def unpublished():
    return {'data':'unpublished'}

@app.get('/course/{id}')
def single_course(id:int):
    return {'courseID':id}

@app.get('/course/{id}/comments')
def comments():
    return {'data':{'comments':'coments'}}