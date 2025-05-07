FROM python:3.11-slim

WORKDIR /app

COPY server.py ./
COPY README.md ./

# Install FastMCP CLI and dependencies
RUN pip install --no-cache-dir "mcp[cli]"
RUN pip install --no-cache-dir "fastmcp"

# Expose internal port (8000 inside docker)
# I just chose 8000 and 8000 because they're often used by Python servers
EXPOSE 8000

# Use fastmcp CLI to run the server on 0.0.0.0:8000
# IT DEFAULTS TO 8000
CMD ["fastmcp", "run", "server.py:mcp", "--transport", "sse"]

# Build & Run the Docker image
# docker build -t mcp . && docker run -d -p 8000:8000 mcp

