from fastapi import APIRouter

from ..schemas.quiz import SkinProfile, SunSafetyAnalysis
from ..services import analyze_sun_safety

router = APIRouter(prefix="/quiz", tags=["quiz"])


@router.post("/skin-profile", response_model=SunSafetyAnalysis)
def receive_skin_profile(profile: SkinProfile) -> SunSafetyAnalysis:
    return analyze_sun_safety(profile)
