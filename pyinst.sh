#!/bin/sh

PYINSTALLER="pyinstaller --onefile -y --distpath . --workpath build --name"
$PYINSTALLER gui_ccard gui.py
$PYINSTALLER ccard ccardprefix.py