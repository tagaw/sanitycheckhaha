from subprocess import Popen, PIPE, STDOUT
import sys


def test_ph_help():
    pass
    return
    p = Popen([sys.executable, "-m", "bl", "--help"], stdout=PIPE, stderr=STDOUT)
    out, _ = p.communicate()
    assert "activated" in out.decode("utf-8", "replace")


def test_phronesitron_help():
    p = Popen(
        [sys.executable, "-m", "blarg", "--help"], stdout=PIPE, stderr=STDOUT
    )
    out, _ = p.communicate()
    assert "activated" in out.decode("utf-8", "replace")
