@echo off

set HTTP_PROXY=http://192.168.8.3:3128
set HTTPS_PROXY=http://192.168.8.3:3128
set NO_PROXY=localhost,127.0.0.1,192.168.1.0/24,192.168.2.0/24,192.168.7.0/24

set PYTHON=C:\_Dev\Repository\Python\Python-3.10.11\python.exe
SET PATH=%PATH%;C:\UserData\Appz\VS2022\BuildTools\VC\Tools\MSVC\14.33.31629\bin\Hostx64\x64

call .\venv\Scripts\activate.bat

REM pip install -r requirements_m.txt
cmd /k
REM python.exe -m pip install --upgrade pip
REM pip3 install -r requirements.txt
REM pip install xformers~=0.0.22
