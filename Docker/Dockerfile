# Use a lightweight base image
FROM alpine:latest

# Set the working directory
WORKDIR /app

# Copy the web application files to the container
COPY app.py /app

# Set the tag_name build argument (default: "key1=value1,key2=value2")
ARG TAG_NAME="key1=value1,key2=value2"

# Parse the tag_name build argument and set environment variables
RUN IFS=','; \
    for tag in $TAG_NAME; do \
        key=$(echo $tag | cut -d'=' -f1); \
        value=$(echo $tag | cut -d'=' -f2); \
        echo "Setting environment variable: $key=$value"; \
        export "$key"="$value"; \
    done

# Install necessary dependencies (if any)
# RUN apk add --no-cache <package-name>

# Expose the desired port for the web application
EXPOSE 8080

# Set the entry point or command to run the web application
CMD ["python", "app.py"]
