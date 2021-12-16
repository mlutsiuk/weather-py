import io

from starlette.responses import StreamingResponse

from app.utils import temperature as temperature_utils
from app.utils import pressure as pressure_utils
from app.utils import humidity as humidity_utils
import matplotlib.pyplot as plt
import numpy as np


async def location_humidity(profile_id: int):
    location_humidity = await humidity_utils.get_all_location_humidity_records(profile_id)

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


async def location_pressure(profile_id: int):
    location_pressure = await pressure_utils.get_all_location_pressure_records(profile_id)

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


async def location_temperature(profile_id: int):
    plot_data = await temperature_utils.get_all_location_temperature_records(profile_id)

    dates = list(map(lambda r: r.date, plot_data))
    calories = list(map(lambda r: r.calories, plot_data))

    fig, cal = plt.subplots()

    cal.plot(dates, calories)
    plt.legend(["Калорії"])

    min_calories = int(np.min(calories))
    max_calories = int(np.max(calories))
    mean_calories = round(np.mean(calories), 1)

    cal.set(xlabel='Дата', ylabel='Калорії',
            title=f'Графік калорій, Мін: {min_calories}, Макс: {max_calories}, Сер: {mean_calories}')
    plt.xticks(rotation=45, ha='right')
    fig.tight_layout()
    cal.grid()

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)

    plot_bytes = buf.read()
    plt.close()
    return StreamingResponse(io.BytesIO(plot_bytes), media_type="image/png")


async def weather_prediction(profile_id: int):
    plot_data = await lunch_utils.get_lunches_for_plot(profile_id)

    dates = list(map(lambda d: d.date, plot_data))
    proteins = list(map(lambda d: d.proteins, plot_data))
    fats = list(map(lambda d: d.fats, plot_data))
    carbs = list(map(lambda d: d.carbs, plot_data))

    fig, cal = plt.subplots()

    cal.plot(dates, proteins)
    cal.plot(dates, fats)
    cal.plot(dates, carbs)
    plt.legend(["Білки", "Жири", "Вуглеводи"])

    cal.set(xlabel='Дата', ylabel='Вага (гр)',
            title='Графік харчування')
    plt.xticks(rotation=45, ha='right')
    fig.tight_layout()
    cal.grid()

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)

    plot_bytes = buf.read()
    plt.close()
    return StreamingResponse(io.BytesIO(plot_bytes), media_type="image/png")
