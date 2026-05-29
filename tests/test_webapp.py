from pathlib import Path
import sys

# Ensure project root is importable
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.webapp.app import app


def test_dashboard_ok():
    client = app.test_client()
    resp = client.get('/')
    assert resp.status_code == 200
