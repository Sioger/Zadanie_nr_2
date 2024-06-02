# Stage 1: Build stage
FROM python:3.9-slim as build

LABEL maintainer="robert54"

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the server code
COPY server.py .

# Stage 2: Final image
FROM python:3.9-slim

LABEL maintainer="robert54"

WORKDIR /app

# Copy the built files from the previous stage
COPY --from=build /app /app

EXPOSE 8000

CMD ["python", "server.py"]











# FROM busybox:1.35

# # Create a non-root user to own the httpd server files
# RUN adduser -D static
# USER static
# WORKDIR /home/static

# # Copy the page source to declared workdir
# COPY src .

# # Run BusyBox httpd server
# CMD ["busybox", "httpd", "-f", "-v", "-p", "3000"]
