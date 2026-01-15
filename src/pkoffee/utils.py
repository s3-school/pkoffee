from pathlib import Path
from typing import Dict
import pandas as pd


def read_config(config_path: Path) -> Dict:
    pass


def load_data(data_path: Path) -> pd.DataFrame:
    pass


def create_plot(data: pd.DataFrame, x_col: str, y_col: str):
    pass


def save_plot(fig, output_path: Path):
    pass