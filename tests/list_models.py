import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from config import client

for model in client.models.list():
    print(model.name)