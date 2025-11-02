# Python with UV
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim


# Settings
RUN groupadd --system --gid 999 nonroot \
    && useradd --system --gid 999 --uid 999 --create-home nonroot

WORKDIR /app


# Installing Dependencies

ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
ENV UV_TOOL_BIN_DIR=/usr/local/bin

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project --no-dev

# Installing project

COPY app /app
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-dev



ENV PATH="/app/.venv/bin:$PATH"

ENTRYPOINT []

USER nonroot

CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]





## syntax=docker/dockerfile:1
#
## Comments are provided throughout this file to help you get started.
## If you need more help, visit the Dockerfile reference guide at
## https://docs.docker.com/engine/reference/builder/
#
#ARG PYTHON_VERSION=3.11.4
#FROM python:${PYTHON_VERSION}-slim as base
#
## Prevents Python from writing pyc files.
#ENV PYTHONDONTWRITEBYTECODE=1
#
## Keeps Python from buffering stdout and stderr to avoid situations where
## the application crashes without emitting any logs due to buffering.
#ENV PYTHONUNBUFFERED=1
#
#WORKDIR /app
#
## Create a non-privileged user that the app will run under.
## See https://docs.docker.com/go/dockerfile-user-best-practices/
#ARG UID=10001
#RUN adduser \
#    --disabled-password \
#    --gecos "" \
#    --home "/nonexistent" \
#    --shell "/sbin/nologin" \
#    --no-create-home \
#    --uid "${UID}" \
#    appuser
#
## Download dependencies as a separate step to take advantage of Docker's caching.
## Leverage a cache mount to /root/.cache/pip to speed up subsequent builds.
## Leverage a bind mount to requirements.txt to avoid having to copy them into
## into this layer.
#RUN --mount=type=cache,target=/root/.cache/pip \
#    --mount=type=bind,source=requirements.txt,target=requirements.txt \
#    python -m pip install -r requirements.txt
#
## Switch to the non-privileged user to run the application.
#USER appuser
#
## Copy the source code into the container.
#COPY . .
#
## Expose the port that the application listens on.
#EXPOSE 8080
#
## Run the application.
#CMD uv run uvicorn app.main:app --reload
