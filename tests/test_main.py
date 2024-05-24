from sphinx_d2 import __about__


def test_dummy()->None:
    a = 1
    assert a == 1

def test_version_exists() -> None:
    assert __about__.__version__
