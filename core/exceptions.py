class PersiaTraderError(Exception):
    """Base Exception"""
    pass


class DatabaseError(PersiaTraderError):
    pass


class ProviderError(PersiaTraderError):
    pass


class AnalysisError(PersiaTraderError):
    pass
