set "PATH=%PATH%;%CUDA_HOME%\\bin%"

%PYTHON% configure.py --enable-shared
if errorlevel 1 exit 1

%PYTHON% -m pip install . -vv
if errorlevel 1 exit 1
