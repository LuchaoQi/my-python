@echo off
cd %~dp0
start /min jupyter notebook %1
#start /min jupyter lab %1