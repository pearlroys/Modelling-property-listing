number_of_pds = len(answers ['physical_devices 1))
for device in datal devices'1: 

    if devicel'id'] == answers| virtual_device_id']:

        answers l'energy_capacity'] = int (devicel'energyCapacity 1) / 1000000
        # for pd's with > that 25m values, we need to divide the values by the number of PD's

        if answers|'site_power'] > 25 or answers'energy_capacity 1 > 25:
            answersI[]'site_power'] = (max(devicel maxImport'1, device [maxExport 1) /number_of_pds) / 1000000
            answers'energy_capacity'] = (max (devicel'maxImport'1,device [maxExport 1) /number_of pds) / 1000000