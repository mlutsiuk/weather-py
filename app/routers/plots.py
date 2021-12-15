from fastapi import APIRouter

from app.utils import plots as plot_utils

router = APIRouter()


@router.get("/profiles/{profile_id}/plots/weight")
async def profile_weights_plot(profile_id: int):
    return await plot_utils.profile_weights(profile_id)


@router.get("/profiles/{profile_id}/plots/height")
async def profile_heights_plot(profile_id: int):
    return await plot_utils.profile_heights(profile_id)


@router.get("/profiles/{profile_id}/plots/pfc")
async def profile_lunches_plot(profile_id: int):
    return await plot_utils.profile_pcf(profile_id)


@router.get("/profiles/{profile_id}/plots/calories")
async def profile_lunches_plot(profile_id: int):
    return await plot_utils.profile_calories(profile_id)
