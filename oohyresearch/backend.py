# backend.py

from django.db.backends.base.base import BaseDatabaseWrapper
import logging

logger = logging.getLogger(__name__)

class CustomDatabaseWrapper(BaseDatabaseWrapper):
    def close_if_unusable_or_obsolete(self):
        try:
            if self.connection is not None:
                self.close()
        except Exception as e:
            logger.error(f"Error closing database connection: {e}")
