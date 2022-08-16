"""
Author: Paul Owe
Date: 29 July, 2022
"""

from fastapi import FastAPI
from router import blog_get
from router import user
from router import blog_post
from db import models
from db.database import engine
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pandas as pd
import matplotlib.pyplot as plt
import os

app = FastAPI()

app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory='templates')

app.include_router(user.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)



def save_fig(fig_id, tight_layout=True, fig_extension="png", resolution=300):
    # Where to save the figures
    PROJECT_ROOT_DIR = "."
    IMAGES_PATH = os.path.join(PROJECT_ROOT_DIR, "static")
    os.makedirs(IMAGES_PATH, exist_ok=True)
    path = os.path.join(IMAGES_PATH, fig_id + "." + fig_extension)
    print("Saving figure", fig_id)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)

@app.get('/', response_class=HTMLResponse)
def index(request:Request):
    return templates.TemplateResponse('visualization.html', {'request':request})


# Create database
models.Base.metadata.create_all(engine)


# To run it uvicorn main:app --reload

