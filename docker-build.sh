#!/bin/bash

# Docker build and push script for Festa Bot
# Usage: ./docker-build.sh [version] [registry]

set -e

# Default values
VERSION=${1:-latest}
REGISTRY=${2:-docker.io}
IMAGE_NAME="festa-bot"
FULL_IMAGE_NAME="${REGISTRY}/${IMAGE_NAME}:${VERSION}"

echo "🚀 Building Docker image: ${FULL_IMAGE_NAME}"

# Build the Docker image
docker build -t "${FULL_IMAGE_NAME}" .

echo "✅ Docker image built successfully!"

# Ask if user wants to push
read -p "Do you want to push the image to registry? (y/N): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "📤 Pushing image to registry..."
    docker push "${FULL_IMAGE_NAME}"
    echo "✅ Image pushed successfully!"
    echo "🎉 Your image is available at: ${FULL_IMAGE_NAME}"
else
    echo "ℹ️  Image built locally. To push later, run:"
    echo "   docker push ${FULL_IMAGE_NAME}"
fi

echo ""
echo "🐳 To run the container:"
echo "   docker run -d --name festa-bot --env-file .env ${FULL_IMAGE_NAME}"
echo ""
echo "🔧 To run with custom env:"
echo "   docker run -d --name festa-bot -e TOKEN=your_token -e DB_HOST=localhost ${FULL_IMAGE_NAME}"
