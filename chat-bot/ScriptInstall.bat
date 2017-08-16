@echo off
pip3 install -r requirements.txt
python3 -m pip install -U https://github.com/rapptz/discord.py/archive/async.zip#egg=discord.py[voice]
echo If it didn't work, try ScriptInstall2.
pause