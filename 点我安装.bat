ECHO OFF
echo  ׼����װpython������ 
echo  ����ѡ��������� Add Python 3.6 to PATH ���ٵ�� "Install Now "
python-3.6.2
if errorlevel 0 goto install_python_ok
if errorlevel 1602 goto install_python_fail
:install_python_fail
echo  ��װpythonʧ��
exit 0
:install_python_ok
echo  python �ɹ���װ!
echo  ׼����װpip������
call next