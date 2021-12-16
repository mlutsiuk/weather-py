import io

from starlette.responses import StreamingResponse

from app.utils import temperature as temperature_utils
from app.utils import pressure as pressure_utils
from app.utils import humidity as humidity_utils
import matplotlib.pyplot as plt
import numpy as np


async def location_humidity(location_id: int):
    location_humidity = await humidity_utils.get_all_location_humidity_records(location_id)

    dates = list(map(lambda r: r.date, location_humidity))
    humidity = list(map(lambda r: r.humidity, location_humidity))

    fig, ax = plt.subplots()

    ax.plot(dates, humidity)
    plt.legend(["Вологість"])

    ax.set(xlabel='Дата', ylabel='Вологість у %', title='Вологість у локації')
    plt.xticks(rotation=45, ha='right')
    fig.tight_layout()
    ax.grid()

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)

    plot_bytes = buf.read()
    plt.close()
    return StreamingResponse(io.BytesIO(plot_bytes), media_type="image/png")


async def location_pressure(location_id: int):
    location_pressure = await pressure_utils.get_all_location_pressure_records(location_id)

    dates = list(map(lambda r: r.date, location_pressure))
    pressure = list(map(lambda r: r.pressure, location_pressure))

    fig, ax = plt.subplots()

    ax.plot(dates, pressure)
    plt.legend(["Тиск"])

    ax.set(xlabel='Дата', ylabel='Тиск у Па', title='Атмосферний тиск')
    plt.xticks(rotation=45, ha='right')
    fig.tight_layout()
    ax.grid()

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)

    plot_bytes = buf.read()
    plt.close()
    return StreamingResponse(io.BytesIO(plot_bytes), media_type="image/png")


async def location_temperature(location_id: int):
    location_temperature = await temperature_utils.get_all_location_temperature_records(location_id)

    dates = list(map(lambda r: r.date, location_temperature))
    temperature = list(map(lambda r: r.temperature, location_temperature))

    fig, ax = plt.subplots()

    ax.plot(dates, temperature)
    plt.legend(["Температура"])

    ax.set(xlabel='Дата', ylabel='Температура у °C', title='Температура на локації')
    plt.xticks(rotation=45, ha='right')
    fig.tight_layout()
    ax.grid()

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)

    plot_bytes = buf.read()
    plt.close()
    return StreamingResponse(io.BytesIO(plot_bytes), media_type="image/png")
