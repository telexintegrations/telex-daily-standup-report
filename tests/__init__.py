from main import app
from fastapi.testclient import TestClient

client = TestClient(app, base_url="http://test/api/v1")