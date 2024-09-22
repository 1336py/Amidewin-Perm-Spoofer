ECHO OFF
TITLE HWID Checker
ECHO **********************************
Color 0F
ECHO **********************************
:start
cls
wmic diskdrive get model, serialnumber
ECHO CPU 
wmic cpu get serialnumber
ECHO BIOS
wmic bios get serialnumber
ECHO Motherboard
wmic baseboard get serialnumber
ECHO smBIOS UUID
wmic path win32_computersystemproduct get uuid
getmac
echo Press any key to get your hardware serials again.
pause>nul
goto start