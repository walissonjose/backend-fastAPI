import os
from dotenv import load_dotenv

load_dotenv()

port: int = int(os.getenv('SERVER_PORT') or 8000)

