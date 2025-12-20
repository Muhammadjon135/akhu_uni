energy_logs = """Heater,LivingRoom,8.5,5.0
TV,LivingRoom,2.0,1.0
Oven,Kitchen,4.0,0.5
OldFreezer,Garage,6.0,7.0
Lamp,Bedroom,0.5,0.5
Error,Line,Missing,Data
AC_Unit,Bedroom,5.0,8.0
"""
with open("energy_log.txt", "w") as f:
    f.write(energy_logs)
def audit_energy_usage(filename):
    list = []
    dict = {}
    with open(filename, "r") as f:
        for line in f:
            appliance, room, day_usage, night_usage = line.strip().split(",")
            try:
                total_usage = float(day_usage) + float(night_usage)
                # print(total_usage)
            except ValueError:
                pass
            else:
                if total_usage > 10:
                    list.append((appliance, total_usage))
                if room not in dict:
                    dict[room] = total_usage
                else:
                    dict[room] += total_usage
    return dict, list
def save_energy_report(room_totals, power_hogs):
    with open("energy_report.txt", "w") as f:
        f.write("ROOM ENERGY CONSUMPTION (kWh)\n")
        f.write("-----------------------------\n")
        for room, kwh in room_totals.items():
            f.write(f"{room}: {kwh}\n")
        f.write("\nPOWER HOGS (> 10 kWh)\n")
        f.write("-----------------------------\n")
        for appliance, total in power_hogs:
            f.write(f"{appliance} ({total} kWh)\n")
audit_energy_usage("energy_log.txt") 
room_totals, power_hogs = audit_energy_usage("energy_log.txt")
save_energy_report(room_totals, power_hogs)
