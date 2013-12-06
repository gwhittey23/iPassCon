__author__ = 'gerardwhittey'
class PowerSchoolRouter(object):
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read auth models go to auth_db.
        """
        if model._meta.app_label == 'pwrschool':
            return 'pwrschool_db'
        return None