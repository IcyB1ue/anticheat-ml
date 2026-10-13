import os
import platform
import sys
from datetime import datetime

import numpy

print("=== System report ===")
print(f"OS:      {platform.system()} {platform.release()}")
print(f"CPU:     {platform.machine()}, {os.cpu_count()} logical CPUs")
print(f"Python:  {platform.python_version()}")
print(f"Program: {sys.executable}")
print(f"NumPy:   {numpy.__version__}")
print(f"Time:    {datetime.now():%Y-%m-%d %H:%M}")