@echo off
echo Installing dependencies...
pip install flask requests

echo Starting Flask app...
python app.py
pause