# Setup development environment
1. Download and install Visual Studio Code for x64 
2. Open Visual Studio Code and click "source control" and following the hints to install git and clone this repository.
3. Click Explorer to add a new .py file and following the hint to install python extention(not sure it is needed). 
4. Read https://code.visualstudio.com/docs/python/python-tutorial, In View->Command Pallete->run "Python: Create Environment" to create a .Venv whose files you can view under explorer. After run "Python: Select Environment" to select the venv, you can run in the Terminal "python -m pip install yahoofinancials".
6. Open src/util.py and Run. There is error message about running Activate.ps1 and prompt you to run  "Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUsery"
7. After run, the script will print information to out.html in current directory. Click the file to view it in browser
8. Run git config --global user.email and git config --global user.name in command window to finish setup git, then you can commit the files. (tip: there is a check mark button for the commit message). Click sync to push the commit to remote.
