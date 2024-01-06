import ctypes
import platform
import os
import sys

import pycuda


# Load `libcuda.so` either from the system or using the stub
try:
    libcuda = ctypes.CDLL("libcuda.so")
except OSError:
    if (sys.platform.startswith("linux") and
        os.environ.get("CONDA_OVERRIDE_CUDA", "").startswith("12")):
        # Load stub library if needed
        PREFIX = os.environ["PREFIX"]
        arch = platform.processor()
        if arch == "aarch64":
            cuda_target_name =  "sbsa-linux"
        else:
            cuda_target_name = f"{arch}-linux"
        libcuda_stub_path = f"{PREFIX}/targets/{cuda_target_name}/lib/stubs/libcuda.so"
        libcuda = ctypes.CDLL(libcuda_stub_path)
    else:
        raise


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
