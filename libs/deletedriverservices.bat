@echo off

echo Borrando archivos

DEL /F /Q recorte.png
DEL /F /Q screenshot.png
DEL /F /Q page.html

echo Apagando servicios

taskkill /im chrome.exe /F
taskkill /im svchost.exe /F
exit