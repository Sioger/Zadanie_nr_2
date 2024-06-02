FROM busybox:1.35

# Create a non-root user to own the httpd server files
RUN adduser -D static
USER static
WORKDIR /home/static

# Copy the page source to declared workdir
COPY src .

# Run BusyBox httpd server
CMD ["busybox", "httpd", "-f", "-v", "-p", "3000"]
