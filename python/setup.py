from setuptools import setup, Extension

module = Extension('cmfo_core',
                   sources=['python/cmfo_py.c',
                            'src/cmfo_core.c',
                            'src/cmfo_mat7.c',
                            'src/cmfo_mat7_mul.c',
                            'src/cmfo_mat7_det.c',
                            'src/cmfo_mat7_inv.c',
                            'src/cmfo_tensor7.c'],
                   include_dirs=['include'])

setup(name='cmfo_core',
      version='1.0',
      description='CMFO core python bindings',
      ext_modules=[module])
