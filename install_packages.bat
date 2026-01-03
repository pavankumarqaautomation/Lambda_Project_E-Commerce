@echo off

echo ================================
echo Creating virtual environment
echo ================================
"C:\Soft\python.exe" -m venv venv

echo ================================
echo Activating virtual environment
echo ================================
call venv\Scripts\activate

echo ================================
echo Installing dependencies
echo ================================
echo Upgrading PiP Package
python -m pip install --upgrade pip
echo ==================================
echo installing all the required packages
echo====================================

pip install allure-pytest==2.15.0
pip install allure-python-commons==2.15.0
pip install atomicwrites==1.4.1
pip install attrs==25.4.0
pip install certifi==2025.10.5
pip install cffi==2.0.0
pip install charset-normalizer==3.4.2
pip install colorama==0.4.6
pip install et_xmlfile==2.0.0
pip install execnet==2.1.1
pip install h11==0.16.0
pip install idna==3.10
pip install iniconfig==2.3.0
pip install Jinja2==3.1.6
pip install MarkupSafe==3.0.3
pip install more-itertools==10.8.0
pip install openpyxl==3.1.5
pip install outcome==1.3.0.post0
pip install packaging==25.0
pip install pip-review==1.3.0
pip install pluggy==1.6.0
pip install py==1.11.0
pip install pycparser==2.23
pip install Pygments==2.19.2
pip install PySocks==1.7.1
pip install pytest==7.4.4
pip install pytest-forked==1.6.0
pip install pytest-html==3.2.0
pip install pytest-metadata==2.0.4
pip install pytest-xdist==1.34.0
pip install python-dotenv==1.1.1
pip install requests==2.32.3
pip install selenium==4.37.0
pip install six==1.17.0
pip install sniffio==1.3.1
pip install sortedcontainers==2.4.0
pip install trio==0.31.0
pip install trio-websocket==0.12.2
pip install typing_extensions==4.15.0
pip install urllib3==2.5.0
pip install wcwidth==0.2.14
pip install webdriver-manager==4.0.2
pip install websocket-client==1.9.0
pip install wsproto==1.2.0

echo ================================
echo Dependencies installed
echo ================================


