import requests


class NestThermostat:
    def __init__(self, token):
        # Initialize the class with the NEST access token
        self.token = token
        self.headers = {'Authorization': 'Bearer ' + self.token}
        self.devices_url = 'https://developer-api.nest.com/devices'
        self.thermostat_id = None

    def get_thermostat_id(self):
        # Retrieve the ID of the thermostat
        devices_response = requests.get(self.devices_url, headers=self.headers).json()
        for device in devices_response['thermostats'].values():
            if device['name'] == 'My Thermostat':
                self.thermostat_id = device['device_id']
                break

    def get_thermostat_data(self):
        # Retrieve the current data for the thermostat
        if self.thermostat_id is None:
            self.get_thermostat_id()
        thermostat_url = self.devices_url + '/thermostats/' + self.thermostat_id
        return requests.get(thermostat_url, headers=self.headers).json()

    def set_temperature(self, temperature):
        # Set the target temperature of the thermostat
        if self.thermostat_id is None:
            self.get_thermostat_id()
        thermostat_url = self.devices_url + '/thermostats/' + self.thermostat_id
        data = {'target_temperature_f': temperature}
        requests.put(thermostat_url, headers=self.headers, json=data)

    def set_fan_mode(self, mode):
        # Set the fan mode of the thermostat
        if self.thermostat_id is None:
            self.get_thermostat_id()
        thermostat_url = self.devices_url + '/thermostats/' + self.thermostat_id
        data = {'fan_mode': mode}
        requests.put(thermostat_url, headers=self.headers, json=data)

    def set_away_mode(self, mode):
        # Set the away mode of the thermostat
        if self.thermostat_id is None:
            self.get_thermostat_id()
        structure_id = self.get_structure_id()
        structure_url = self.devices_url + '/structures/' + structure_id
        data = {'away': mode}
        requests.put(structure_url, headers=self.headers, json=data)

    def get_structure_id(self):
        # Retrieve the structure ID of the thermostat
        devices_response = requests.get(self.devices_url, headers=self.headers).json()
        for structure_id, structure in devices_response['structures'].items():
            if self.thermostat_id in structure['thermostats']:
                return structure_id
        return None

    def get_energy_usage(self, start_time, end_time):
        # Retrieve the energy usage data for the thermostat
        if self.thermostat_id is None:
            self.get_thermostat_id()
        thermostat_url = self.devices_url + '/thermostats/' + self.thermostat_id + '/energy_usage'
        params = {'start_time': start_time, 'end_time': end_time}
        return requests.get(thermostat_url, headers=self.headers, params=params).json()
