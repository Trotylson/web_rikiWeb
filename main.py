from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory='templates')

# MAIN PAGES \/
@app.get('/')
def home(request:Request):
    return templates.TemplateResponse('home.html', {'request': request})

@app.get('/courses')
def home(request:Request):
    return templates.TemplateResponse('courses.html', {'request': request})

@app.get('/services')
def home(request:Request):
    return templates.TemplateResponse('services.html', {'request': request})

@app.get('/shops')
def home(request:Request):
    return templates.TemplateResponse('shops.html', {'request': request})

@app.get('/contact')
def home(request:Request):
    return templates.TemplateResponse('contact.html', {'request': request})

@app.get('/diverstoolbox')
def home(request:Request):
    return templates.TemplateResponse('diverstoolbox.html', {'request': request})


# COURSE PAGES \/
@app.get('/tryDive')
def home(request:Request):
    return templates.TemplateResponse('tryDive.html', {'request': request})

@app.get('/owsd')
def home(request:Request):
    return templates.TemplateResponse('owsd.html', {'request': request})

# @app.get('/{id}')
# def home(request:Request):
#     return templates.TemplateResponse('details{id}.html', {'request': request})
