from fastapi import APIRouter

from ..database import DbSession
from ..models import SkinProfile as SkinProfileModel
from ..schemas.quiz import (
    PersistSkinProfileRequest,
    PersistSkinProfileResponse,
    SkinProfile,
    SunSafetyAnalysis,
)
from ..services import analyze_sun_safety

router = APIRouter(prefix="/quiz", tags=["quiz"])


@router.post("/skin-profile", response_model=SunSafetyAnalysis)
def receive_skin_profile(profile: SkinProfile) -> SunSafetyAnalysis:
    return analyze_sun_safety(profile)


@router.post(
    "/add-skin-profile",
    response_model=PersistSkinProfileResponse,
    status_code=201,
)
def add_skin_profile(
    payload: PersistSkinProfileRequest,
    db: DbSession,
) -> PersistSkinProfileResponse:
    """
    Persist a previously generated quiz + analysis for a signed-up user.
    The user is referenced by their email address.
    """
    record = SkinProfileModel(
        user_email=payload.email,
        quiz_response=payload.quiz.model_dump(),
        analysis_response=payload.analysis.model_dump(),
    )
    db.add(record)
    db.commit()
    db.refresh(record)

    return PersistSkinProfileResponse(
        id=str(record.id),
        email=record.user_email,
    )
