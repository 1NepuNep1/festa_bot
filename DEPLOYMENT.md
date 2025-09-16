# 🚀 Festa Bot Deployment Guide

## Quick Start with Docker

### 1. Build and Push Docker Image

```bash
# Build with default settings (latest tag)
./docker-build.sh

# Build with custom version
./docker-build.sh v1.0.0

# Build and push to custom registry
./docker-build.sh v1.0.0 your-registry.com
```

### 2. Run with Docker Compose (Recommended)

```bash
# 1. Configure your .env file
cp .env.example .env
# Edit .env with your actual values

# 2. Start the services
docker-compose up -d

# 3. Check logs
docker-compose logs -f festa-bot
```

### 3. Run with Docker Run

```bash
# Simple run
docker run -d --name festa-bot --env-file .env festa-bot:latest

# With custom environment variables
docker run -d --name festa-bot \
  -e TOKEN=your_bot_token \
  -e DB_HOST=your_db_host \
  -e DB_USER=your_db_user \
  -e DB_PWD=your_db_password \
  -e DB=your_db_name \
  festa-bot:latest
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `TOKEN` | Telegram Bot Token (required) | - |
| `DB_HOST` | MySQL host | localhost |
| `DB_USER` | MySQL username | root |
| `DB_PWD` | MySQL password | password |
| `DB` | Database name | festa_bot_db |

## Production Deployment

### Using Docker Hub

```bash
# Build and tag for Docker Hub
./docker-build.sh v1.0.0 docker.io/yourusername

# Pull and run on production server
docker pull yourusername/festa-bot:v1.0.0
docker run -d --name festa-bot --env-file .env yourusername/festa-bot:v1.0.0
```

### Using Private Registry

```bash
# Build and push to private registry
./docker-build.sh v1.0.0 your-registry.com/namespace

# Deploy to production
docker pull your-registry.com/namespace/festa-bot:v1.0.0
docker run -d --name festa-bot --env-file .env your-registry.com/namespace/festa-bot:v1.0.0
```

## Health Check

```bash
# Check if bot is running
docker ps | grep festa-bot

# Check logs
docker logs festa-bot

# Restart if needed
docker restart festa-bot
```

## Database Setup

The bot will automatically create the required database tables on first run. Make sure your MySQL server is accessible and the database exists.

## Troubleshooting

1. **Bot not responding**: Check TOKEN in .env file
2. **Database connection failed**: Verify DB_* variables in .env
3. **Container won't start**: Check logs with `docker logs festa-bot`
