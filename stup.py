from distutils.core import setup  
  
import py2exe  
  
  
  
includes = ["encodings", "encodings.*"]  
  
options = {"py2exe":  
  
            {   "compressed": 1,  
  
                "optimize": 2,  
  
                "includes": includes,  
  
                "bundle_files": 1  
  
            }  
  
          }  
  
setup(     
  
    version = "3.0.0",  
  
    description = "Data Convert Tools(For MM-Bukepa.org only)",  
  
    name = "Data Convert Tools",  
  
    options = options,  
  
    zipfile=None,  
  
    console = ["dou2_win.py"], 
    )