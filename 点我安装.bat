ECHO OFF
echo  准备安装python。。。 
echo  请先选择最下面的 Add Python 3.6 to PATH 后再点击 "Install Now "
python-3.6.2
if errorlevel 0 goto install_python_ok
if errorlevel 1602 goto install_python_fail
:install_python_fail
echo  安装python失败
exit 0
:install_python_ok
echo  python 成功安装!
echo  准备安装pip。。。
call next