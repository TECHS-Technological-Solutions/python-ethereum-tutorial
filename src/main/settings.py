import pathlib
from dotenv import load_dotenv


PROJECT_ROOT = pathlib.Path(__file__).parent.parent
load_dotenv(PROJECT_ROOT / ".env")

