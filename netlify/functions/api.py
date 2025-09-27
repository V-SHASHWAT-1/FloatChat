# File: floatchat/netlify/functions/api.py

import sys
from pathlib import Path
from mangum import Mangum

# Add the backend app directory to the Python path
# This allows us to import your existing app
sys.path.append(str(Path(__file__).resolve().parent.parent.parent / "backend"))

# Import your existing FastAPI app instance
from app.main import app

# This handler is what Netlify will run
handler = Mangum(app)