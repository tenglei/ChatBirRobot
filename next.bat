cd pip-1.2.1
python setup.py>null 2>&1
if errorlevel 0 goto install_pip_ok
if errorlevel 9009 goto install_pip_fail
:install_pip_fail
echo  安装pip失败，请确保python-3.6.2.exe、ItChat-master、pip-1.2.1和next.bat安装程序放在同一目录下！
exit 0
:install_pip_ok
echo  pip 成功安装!
echo  请确保您的计算机可以访问外网
pause
pip install itchat>null 2>&1
if errorlevel 0 goto install_itchat_ok
if errorlevel 9009 goto install_itchat_fail
:install_itchat_fail
echo  安装itchat失败，请确保您的计算机可以访问外网
exit 0
:install_itchat_ok
echo  安装itchat成功，现在可以直接运行微信机器人了！
pause
python 微信机器人.py
exit 0