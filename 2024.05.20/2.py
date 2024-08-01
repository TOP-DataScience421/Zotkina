from decimal import Decimal, ROUND_HALF_UP
from datetime import datetime, date, time
import numbers

class PowerMeter:
    def __init__(self, 
                 tariff1: numbers.Number = 5, 
                 tariff2: numbers.Number = 3, 
                 tariff2_starts: time = time(23, 0), 
                 tariff2_ends: time = time(7, 0)):
        self.tariff1 = Decimal(tariff1).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        self.tariff2 = Decimal(tariff2).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        self.tariff2_starts = tariff2_starts
        self.tariff2_ends = tariff2_ends
        self.power = Decimal(0).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        self.charges = {}

    def __repr__(self):
        return f"<PowerMeter: {self.power} кВт/ч>"

    def __str__(self):
        total_charge = sum(self.charges.values())
        current_month = datetime.now().strftime('%b')
        return f"({current_month}) {total_charge.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)}"

    def meter(self, power: numbers.Number) -> Decimal:
        power = Decimal(power).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        now = datetime.now().time()

        if self.tariff2_starts < self.tariff2_ends:
            is_tariff2 = self.tariff2_starts <= now < self.tariff2_ends
        else: # охватывающий полночь
            is_tariff2 = now >= self.tariff2_starts or now < self.tariff2_ends

        rate = self.tariff2 if is_tariff2 else self.tariff1
        cost = (power * rate).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        
        self.power += power

        first_of_month = date(datetime.now().year, datetime.now().month, 1)
        if first_of_month not in self.charges:
            self.charges[first_of_month] = Decimal(0).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        self.charges[first_of_month] += cost
        self.charges[first_of_month] = self.charges[first_of_month].quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

        return cost

#Пример теста
#>>> pm1 = PowerMeter()
#>>> pm1.meter(2)
#Decimal('10.00')
#>>> pm1.meter(1.2)
#Decimal('6.00')
#>>> pm1
#<PowerMeter: 3.20 кВт/ч>
#>>> print(pm1)
#(Jul) 16.00

