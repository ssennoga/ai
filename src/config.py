from pathlib import Path
from dotenv import load_dotenv

load_dotenv()  # loads .env file if exists

BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"

TESTSET_PATH = DATA_DIR / "testset.json"

# You can also store LLM choice, temperature, etc. here
LLM_MODEL = "gpt-4o-mini"           # or "claude-3-5-sonnet", "llama-3.1-70b", etc.
EMBEDDING_MODEL = "text-embedding-3-small"
TEMPERATURE = 0.0