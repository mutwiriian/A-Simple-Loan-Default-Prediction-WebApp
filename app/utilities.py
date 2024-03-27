from pandas import DataFrame
from sqlmodel import Session
from db import PayLoad, PredictData

async def make_prediction(vars: list, model):
    vars: DataFrame = DataFrame([vars], columns = ['purpose', 'int_rate', 'installment', 'log_annual_inc', 'dti', 'fico',
       'days_with_cr_line', 'revol_bal', 'revol_util'])
    prediction = model.predict(vars)[0]
    
    return prediction


def save_pred(payload: PayLoad, session: Session):
    pred_data = PredictData.model_validate(payload)
    
    session.add(pred_data)
    session.commit()