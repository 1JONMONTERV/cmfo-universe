# CMFO-UNIVERSE: Installation Guide

This guide provides detailed installation instructions for CMFO-UNIVERSE across different platforms.

## Table of Contents

- [System Requirements](#system-requirements)
- [Installation Methods](#installation-methods)
- [Platform-Specific Instructions](#platform-specific-instructions)
- [Verification](#verification)
- [Troubleshooting](#troubleshooting)

## System Requirements

### Supported Operating Systems

| OS | Versions | Status |
|----|----------|--------|
| **Linux** | Ubuntu 20.04+, Debian 11+, RHEL 8+, Fedora 35+ | ✅ Fully Supported |
| **Windows** | Windows 10/11 (x64) | ✅ Fully Supported |
| **macOS** | macOS 11+ (Big Sur and later) | ✅ Fully Supported |

### Supported Python Versions

- Python 3.8
- Python 3.9
- Python 3.10
- Python 3.11
- Python 3.12

### Required Compilers

| Platform | Compiler | Minimum Version |
|----------|----------|-----------------|
| Linux | GCC | 9.0+ |
| Linux | Clang | 10.0+ |
| Windows | MSVC | 2019+ (v142) |
| Windows | MinGW-w64 | 8.0+ |
| macOS | Clang (Xcode) | 12.0+ |

### Optional: CUDA Support

For GPU acceleration (optional):
- **CUDA Toolkit**: 11.8+ or 12.x
- **GPU**: NVIDIA with Compute Capability SM86 (RTX 30/40 series)
- **Driver**: NVIDIA driver 520+ (Linux), 527+ (Windows)

## Installation Methods

### Method 1: Install from PyPI (Recommended)

```bash
pip install cmfo-universe
```

### Method 2: Install from GitHub Releases

1. Download the appropriate wheel for your platform from [GitHub Releases](https://github.com/1JONMONTERV/cmfo-universe/releases)
2. Install the wheel:
   ```bash
   pip install cmfo_universe-1.0.0-*.whl
   ```

### Method 3: Build from Source

See [Platform-Specific Instructions](#platform-specific-instructions) below.

## Platform-Specific Instructions

### Linux (Ubuntu/Debian)

#### Prerequisites

```bash
sudo apt-get update
sudo apt-get install -y build-essential cmake ninja-build python3-dev
```

#### Build and Install

```bash
# Clone repository
git clone https://github.com/1JONMONTERV/cmfo-universe.git
cd cmfo-universe

# Build C core library
mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED=ON
cmake --build . -j$(nproc)
cd ..

# Install Python package
cd python
pip install -e .
```

#### Optional: Enable CUDA

```bash
# Install CUDA Toolkit (if not already installed)
# Follow: https://developer.nvidia.com/cuda-downloads

# Build with CUDA enabled
mkdir build-cuda && cd build-cuda
cmake .. -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED=ON -DENABLE_CUDA=ON
cmake --build . -j$(nproc)
```

### Windows

#### Prerequisites

1. Install [Visual Studio 2019+](https://visualstudio.microsoft.com/) with C++ development tools
2. Install [CMake](https://cmake.org/download/) (3.18+)
3. Install [Python 3.8+](https://www.python.org/downloads/)

#### Build and Install (PowerShell)

```powershell
# Clone repository
git clone https://github.com/1JONMONTERV/cmfo-universe.git
cd cmfo-universe

# Build C core library
mkdir build
cd build
cmake .. -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED=ON
cmake --build . --config Release
cd ..

# Install Python package
cd python
pip install -e .
```

#### Alternative: MinGW-w64

```bash
# Using MinGW-w64
mkdir build && cd build
cmake .. -G "MinGW Makefiles" -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED=ON
cmake --build .
```

### macOS

#### Prerequisites

```bash
# Install Xcode Command Line Tools
xcode-select --install

# Install Homebrew (if not already installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install CMake
brew install cmake ninja
```

#### Build and Install

```bash
# Clone repository
git clone https://github.com/1JONMONTERV/cmfo-universe.git
cd cmfo-universe

# Build C core library
mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED=ON
cmake --build . -j$(sysctl -n hw.ncpu)
cd ..

# Install Python package
cd python
pip install -e .
```

#### Apple Silicon (M1/M2/M3)

The build system automatically detects Apple Silicon and configures appropriately. No special flags needed.

## Verification

After installation, verify the installation:

### Python Package

```python
python -c "from cmfo import CMFOCore; print('CMFO-UNIVERSE installed successfully!')"
```

### Run Tests

```bash
# C/C++ tests
cd build
ctest --output-on-failure

# Python tests
cd python
pytest -v
```

### Run Examples

```bash
# Basic tensor operation
python examples/basic_tensor.py

# Matrix operations
python examples/matrix_operations.py

# Phi-logic demonstration
python examples/phi_logic_demo.py
```

## Troubleshooting

### Issue: `cmfo_core.h` not found

**Solution**: Ensure you've built the C core library first:
```bash
mkdir build && cd build
cmake .. -DBUILD_SHARED=ON
cmake --build .
```

### Issue: Python import error `ImportError: No module named 'cmfo'`

**Solution**: Install the Python package in development mode:
```bash
cd python
pip install -e .
```

### Issue: CUDA compilation fails

**Possible causes:**
1. CUDA Toolkit not installed or not in PATH
2. Incompatible GPU architecture

**Solution**:
```bash
# Check CUDA installation
nvcc --version

# Specify architecture explicitly
cmake .. -DENABLE_CUDA=ON -DCMAKE_CUDA_ARCHITECTURES=86
```

### Issue: Windows DLL not found

**Solution**: Ensure the build directory is in your PATH or copy `cmfo_core.dll` to the Python package directory:
```powershell
copy build\Release\cmfo_core.dll python\cmfo\
```

### Issue: macOS library not loaded

**Solution**: Set `DYLD_LIBRARY_PATH`:
```bash
export DYLD_LIBRARY_PATH=$PWD/build:$DYLD_LIBRARY_PATH
```

### Issue: Permission denied during installation

**Solution**: Use `--user` flag or virtual environment:
```bash
pip install --user -e python/
# OR
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate  # Windows
pip install -e python/
```

## Getting Help

If you encounter issues not covered here:

1. Check [GitHub Issues](https://github.com/1JONMONTERV/cmfo-universe/issues)
2. Review [Documentation](https://github.com/1JONMONTERV/cmfo-universe/tree/main/Docs)
3. Contact: jmvlavacar@hotmail.com

---

**Last Updated**: 2025-12-12  
**Version**: 1.0.0
