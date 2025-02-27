from ops.calculate import calc


def test_add():
    assert calc('1252+845') == 2097

def test_sub():
    assert calc('-4635-3584') == -8219

def test_mlt():
    assert calc('125*2123.15') == 265393.75

def test_div():
    assert calc('125/-25') == -5

def test_ZeroDivision():
    assert  calc("64211/0") == ZeroDivisionError
