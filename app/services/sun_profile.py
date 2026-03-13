import json
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

from ..schemas.quiz import SunSafetyAnalysis, SkinProfile

load_dotenv()


_INSTRUCTIONS_PATH = (
    Path(__file__).resolve().parents[2] / "docs" / "instructions.txt"
)
_INSTRUCTIONS = _INSTRUCTIONS_PATH.read_text(encoding="utf-8")


_client = OpenAI()


def analyze_sun_safety(profile: SkinProfile) -> SunSafetyAnalysis:
    payload = profile.model_dump()

    response = _client.responses.parse(
        model="gpt-5-mini-2025-08-07",
        input=[
            {
                "role": "system",
                "content": _INSTRUCTIONS,
            },
            {
                "role": "user",
                "content": json.dumps(payload),
            },
        ],
        text_format=SunSafetyAnalysis,
        max_output_tokens=400,
    )

    return response.output_parsed
