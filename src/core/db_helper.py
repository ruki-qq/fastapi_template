from asyncio import current_task
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_scoped_session,
    async_sessionmaker,
    create_async_engine,
)

from .config import settings


class DBHelper:
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(url=url, echo=echo)
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    def get_scoped_session(self):
        return async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task,
        )

    async def session_dependency(self) -> AsyncGenerator[AsyncSession]:
        async with self.session_factory() as session:
            yield session
            await session.close()

    async def scoped_session_dependency(
        self,
    ) -> AsyncGenerator[async_scoped_session[AsyncSession]]:
        session = self.get_scoped_session()
        yield session
        await session.remove()


db_helper = DBHelper(
    url=settings.db.url,
    echo=settings.db.echo,
)
