from typing import Annotated
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request,Form, BackgroundTasks, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

from sqlmodel import Session

import json
import joblib

from db import get_db, create_db_table, PayLoad
from utilities import make_prediction, save_pred


template = Jinja2Templates(directory='templates')

@asynccontextmanager
async def load_model(app: FastAPI):
    with open('ml_model/model.joblib','rb') as model_file:
        model = joblib.load(model_file)
        app.model = model
    
    create_db_table()
    yield
    app.model = None

app = FastAPI(lifespan=load_model)

app.mount(path='/static', app=StaticFiles(directory='static'), name='static')

@app.get('/')
async def redirect():
    return RedirectResponse(url = '/home')

@app.get('/home')
def loan_form(request: Request):
    return template.TemplateResponse(
        name='index.html',
        request=request)


@app.post('/predict')
async def predict(
    purpose : Annotated[str, Form()],
    interest_rate : Annotated[str, Form()],
    installment : Annotated[str, Form()],
    income : Annotated[str, Form()],
    dti : Annotated[str, Form()],
    score : Annotated[str, Form()],
    cr_line : Annotated[str, Form()],
    rev_balance : Annotated[str, Form()],
    utilization_rate : Annotated[str, Form()],
    save_pred_task: BackgroundTasks,
    session: Session = Depends(get_db)
    ):
    vars: list = [purpose, interest_rate, installment, income, dti, score, cr_line, rev_balance, utilization_rate] 
    pred = await make_prediction(vars, model=app.model)
    pred = json.dumps(pred.tolist())

    payload = PayLoad(**dict(zip(PayLoad.__annotations__.keys(),vars)))
    save_pred_task.add_task(save_pred, payload, session)

    return pred
