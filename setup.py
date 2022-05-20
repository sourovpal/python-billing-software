import cx_Freeze 
import sys 
import os 

base = None 

if sys.platform == "win32": 
    base = "win32GUI" 

os.environ['TCL_LIBRAW'] = r"C:\Users\SOUROV\AppData\Local\Programs\Python\Python37\tcl\tcl8.6"

os.environ['TK_LIBRAW'] = r"C:\Users\SOUROV\AppData\Local\Programs\Python\Python37\tcl\tk8.6" 

executables = [cx_Freeze.Executable("billing.py", base=base, icon="icon.ico")] 
cx_Freeze.setup( 
    name = "Billing Software", 
    options = {"build_exe": {"packages":['tkinter', 'os'], "include_files":["icon.ico","tcl86t.dll", "tk86t.dll"]}},
    version = "0.01",
    description = "tkinter Application",
    executables = executables
    )