
# Top-level CMake for CMFO-UNIVERSE

cmake_minimum_required(VERSION 3.18)
project(cmfo_universe LANGUAGES C)

# Source layout
set(CMFO_INCLUDE_DIR "${CMAKE_SOURCE_DIR}/include")
set(CMFO_SRC_DIR "${CMAKE_SOURCE_DIR}/src")

file(GLOB CMFO_SOURCES
    "${CMFO_SRC_DIR}/cmfo_core.c"
    "${CMFO_SRC_DIR}/cmfo_mat7.c"
    "${CMFO_SRC_DIR}/cmfo_mat7_mul.c"
    "${CMFO_SRC_DIR}/cmfo_mat7_det.c"
    "${CMFO_SRC_DIR}/cmfo_mat7_inv.c"
    "${CMFO_SRC_DIR}/cmfo_tensor7.c"
    "${CMFO_SRC_DIR}/cmfo_soliton.c"
)

# Library target (core C implementation)
option(BUILD_SHARED "Build shared library for bindings" OFF)
add_library(cmfo_core STATIC ${CMFO_SOURCES})
if(BUILD_SHARED)
  add_library(cmfo_core_shared SHARED ${CMFO_SOURCES})
  target_include_directories(cmfo_core_shared PUBLIC ${CMFO_INCLUDE_DIR})
  set_target_properties(cmfo_core_shared PROPERTIES OUTPUT_NAME "cmfo_core")
  if(MSVC)
    target_compile_definitions(cmfo_core_shared PRIVATE CMFO_CORE_EXPORTS)
  endif()
endif()
target_include_directories(cmfo_core PUBLIC ${CMFO_INCLUDE_DIR})
target_compile_features(cmfo_core PUBLIC c_std_99)

# Optionally configure CUDA pieces if explicitly enabled and sources present
option(ENABLE_CUDA "Enable CUDA targets (requires CUDA toolkit installed)" OFF)
if(ENABLE_CUDA AND EXISTS "${CMAKE_SOURCE_DIR}/cuda")
  # Only enable CUDA language if nvcc is available on the system.
  find_program(NVCC_EXECUTABLE nvcc)
  if(NVCC_EXECUTABLE)
    enable_language(CUDA)
    cmake_policy(SET CMP0104 NEW)
    # Default to a reasonable architecture if not set by user
    if(NOT DEFINED CMAKE_CUDA_ARCHITECTURES)
      set(CMAKE_CUDA_ARCHITECTURES 86)
    endif()

    file(GLOB CUDA_SOURCES "${CMAKE_SOURCE_DIR}/cuda/*.cu")
    if(CUDA_SOURCES)
      add_library(cmfo_cuda STATIC ${CUDA_SOURCES})
      target_include_directories(cmfo_cuda PUBLIC ${CMFO_INCLUDE_DIR})
      set_target_properties(cmfo_cuda PROPERTIES
        CUDA_SEPARABLE_COMPILATION ON
        CUDA_RESOLVE_DEVICE_SYMBOLS ON
      )
      target_link_libraries(cmfo_cuda PUBLIC cmfo_core)

      # Add CUDA test executable if test exists
      if(EXISTS "${CMAKE_SOURCE_DIR}/tests/test_cuda.cu")
        add_executable(test_cuda tests/test_cuda.cu)
        set_target_properties(test_cuda PROPERTIES
          CUDA_SEPARABLE_COMPILATION ON
          CUDA_RESOLVE_DEVICE_SYMBOLS ON
        )
        target_link_libraries(test_cuda PRIVATE cmfo_cuda cmfo_core cudart)
      endif()
    endif()
  else()
    message(WARNING "CUDA folder found but 'nvcc' not in PATH. Skipping CUDA targets.")
    enable_language(C) # Fallback? No need, already enabled
  endif()
elseif(EXISTS "${CMAKE_SOURCE_DIR}/cuda")
  message(WARNING "CUDA sources present but ENABLE_CUDA is OFF. Pass -DENABLE_CUDA=ON to enable CUDA build.")
endif()

# Enable tests and add tests folder
enable_testing()
add_subdirectory(tests)
