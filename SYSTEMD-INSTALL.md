# 🚀 Festa Bot Systemd Service Installation

## Quick Install

```bash
# 1. Clone/download the project
git clone <your-repo-url>
cd festa_bot

# 2. Install the service (replace 'yourusername' with your Docker Hub username)
sudo ./install-service.sh yourusername

# 3. Configure environment
sudo nano /opt/festa-bot/.env

# 4. Start the service
sudo systemctl start festa-bot
```

## Manual Installation

### 1. Prepare the server

```bash
# Install Docker
sudo apt update
sudo apt install docker.io -y
sudo systemctl enable docker
sudo systemctl start docker

# Add user to docker group
sudo usermod -aG docker $USER
newgrp docker
```

### 2. Create service directory

```bash
sudo mkdir -p /opt/festa-bot
cd /opt/festa-bot
```

### 3. Create .env file

```bash
sudo nano .env
```

Add your configuration:
```env
# Telegram Bot Configuration
TOKEN=your_real_bot_token_from_botfather

# MySQL Database Configuration
DB_HOST=your_mysql_host
DB_USER=your_db_user
DB_PWD=your_db_password
DB=festa_bot_db
```

### 4. Install systemd service

```bash
# Copy service file
sudo cp festa-bot.service /etc/systemd/system/

# Update Docker Hub username in service file
sudo sed -i 's/yourusername/yourdockerhubusername/g' /etc/systemd/system/festa-bot.service

# Reload systemd
sudo systemctl daemon-reload

# Enable service
sudo systemctl enable festa-bot
```

### 5. Start the service

```bash
sudo systemctl start festa-bot
```

## Service Management

```bash
# Check status
sudo systemctl status festa-bot

# Start service
sudo systemctl start festa-bot

# Stop service
sudo systemctl stop festa-bot

# Restart service
sudo systemctl restart festa-bot

# View logs
sudo journalctl -u festa-bot -f

# View recent logs
sudo journalctl -u festa-bot --since "1 hour ago"
```

## Docker Hub Setup

### 1. Build and push image

```bash
# Build image
docker build -t yourusername/festa-bot:latest .

# Push to Docker Hub
docker push yourusername/festa-bot:latest
```

### 2. Update service file

Replace `yourusername` in the service file with your actual Docker Hub username.

## Troubleshooting

### Service won't start

```bash
# Check service status
sudo systemctl status festa-bot

# Check logs
sudo journalctl -u festa-bot -n 50

# Check Docker
sudo docker ps -a
sudo docker logs festa-bot
```

### Container issues

```bash
# Check if image exists
sudo docker images | grep festa-bot

# Pull latest image
sudo docker pull yourusername/festa-bot:latest

# Test run manually
sudo docker run --rm --env-file /opt/festa-bot/.env yourusername/festa-bot:latest
```

### Environment issues

```bash
# Check .env file
sudo cat /opt/festa-bot/.env

# Test environment variables
sudo docker run --rm --env-file /opt/festa-bot/.env yourusername/festa-bot:latest env
```

## Security Notes

- The service runs as root (required for Docker)
- Uses `--network host` for simplicity
- Environment file is protected by systemd
- Container has security restrictions enabled

## Auto-updates

The service automatically pulls the latest image on each start. To update:

```bash
sudo systemctl restart festa-bot
```

This will pull the latest version from Docker Hub and restart the service.
