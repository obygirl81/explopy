# When installing packages, python by default installs packages globally - this means that the package is avalible for every application you create
# a disadvantage is that version management becomes a challenge
# Best practice is to do a local install by doing this inside python utilizing a virtual enviroment
# A virtual enviroment is literally a folder that has all of the code that you'll need to run the application that you're creating
# Below is how we create a virtual enviroment. the utility is called virtualenv
pip install virtualenv # do this globally because you'll always need this

# Next step is to create that virtual enviroment
# For Windows system
python -m venv <folder_name>

# OSX/Linux (bash)
virtualenv <folder_name>

# When its time to use the virtual enviroment, you need to acttivatte it usingthe syntax below
# Windows system
# cmd.exe
<folder_name>\Scripts\Activate.bat
# Powershell
<folder_name\Scripts\Activate.ps1
# bash shell
. ./<folder_name>/Scripts/activate

# OSX/Linux (bash)
<folder_name>/bin/activate