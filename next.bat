cd pip-1.2.1
python setup.py>null 2>&1
if errorlevel 0 goto install_pip_ok
if errorlevel 9009 goto install_pip_fail
:install_pip_fail
echo  ��װpipʧ�ܣ���ȷ��python-3.6.2.exe��ItChat-master��pip-1.2.1��next.bat��װ�������ͬһĿ¼�£�
exit 0
:install_pip_ok
echo  pip �ɹ���װ!
echo  ��ȷ�����ļ�������Է�������
pause
pip install itchat>null 2>&1
if errorlevel 0 goto install_itchat_ok
if errorlevel 9009 goto install_itchat_fail
:install_itchat_fail
echo  ��װitchatʧ�ܣ���ȷ�����ļ�������Է�������
exit 0
:install_itchat_ok
echo  ��װitchat�ɹ������ڿ���ֱ������΢�Ż������ˣ�
pause
python ΢�Ż�����.py
exit 0