# Using python:3.10 as base image
FROM python:3.10        

# ensure Python output is sent directly to the terminal without buffering
ENV PYTHONUNBUFFERED=1

# prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Docker container ko working directory /app
WORKDIR /app


# local computer ko requirements.txt lai container ko requirements.txt ma lagera paste gareko
COPY requirements.txt requirements.txt


# command for upgrading pip version in the container
RUN pip3 install --upgrade pip


# command for installing all the requirements in docker container
RUN pip3 install --no-cache-dir -r requirements.txt


# copying all the files & folders in local computer to the /app directory in the container
COPY . /app


# exposing the fastapi appllication to the port 8000
EXPOSE 8000


# Default application run command only for development
CMD uvicorn main:app --reload --host 0.0.0.0 --port 8000

# # Default application run command for production
# CMD uvicorn main:app --host 0.0.0.0 --port 8000









# # syntax=docker/dockerfile:1

# # Comments are provided throughout this file to help you get started.
# # If you need more help, visit the Dockerfile reference guide at
# # https://docs.docker.com/go/dockerfile-reference/

# # Want to help us make this template better? Share your feedback here: https://forms.gle/ybq9Krt8jtBL3iCk7

# ARG PYTHON_VERSION=3.10
# FROM python:${PYTHON_VERSION}-slim as base

# # Prevents Python from writing pyc files.
# ENV PYTHONDONTWRITEBYTECODE=1

# # Keeps Python from buffering stdout and stderr to avoid situations where
# # the application crashes without emitting any logs due to buffering.
# ENV PYTHONUNBUFFERED=1

# WORKDIR /app

# # Create a non-privileged user that the app will run under.
# # See https://docs.docker.com/go/dockerfile-user-best-practices/
# ARG UID=10001
# RUN adduser \
#     --disabled-password \
#     --gecos "" \
#     --home "/nonexistent" \
#     --shell "/sbin/nologin" \
#     --no-create-home \
#     --uid "${UID}" \
#     appuser

# # Download dependencies as a separate step to take advantage of Docker's caching.
# # Leverage a cache mount to /root/.cache/pip to speed up subsequent builds.
# # Leverage a bind mount to requirements.txt to avoid having to copy them into
# # into this layer.
# RUN --mount=type=cache,target=/root/.cache/pip \
#     --mount=type=bind,source=requirements.txt,target=requirements.txt \
#     python -m pip install -r requirements.txt

# # Switch to the non-privileged user to run the application.
# USER appuser

# # Copy the source code into the container.
# COPY . .

# # Expose the port that the application listens on.
# EXPOSE 8000

# # Run the application.
# CMD uvicorn main:app --reload --port 8000 --host 0.0.0.0
