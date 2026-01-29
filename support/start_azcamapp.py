"""
azcamapp example start file
"""

import subprocess

OPTIONS = "-system test"
CMD = f"python -i -m azcam_app -- {OPTIONS}"

p = subprocess.Popen(
    CMD,
    creationflags=subprocess.CREATE_NEW_CONSOLE,
)
