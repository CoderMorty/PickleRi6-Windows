@echo off
pip install -r requirements.txt
python3 -m pip install -U https://github.com/rapptz/discord.py/archive/async.zip#egg=discord.py[voice]
echo If this didn't work, create an issue at: github.com/bourbbbon/pickleri6
pause