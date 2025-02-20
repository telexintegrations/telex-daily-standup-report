from typing import List
from pydantic import BaseModel

class Setting(BaseModel):
  label: str
  type: str
  required: bool
  default: str
  options: List[str] = None

class TickPayload(BaseModel):
  channel_id: str
  return_url: str
  settings: List[Setting]