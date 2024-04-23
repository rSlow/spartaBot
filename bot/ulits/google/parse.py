import re
from concurrent.futures import ProcessPoolExecutor
from functools import partial
from io import BytesIO

from loguru import logger
import pandas as pd

from config import settings


class ExcelTableParser:
    def __init__(self):
        self.excel_file: pd.ExcelFile | None = None
        self._sheet_names: list[str] | None = None

    @property
    def sheet_names(self):
        if self._sheet_names is None and self.excel_file is not None:
            self._sheet_names = self.excel_file.sheet_names
        return self._sheet_names

    def _parse_sheet(self, sheet_name: str):
        excel: pd.DataFrame = self.excel_file.parse(
            sheet_name=sheet_name,
            header=None,
        )

    def parse(self, data: BytesIO):
        logger.info("Start parsing table")
        self.excel_file = pd.ExcelFile(data)
        sheet_pattern = re.compile(settings.COMPETITION_SHEET_NAME_RE)
        readable_sheets = [sheet for sheet in self.sheet_names if sheet_pattern.match(sheet)]

        with ProcessPoolExecutor(len(readable_sheets)) as pool:
            _ = [*pool.map(
                partial(self.excel_file.parse),
                readable_sheets
            )]
