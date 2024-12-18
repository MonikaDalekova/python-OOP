from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):
    STRENGTH = 200

    def __init__(self, name):
        super().__init__(name, strength=self.STRENGTH)

    def can_climb(self):
        return self.strength >= 100

    def climb(self, peak: BasePeak):
        if peak.difficulty_level == 'Extreme':
            self.strength -= 20 * 2
        else:
            self.strength -= 20 * 1.5
        self.conquered_peaks.append(peak.name)
