from fastapi import APIRouter

from app.utils import plots as plot_utils

router = APIRouter()


@router.get("/locations/{location_id}/visualise/humidity-records")
async def location_humidity_plot(location_id: int):
    return await plot_utils.location_humidity(location_id)


@router.get("/locations/{location_id}/visualise/pressure-records")
async def location_pressure_plot(location_id: int):
    return await plot_utils.location_pressure(location_id)


@router.get("/locations/{location_id}/visualise/temperature-records")
async def location_temperature_plot(location_id: int):
    return await plot_utils.location_temperature(location_id)


@router.get("/locations/{location_id}/visualise/weather-prediction")
async def profile_lunches_plot(location_id: int):
    return await plot_utils.weather_prediction(location_id)
