import cmfo_core

def test_phi():
    assert abs(cmfo_core.phi() - 1.6180339887498948) < 1e-12

def test_tau():
    assert abs(cmfo_core.tau() - 0.6180339887498948) < 1e-12
