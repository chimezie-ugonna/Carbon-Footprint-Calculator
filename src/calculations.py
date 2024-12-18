def calculate_energy_footprint(electricity_bill, gas_bill, fuel_bill):
    return (electricity_bill * 12 * 0.0005) + (gas_bill * 12 * 0.0053) + (fuel_bill * 12 * 2.32)

def calculate_waste_footprint(waste_generated, recycling_percentage):
    return (waste_generated * 12 * (0.57 - (recycling_percentage / 100)))

def calculate_business_travel_footprint(km_travel, fuel_efficiency):
    return km_travel * (1 / fuel_efficiency) * 2.31