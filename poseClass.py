#This is the yoga pose class. Wu, yin, vin, pow and cd stand for warm-up, yin, vinyasa, power and cool-down
class pose:
    def __init__(self, id, name, int, primary, secondary, is_wu, is_yin, is_vin, is_pow, is_cd):
        self.id = id
        self.name = name
        self.int = int
        self.primary = primary
        self.secondary = secondary
        self.is_wu = is_wu
        self.is_yin = is_yin
        self.is_vin = is_vin
        self.is_pow = is_pow
        self.is_cd = is_cd
