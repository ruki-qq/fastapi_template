import uvicorn

from core import get_logger, setup_logging

setup_logging()
logger = get_logger(__name__)


def main() -> None:
    uvicorn.run(
        "app.app:app",
        port=8000,
        host="0.0.0.0",
        reload=True,
    )


if __name__ == "__main__":
    logger.info("Starting main")
    main()
