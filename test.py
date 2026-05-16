import asyncio
import datetime
import json
from typing import Literal
import uuid
from Modules import SupabaseReader

user = SupabaseReader.get_user("d7cb0869-5ed9-465c-87bf-0fb95aaebbd5")

print(len(user.owned_games))