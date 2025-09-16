#!/bin/bash

# Festa Bot Systemd Service Installer
# Usage: sudo ./install-service.sh [dockerhub-username]

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Default values
DOCKERHUB_USERNAME="1nepunep1"
SERVICE_DIR="/opt/festa-bot"
SERVICE_FILE="festa-bot.service"

echo -e "${GREEN}🚀 Installing Festa Bot Systemd Service${NC}"

# Check if running as root
if [[ $EUID -ne 0 ]]; then
   echo -e "${RED}❌ This script must be run as root (use sudo)${NC}"
   exit 1
fi

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo -e "${RED}❌ Docker is not installed. Please install Docker first.${NC}"
    exit 1
fi

# Create service directory
echo -e "${YELLOW}📁 Creating service directory: ${SERVICE_DIR}${NC}"
mkdir -p ${SERVICE_DIR}

# Copy service file and update Docker Hub username
echo -e "${YELLOW}📝 Configuring service file${NC}"
sed "s/yourusername/${DOCKERHUB_USERNAME}/g" ${SERVICE_FILE} > ${SERVICE_DIR}/${SERVICE_FILE}

# Create .env file if it doesn't exist
if [ ! -f "${SERVICE_DIR}/.env" ]; then
    echo -e "${YELLOW}📝 Creating .env file template${NC}"
    cat > ${SERVICE_DIR}/.env << 'EOF'
# Telegram Bot Configuration
TOKEN=your_telegram_bot_token_here

# MySQL Database Configuration (for external MySQL)
DB_HOST=localhost
DB_USER=root
DB_PWD=your_db_password
DB=festa_bot_db
EOF
    echo -e "${YELLOW}⚠️  Please edit ${SERVICE_DIR}/.env with your actual values${NC}"
fi

# Copy systemd service file
echo -e "${YELLOW}📋 Installing systemd service${NC}"
cp ${SERVICE_DIR}/${SERVICE_FILE} /etc/systemd/system/

# Set proper permissions
chmod 644 /etc/systemd/system/${SERVICE_FILE}
chown root:root /etc/systemd/system/${SERVICE_FILE}

# Reload systemd
echo -e "${YELLOW}🔄 Reloading systemd daemon${NC}"
systemctl daemon-reload

# Enable service
echo -e "${YELLOW}✅ Enabling service${NC}"
systemctl enable ${SERVICE_FILE}

echo -e "${GREEN}🎉 Installation complete!${NC}"
echo ""
echo -e "${YELLOW}Next steps:${NC}"
echo "1. Edit ${SERVICE_DIR}/.env with your actual values:"
echo "   - Get bot token from @BotFather"
echo "   - Set up MySQL database"
echo ""
echo "2. Start the service:"
echo "   sudo systemctl start festa-bot"
echo ""
echo "3. Check status:"
echo "   sudo systemctl status festa-bot"
echo ""
echo "4. View logs:"
echo "   sudo journalctl -u festa-bot -f"
echo ""
echo -e "${GREEN}Service will auto-start on boot!${NC}"
