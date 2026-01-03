@echo off

set PATH=%CD%\venv\Scripts;%PATH%
echo Activating virtual environment
call venv\Scripts\activate


pytest
