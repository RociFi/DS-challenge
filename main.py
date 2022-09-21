
from fastapi import FastAPI
from model import MyModel

### Add additional imports here if necessary

############################################

def getScore(model : MyModel, address : str) -> int:
    ### Provide implementation

    ##########################
    return 0


PATH_TO_MODEL = "" #PROVIDE PATH TO MODEL
PATH_TO_DATABASE = "" #PROVIDE PATH TO DATABASE

app = FastAPI()
model = MyModel(PATH_TO_MODEL=PATH_TO_MODEL, PATH_TO_DATABASE=PATH_TO_DATABASE)

@app.post("/score")
async def score(address : str):
    ### Provide implementation

    ##########################

    return {"Fraud Score":  0}
