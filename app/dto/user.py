from dataclasses import dataclass
from typing import Optional


@dataclass
class UserDTO():
    user_id: Optional[int]
    name: str
    email: str
    password: str
