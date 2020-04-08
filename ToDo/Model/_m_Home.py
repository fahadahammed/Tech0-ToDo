from ToDo.Library.TimeCalculator import TimeCalculator
import datetime


class _m_Home:
    """Create index"""
    def __init__(self):
        self.dt_now = str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
        self.to_return = {
            "_time": self.dt_now,
            "_msg": f"ToDo: {str(datetime.datetime.now().strftime('%Y-%m-%d'))}"
        }

    def get_home(self):
        self.to_return["_function"] = self.get_home.__name__
        return self.to_return
