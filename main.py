# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 21:00:13 2025

@author: Dinesh kumar
"""

import uvicorn ##ASGI
from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def index():
    return {'message': 'Hello,everyone!!!'}

@app.get('/Welcome')
def get_name(name: str):
    return {'Welcome to my webpage': f'{name}'}

if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8000,reload=True)