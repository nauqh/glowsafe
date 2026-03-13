from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy import Column, DateTime, String
import uuid
from datetime import datetime, timezone
from .database import Base


class SkinProfile(Base):
    __tablename__ = "skin_profiles"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    # Email from Neon auth DB `user` table (public."user")
    # Stored as a plain text column to avoid SQLAlchemy needing
    # the external `user` table in its metadata.
    user_email = Column(String, nullable=False, index=True)

    # Raw JSON payloads for quiz input and GlowSafe analysis output
    quiz_response = Column(JSONB, nullable=False)
    analysis_response = Column(JSONB, nullable=False)

    created_at = Column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
    )
    updated_at = Column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

    def __repr__(self) -> str:  # pragma: no cover - repr helper
        return f"<SkinProfile(id={self.id}, user_email='{self.user_email}')>"
