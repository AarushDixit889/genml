import ydata_profiling


class Analyzer:
    def __init__(self, data):
        self.data = data

    def saveReport(self, path, title):
        profile = ydata_profiling.ProfileReport(self.data, title=title)
        profile.to_file(path)
        return profile
