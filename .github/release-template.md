# Release Template for CMFO-UNIVERSE

## What's New in v{VERSION}

{Brief description of the release}

### ✨ New Features

- {Feature 1}
- {Feature 2}

### 🔧 Improvements

- {Improvement 1}
- {Improvement 2}

### 🐛 Bug Fixes

- {Fix 1}
- {Fix 2}

### ⚠️ Breaking Changes

{List any breaking changes, or remove this section if none}

---

## Installation

### From PyPI

```bash
pip install cmfo-universe=={VERSION}
```

### From GitHub Release

Download the appropriate wheel for your platform:

- **Linux (x86_64)**: `cmfo_universe-{VERSION}-cp3{X}-cp3{X}-manylinux_2_17_x86_64.whl`
- **Windows (x64)**: `cmfo_universe-{VERSION}-cp3{X}-cp3{X}-win_amd64.whl`
- **macOS (Intel)**: `cmfo_universe-{VERSION}-cp3{X}-cp3{X}-macosx_10_9_x86_64.whl`
- **macOS (Apple Silicon)**: `cmfo_universe-{VERSION}-cp3{X}-cp3{X}-macosx_11_0_arm64.whl`

Then install:
```bash
pip install cmfo_universe-{VERSION}-*.whl
```

### Verification

Verify the installation:
```python
python -c "from cmfo import CMFOCore; print('CMFO-UNIVERSE v{VERSION} installed successfully!')"
```

---

## Security & Integrity

### Checksums

All release artifacts include SHA256 checksums in `SHA256SUMS.txt`. Verify integrity:

```bash
# Linux/macOS
sha256sum -c SHA256SUMS.txt

# Windows (PowerShell)
Get-FileHash cmfo_universe-{VERSION}-*.whl -Algorithm SHA256
```

### Software Bill of Materials (SBOM)

This release includes a complete SBOM (`sbom.json`) in CycloneDX format, listing all dependencies and components for supply chain security.

---

## Documentation

- **Installation Guide**: [Docs/INSTALLATION.md](https://github.com/1JONMONTERV/cmfo-universe/blob/main/Docs/INSTALLATION.md)
- **Numerical Tolerances**: [Docs/NUMERICAL_TOLERANCES.md](https://github.com/1JONMONTERV/cmfo-universe/blob/main/Docs/NUMERICAL_TOLERANCES.md)
- **Examples**: [examples/](https://github.com/1JONMONTERV/cmfo-universe/tree/main/examples)
- **Full Changelog**: [CHANGELOG.md](https://github.com/1JONMONTERV/cmfo-universe/blob/main/CHANGELOG.md)

---

## Supported Platforms

| Platform | Python Versions | Architecture |
|----------|----------------|--------------|
| Linux | 3.8, 3.9, 3.10, 3.11, 3.12 | x86_64 |
| Windows | 3.8, 3.9, 3.10, 3.11, 3.12 | x64 |
| macOS | 3.8, 3.9, 3.10, 3.11, 3.12 | x86_64, ARM64 |

---

## Getting Help

- **Issues**: [GitHub Issues](https://github.com/1JONMONTERV/cmfo-universe/issues)
- **Discussions**: [GitHub Discussions](https://github.com/1JONMONTERV/cmfo-universe/discussions)
- **Email**: jmvlavacar@hotmail.com

---

## License

CMFO-UNIVERSE v1.1 – Commercial Restricted License  
Copyright © 2025 Jonnathan Montero Víquez

See [LICENSE](https://github.com/1JONMONTERV/cmfo-universe/blob/main/LICENSE) for details.
