# Use NVIDIA CUDA base for Ubuntu 24.04
FROM nvidia/cuda:12.1.0-base-ubuntu22.04

# Install system dependencies for MuJoCo and OpenGL
RUN apt-get update && apt-get install -y \
    python3.11 python3-pip libgl1-mesa-dev libosmesa6-dev \
    libglew-dev mesa-utils xvfb git && \
    rm -rf /var/lib/apt/lists/*

# Set up work directory
WORKDIR /app
COPY . /app

# Install Python requirements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Force EGL rendering for headless cloud training
ENV MUJOCO_GL=egl
