from logging import Logger

from common.logger import get_logger
from common.engine import Engine
from data.event import get_events
from ffe.event_selector import EventSelector

logger: Logger = get_logger()


class FFEEngine(Engine):
    def __init__(self):
        super().__init__()
        while EventSelector(get_events()).run():
            pass
