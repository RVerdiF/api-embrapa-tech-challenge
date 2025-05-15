@ECHO OFF
SETLOCAL EnableDelayedExpansion

ECHO Starting Embrapa API application...

REM Check if virtual environment exists
SET ENV_CREATED=0
IF NOT EXIST .env\ (
    ECHO Virtual environment not found. Creating one...
    python -m venv .env
    IF !ERRORLEVEL! NEQ 0 (
        ECHO Failed to create virtual environment. Please check if Python is installed correctly.
        EXIT /B 1
    )
    SET ENV_CREATED=1
)

REM Activate virtual environment
ECHO Activating virtual environment...
CALL .env\Scripts\activate.bat
IF !ERRORLEVEL! NEQ 0 (
    ECHO Failed to activate virtual environment.
    EXIT /B 1
)

REM Install requirements only if virtual environment was just created
IF !ENV_CREATED!==1 (
    ECHO Installing requirements...
    pip install -r requirements.txt
    IF !ERRORLEVEL! NEQ 0 (
        ECHO Failed to install requirements. Please check if requirements.txt exists.
        EXIT /B 1
    )
)

REM Run the application
ECHO Starting the application...
python -m app.main
IF !ERRORLEVEL! NEQ 0 (
    ECHO Application exited with error code !ERRORLEVEL!.
    PAUSE
    EXIT /B !ERRORLEVEL!
)

ECHO Application stopped.
ENDLOCAL
