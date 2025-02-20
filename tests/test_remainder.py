import pytest
from tests import client
from unittest.mock import patch

@pytest.mark.asyncio
async def test_get_integration_json():
  response = client.get("/integration.json")
  assert response.status_code == 200
  res = response.json()
  data = res.get("data")
  assert "descriptions" in data
  assert len(data.get("settings")) == 3
  assert data.get("tick_url").endswith("/tick")

@pytest.mark.asyncio
async def test_tick_endpoint():
  payload = {
    "channel_id":"test_channel",
    "return_url":"http://test_url",
    "settings":[
      {"label": "Reminder Message", "type": "text", "required": True, "default": "Custom reminder"},
      {"label": "Mention Type", "type": "dropdown", "required": True, "default": "@here", "options": ["@channel", "@here"]}
    ]
  }

  with patch("httpx.AsyncClient.post") as mock_post:
    response = client.post("/tick", json=payload)
    assert response.status_code == 202
    assert response.json() == {"status": "accepted"}
    mock_post.assert_awaited_once()
    mock_post.assert_awaited_with(
      "http://test_url",
      json={
        "event_name": "Daily Standup Report",
        "message": "@here Custom reminder",
        "status": "success",
        "username": "Standup Bot",
      }
    )
