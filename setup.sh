#!/bin/bash
echo "[+] Installing Python dependencies..."
pip3 install -r requirements.txt
echo "[+] Setting up hourly cronjob..."
(crontab -l 2>/dev/null; echo "0 * * * * cd $PWD && /usr/bin/python3 scraper.py && /usr/bin/python3 deduplicate.py && /usr/bin/python3 update_website.py") | crontab -
echo "[✓] Setup complete. Automation is live every hour!"
