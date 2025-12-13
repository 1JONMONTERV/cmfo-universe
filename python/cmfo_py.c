#include <Python.h>
#include "cmfo_core.h"

static PyObject* py_cmfo_phi(PyObject* self, PyObject* args) {
    double v = cmfo_phi();
    return PyFloat_FromDouble(v);
}

static PyObject* py_cmfo_tau(PyObject* self, PyObject* args) {
    double v = cmfo_tau();
    return PyFloat_FromDouble(v);
}

static PyMethodDef CmfoMethods[] = {
    {"phi", py_cmfo_phi, METH_NOARGS, "Return CMFO phi"},
    {"tau", py_cmfo_tau, METH_NOARGS, "Return CMFO tau"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef cmfomodule = {
    PyModuleDef_HEAD_INIT,
    "cmfo_core",
    "Python bindings for cmfo_core",
    -1,
    CmfoMethods
};

PyMODINIT_FUNC PyInit_cmfo_core(void) {
    return PyModule_Create(&cmfomodule);
}
