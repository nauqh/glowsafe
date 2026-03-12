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

