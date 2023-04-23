import logging
import os
import sys
from datetime import datetime
from pathlib import Path

logger_filepath = Path(
    os.getcwd() + f'/src/logs/{datetime.now().strftime("%m-%d-%Y")}.log'
)
if not os.path.isdir(Path(os.getcwd()) / "src/logs/"):
    os.mkdir(Path(os.getcwd() + "/src/logs/"))
logging.basicConfig(
    filename=logger_filepath,
    level=logging.DEBUG,
    format="%(levelname)s %(asctime)s - %(message)s",
    filemode="w",
)

logger = logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
sys.path.append(Path(__file__).parent.parent.parent.parent.as_posix())