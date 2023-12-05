"""Functions to prevent a nuclear meltdown."""

"""This function checks if a nuclear reactor is critically balanced by checking if the temperature is less than 800 K, the number of neutrons emitted per second is greater than 500, and that the temperature * neutrons_emitted is less than 500000"""


def is_criticality_balanced(temperature, neutrons_emitted):
    if temperature < 800 and neutrons_emitted > 500:
        if temperature * neutrons_emitted < 500000:
            return True
    return False


"""This function checks the efficiency of the reactor by calculating the generated power and comparing it to theoretical_max_power as a ratio"""


def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    power_eff = (generated_power / theoretical_max_power) * 100

    if power_eff >= 80:
        return "green"
    if 60 <= power_eff < 80:
        return "orange"
    if 30 <= power_eff < 60:
        return "red"
    return "black"


"""This function compares the energy produced to the threshold and indicates wether control rods should removed or added to return the levels to NORMAL"""


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    energy = temperature * neutrons_produced_per_second

    if energy < 0.9 * threshold:
        return "LOW"
    if 0.9 * threshold <= energy <= 1.1 * threshold:
        return "NORMAL"
    return "DANGER"
