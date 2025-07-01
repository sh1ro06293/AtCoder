# Use the official Python image as the base image
FROM python:3.10-slim

# Set up a workspace directory
WORKDIR /workspace

# Install necessary tools
RUN apt-get update && apt-get install -y \
    bash \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --upgrade pip

# Set the default user to vscode
ARG USERNAME=vscode
RUN useradd -m $USERNAME && \
    chown -R $USERNAME:$USERNAME /workspace

USER $USERNAME

# Set the default command to bash
CMD ["bash"]
