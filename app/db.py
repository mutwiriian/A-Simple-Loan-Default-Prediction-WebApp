from sqlmodel import SQLModel,Field, create_engine, Session
import uuid

class PayLoad(SQLModel):
    purpose: str 
    interest_rate: str 
    installment: str 
    income: str 
    dti: str 
    score: str 
    cr_line: str 
    rev_balance: str 
    utilization_rate: str 

class PredictData(PayLoad, table= True):
    id: uuid.UUID = Field(default_factory = uuid.uuid4, primary_key = True)

sqlite_filename = "loan_vars.db"
engine = create_engine(f'sqlite:///{sqlite_filename}')

def create_db_table():
    SQLModel.metadata.create_all(engine)

def get_db():
    with Session(engine) as session:
        yield session

