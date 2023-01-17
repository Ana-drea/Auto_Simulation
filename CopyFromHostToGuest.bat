@echo off
vmrun -T ws start "D:\W10ENT-CHSx64-VM15\W10ENT-CHSx64-VM15.vmx" gui

vmrun -T ws -gu Administrator -gp "" CopyFileFromHostToGuest "D:\W10ENT-CHSx64-VM15\W10ENT-CHSx64-VM15.vmx" %~1%  %~2%
pause