from fastapi import APIRouter, HTTPException, status

from ..database import DbSession
from ..models import SkinProfile as SkinProfileModel
from ..schemas.quiz import (
    PersistSkinProfileRequest,
    PersistSkinProfileResponse,
    SkinProfile,
    SunSafetyAnalysis,
    GetSkinProfileRequest,
    GetSkinProfileResponse,
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


@router.post(
    "/skin-profile-by-email",
    response_model=GetSkinProfileResponse,
)
def get_skin_profile_by_email(
    payload: GetSkinProfileRequest,
    db: DbSession,
) -> GetSkinProfileResponse:
    """
    Fetch the most recent skin profile + analysis for a user by email.
    The email is provided in the JSON request body.
    """
    record = (
        db.query(SkinProfileModel)
        .filter(SkinProfileModel.user_email == payload.email)
        .order_by(SkinProfileModel.created_at.desc())
        .first()
    )

    if record is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Skin profile not found for this email.",
        )

    return GetSkinProfileResponse(
        id=str(record.id),
        email=record.user_email,
        quiz=record.quiz_response,
        analysis=record.analysis_response,
    )
