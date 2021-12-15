import io

from starlette.responses import StreamingResponse

from app.utils import humidity as measure_utils
from app.utils import location as lunch_utils
import matplotlib.pyplot as plt
import numpy as np


async def profile_heights(profile_id: int):
    profile_measures = await measure_utils.get_profile_measures(profile_id)

    dates = list(map(lambda m: m.date, profile_measures))
    heights = list(map(lambda m: m.height, profile_measures))

    fig, ax = plt.subplots()

    ax.plot(dates, heights)
    plt.legend(["Зріст"])

    min_height = np.min(heights)
    max_height = np.max(heights)
    mean_height = round(np.mean(heights), 1)

    ax.set(xlabel='Дата', ylabel='Зріст (см)',
           title=f'Графік зросту, Мін: {min_height}, Макс: {max_height}, Сер: {mean_height}')
    plt.xticks(rotation=45, ha='right')
    fig.tight_layout()
    ax.grid()

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)

    plot_bytes = buf.read()
    plt.close()
    return StreamingResponse(io.BytesIO(plot_bytes), media_type="image/png")


async def profile_weights(profile_id: int):
    profile_measures = await measure_utils.get_profile_measures(profile_id)

    dates = list(map(lambda m: m.date, profile_measures))
    weights = list(map(lambda m: m.weight, profile_measures))

    fig, ax = plt.subplots()

    ax.plot(dates, weights)
    plt.legend(["Вага"])

    min_weight = np.min(weights)
    max_weight = np.max(weights)
    mean_weight = round(np.mean(weights), 1)

    ax.set(xlabel='Дата', ylabel='Вага (кг)',
           title=f'Графік ваги, Мін: {min_weight}, Макс: {max_weight}, Сер: {mean_weight}')
    plt.xticks(rotation=45, ha='right')
    fig.tight_layout()
    ax.grid()

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)

    plot_bytes = buf.read()
    plt.close()
    return StreamingResponse(io.BytesIO(plot_bytes), media_type="image/png")


async def profile_calories(profile_id: int):
    plot_data = await lunch_utils.get_lunches_for_plot(profile_id)

    dates = list(map(lambda d: d.date, plot_data))
    calories = list(map(lambda d: d.calories, plot_data))

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


async def profile_pcf(profile_id: int):
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
