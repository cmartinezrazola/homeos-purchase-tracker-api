# ==============================================================================
# STAGE 1: Build Environment (Builder)
# ==============================================================================
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS builder

# Optimize Python and uv performance during build
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

WORKDIR /app

# Copy dependency definition files
COPY pyproject.toml uv.lock ./

# Install project dependencies using Docker cache mounts for high-speed builds
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

# ==============================================================================
# STAGE 2: Final Production Image (Runtime)
# ==============================================================================
FROM python:3.12-slim-bookworm AS runtime

# Ensure Python logs are delivered instantly without buffering
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV ENVIRONMENT=production

WORKDIR /app

# Inject the uv virtual environment directly into the system PATH
ENV PATH="/app/.venv/bin:$PATH"

# Copy the pre-compiled virtual environment from the builder stage
COPY --from=builder /app/.venv /app/.venv

# Copy the application source code (respecting .dockerignore exclusions)
COPY . .

# Expose the application port for AWS Fargate mapping
EXPOSE 8000

# Launch the production server using Gunicorn WSGI
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]