import uvicorn
import sys
from pathlib import Path
import os

if __name__ == "__main__":
    path = Path(os.path.realpath(__file__)).parent.parent.absolute()
    sys.path.append(str(path))
    uvicorn.run("src.app.main:app", host="0.0.0.0", reload=True, port=8080)
