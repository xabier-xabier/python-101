# Use the built-in `platform` module to print out the following info:

import platform

placeholder = "remove me :)"

plat_str=platform.platform()
plat_pyc=platform.python_compiler()
plat_pyv=platform.python_version()
plat_sys=platform.system()
plat_re=platform.release()
plat_pro=platform.processor()
 
print(f"{'Platform:':>10} {plat_str}",)  # platform.platform()
print(f"{'Compiler:':>10} {plat_pyc}",)  # platform.python_compiler()
print(f"{'Python:':>10} {plat_pyv}",)  # platform.python_version()
print(f"{'System:':>10} {plat_sys}",)  # platform.system()
print(f"{'Release:':>10} {plat_re}",)  # platform.release()
print(f"{'System:':>10} {plat_pro}",)  # platform.processor()
