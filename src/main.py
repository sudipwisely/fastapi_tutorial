from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data':{'name':'sudip'}}

@app.get('/contact')
def contact():
    return {'data':{'page':'this is contact page'}}

@app.get('/blogs')
def all_blogs(limit=None,published:bool=None):
    if limit:
        if published:
            return {'data':{'blogs': f'{limit} published blogs displayed'}}
        else:
            return {'data':{'blogs': f'{limit} unpublished blogs displayed'}}
    else:
        if published:
            return {'data':{'blogs': 'all published blogs displayed'}}
        else:
            return {'data':{'blogs': 'all unpublished blogs displayed'}}

@app.get('/blog/{id}')
def single_blog(id:int):
    return {'data':f'{id} blog id displayed.'}

