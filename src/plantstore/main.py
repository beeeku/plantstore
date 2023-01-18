import uvicorn

from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health() -> None:
    pass


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
