import os
import sys
import pytest
import consts

_cwd = os.path.dirname(os.path.abspath(__file__))
_project_dir = os.path.dirname(_cwd)

sys.path.append(_project_dir)
os.environ["SHORTENER_WEB_SERVER"] = consts.SHORTENER_WEB_SERVER


from api import app


@pytest.fixture(scope="session")
def client():
    return app.test_client()
