from fastapi import FastAPI
from datetime import date
app=FastAPI()

@app.get("/")
def root():
    return{
        "this is root file"
    }

@app.get("/healthy")
def healty():
    return {
        "healthy"
    }

@app.get("/info")
def info():
    return{
        "name":"Vaibhav Nhayade",
        "emp_id":"CI21402",
        "batch_name":"AI Batch 1",
        "module_review":"github",
        "today_date":date.today()
    }