class Motor():
    def __init__(self, Voltage, GearRatio, PPR,RPM):
        self.V = Voltage
        self.GR = GearRatio
        self.events = PPR * GearRatio
        self.RPM = RPM
