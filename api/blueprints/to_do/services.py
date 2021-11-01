import logging

logger = logging.getLogger(__name__)


class ToDoClass:
    @staticmethod
    def example_method(arg):
        logger.warn(arg)
        return True
