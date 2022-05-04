import os
import sys

import pycuda


# Ensure PyCUDA picks up the correct CUDA_VERSION
try:
    from pycuda import driver
    ver = driver.get_version()[:2]
    cuda_ver = tuple(map(int, os.environ.get("cuda_compiler_version").split(".")))
    if ver != cuda_ver:
        raise ValueError(
            "CUDA version {0} != cuda_compiler_version {1}".format(ver, cuda_ver)
        )
except Exception as e:
    if os.name == 'nt':
        print("No nvcuda.dll available on windows. Exiting without checking for driver version.")
    else:
        raise

# Check PyCUDA can access a GPU for testing
# If not, exit cleanly (may be on CPU only CI)
try:
    import pycuda.autoinit
except Exception as e:
    print("Got an error: \n%s" % str(e))
    print("No GPU available. Exiting without running PyCUDA's tests.")
    sys.exit(0)

# Run PyCUDA's test suite
import py
py.test.cmdline.main(["test"])
