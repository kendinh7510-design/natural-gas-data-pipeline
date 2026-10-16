
import logging
from pathlib import Path

def setup_logger():
    log_dir = Path(__file__).resolve().parents[1] / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(
                log_dir / "etl.log",
                encoding="utf-8"
            ),
            logging.StreamHandler()
        ],
        force=True
    )

    return logging.getLogger(__name__)
