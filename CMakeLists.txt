# ===========================================================
# CONFIGURACIÓN CUDA
# ===========================================================

enable_language(CUDA)
cmake_policy(SET CMP0104 NEW)
set(CMAKE_CUDA_ARCHITECTURES 86)

# ===========================================================
# CMFO CUDA LIB
# ===========================================================
add_library(cmfo_cuda STATIC
    cuda/cmfo_kernels.cu
)

set_target_properties(cmfo_cuda PROPERTIES
    CUDA_SEPARABLE_COMPILATION ON
    CUDA_RESOLVE_DEVICE_SYMBOLS ON
)

# ===========================================================
# TEST CUDA
# ===========================================================
add_executable(test_cuda tests/test_cuda.cu)

target_link_libraries(test_cuda
    PRIVATE
        cmfo_cuda
        cmfo_core
        cudart
)

set_target_properties(test_cuda PROPERTIES
    CUDA_SEPARABLE_COMPILATION ON
    CUDA_RESOLVE_DEVICE_SYMBOLS ON
)


