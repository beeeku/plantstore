import uvicorn

from fastapi import FastAPI

from plantstore.generated.server.register import register
from plantstore.owner import OwnerService
from plantstore.plant import PlantService


app = FastAPI()


register(
    app,
    owner=OwnerService(),
    plant=PlantService(),
)


def start() -> None:
    """Launched with `poetry run start` at root level"""

    uvicorn.run(
        "plantstore.main:app",
        host="0.0.0.0",
        port=8080,
        reload=True,
    )


if __name__ == "__main__":
    start()
