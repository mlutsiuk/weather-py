from typing import List

from fastapi import APIRouter, Query
from app.utils import predict as predict_utils

router = APIRouter()


@router.get("/predict")
async def predict(pressures: List[int] = Query(None)):
    delta = predict_utils.predict(pressures)

    if 20 >= delta >= -20:
        explanation = "Незначні зміни погоди або стала погода."
    elif 20 <= delta <= 125:
        explanation = "Антициклон, незначне покращення погоди та покращення у довгостроковій перспективі."
    elif delta >= 125:
        explanation = "Значне покращення погоди, короткочасна зміна."
    elif -20 > delta > -125:
        explanation = "Циклон, незначне погіршення погоди та погрішення у довгостроковій перспективі."
    else:
        explanation = "Значне погіршення погоди, буря зимою та гроза літом."

    return {"delta": delta, "explanation": explanation}
