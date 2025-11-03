FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim
WORKDIR /app
ADD . /app
RUN uv sync
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]