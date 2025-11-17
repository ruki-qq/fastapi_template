from sqlalchemy.ext.asyncio import AsyncSession

from app.app import app
from core import db_helper


def override_db_session(session: AsyncSession) -> None:
    """Override db session dependencies"""

    def override_get_scoped_session():
        return session

    async def override_session_dependency():
        yield session

    app.dependency_overrides[db_helper.get_scoped_session] = override_get_scoped_session
    app.dependency_overrides[db_helper.session_dependency] = override_session_dependency
