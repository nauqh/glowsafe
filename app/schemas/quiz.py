from typing import List, Optional

from pydantic import BaseModel


class SkinProfile(BaseModel):
    skinTypeId: str
    locationId: str
    activityIds: List[str]
    uvRiskLevel: str
    burnHistory: Optional[str] = None
    workPattern: Optional[str] = None
    peakSunExposure: Optional[str] = None
    sunscreenFrequency: Optional[str] = None
    protectionHabits: Optional[List[str]] = None


class SunSafetyVibe(BaseModel):
    hex: str
    label: str


class SunSafetySection(BaseModel):
    heading: str
    body: str


class SunSafetyAnalysis(BaseModel):
    vibe: SunSafetyVibe
    sections: List[SunSafetySection]


class PersistSkinProfileRequest(BaseModel):
    """
    Payload sent after signup to persist a quiz + analysis
    for a specific authenticated user, identified by email.
    """

    email: str
    quiz: SkinProfile
    analysis: SunSafetyAnalysis


class PersistSkinProfileResponse(BaseModel):
    id: str
    email: str


class GetSkinProfileRequest(BaseModel):
    """
    Request payload to fetch a skin profile by email.
    """

    email: str


class GetSkinProfileResponse(BaseModel):
    """
    Full persisted skin profile + analysis for a user.
    """

    id: str
    email: str
    quiz: SkinProfile
    analysis: SunSafetyAnalysis
