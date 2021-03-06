"""
This file contains variables that differ from system to system.
"""
print "importing " + __file__

# All users should supply these values
dragonNatSpeakPath = r"C:\Program Files (x86)\Nuance\NaturallySpeaking13\Program\natspeak.exe"
macroHomeFolder = r"C:\NatLink\NatLink\MacroSystem" # deploy.bat deploys to here
pythonPath = r"C:\Python27_6_32bit\python.exe"

# Users that deploy updated rules using deploy.bat should supply these values
computerName = "CHAJADAN-PC" # used in the safeguards of deploy.bat
macroSourceFolder = r"D:\git\DragonflyRules\DragonflyRules\src" # deploy.bat pulls from here

# Report32.py uses these values
aciAwareDllPath = r"D:\git\AciImporter\Release\AciAware.dll"
aciPicPath = r"D:\git\AciCompiler\AciCompiler\AciCompiler\pics"