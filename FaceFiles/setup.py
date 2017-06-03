import sys
from cx_Freeze import setup,Executable

include_files = ['autorun.inf']
base = None

if sys.platform=='win32':
    base = 'win32GUI'
setup(name="connector",version = "1.0",description = "It connects to main server script",
options ={'build_exe':{'include_files':include_files}},executables = [Executable("gui2.py",base = base)])