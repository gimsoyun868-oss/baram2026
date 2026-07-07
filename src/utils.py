"""공통 유틸리티 (시드 고정, 로깅 등)."""

from __future__ import annotations

import logging
import random

import numpy as np


def set_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    try:
        import os

        os.environ["PYTHONHASHSEED"] = str(seed)
    except Exception:
        pass


def get_logger(name: str = "baram2026") -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "[%(asctime)s] %(levelname)s %(name)s - %(message)s", "%H:%M:%S"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger
