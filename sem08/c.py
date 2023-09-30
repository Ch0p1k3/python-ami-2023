class BannerStat:
    def __init__(self, clicks: int, shows: int):
        self._clicks = clicks
        self._shows = shows

    def add_click(self) -> None:
        self._clicks += 1

    def add_show(self) -> None:
        self._shows += 1

    @property
    def clicks(self) -> int:
        return self._clicks

    @property
    def shows(self) -> int:
        return self._shows

    def compute_ctr(self, default_ctr: float) -> float:
        if self.shows == 0:
            return default_ctr
        else:
            return self.clicks / self.shows


print(BannerStat.__dict__)
