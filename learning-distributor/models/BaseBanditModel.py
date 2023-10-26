class BaseBanditModel:
    def choose_composition_index(self) -> int:
        return 0

    def update(self, action: int, reward: float) -> None:
        return None