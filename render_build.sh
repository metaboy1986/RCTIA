#!/bin/bash
echo "=== Python Version Check ==="
python --version
which python
#!/usr/bin/env bash

# Display Python version
echo "=== Python Version Check ==="
python --version
which python

# Force install all dependencies INCLUDING gunicorn
pip install --upgrade pip
pip install gunicorn
pip install -r requirements.txt
