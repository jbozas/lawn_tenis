import requests
import datetime


class ReservaTuSpot:
    url = 'https://back.reservatuspot.com:4000'
    hourly_lag = 1.6
    token: str
    hour: str
    day: str
    user_name: str
    password: str
    players: list

    def _parse_schedule(self, schedule):
        self.day, self.hour = schedule.split(' ')

    def __init__(self, user_name, password, players, schedule):
        self.user_name = user_name
        self.password = password
        self.players = players
        self._parse_schedule(schedule)

    def get(self, url: str, payload: dict = None):
        return requests.get(self.url + url, data=payload, headers={'Authorization': self.token})

    def post(self, url: str, payload: dict = None):
        return requests.post(self.url + url, data=payload)

    def get_token(self):
        response = self.post(url='/user/login', payload={
            'usuario': self.user_name,
            'password': self.password
        })
        self.token = response.json().get('Token')

    def schedules_availables(self, match_type: str, field='undefined'):
        return self.get(url=f'/reservas/bringHoursFree/{self.day}/{field}/{match_type}').json()

    def get_user_id(self, user_name: str):
        return str(self.get(url=f'/reservas/getID/{user_name}').json().get('resultado')[0].get('ID_Usuario'))

    def get_players_ids(self):
        players = [self.get_user_id(user_name) for user_name in self.players]
        if len(players) == 2:
            players.extend(['0', '0'])
        return players.pop(0), '/'.join(players)

    def closest_schedule(self, match_type: str):
        response = self.schedules_availables(match_type)
        for available in response.get('resultado'):
            available = available.get('Hora')
            hour = int(available)
            minutes_splitted = str(available).split('.')
            minutes = int(
                minutes_splitted[1])/self.hourly_lag if len(minutes_splitted) == 2 else 0
            wanted_hour, wanted_minutes = self.hour.split('.')
            if hour == int(wanted_hour) and minutes == int(wanted_minutes) or hour > int(wanted_hour):
                return available

    def book(self):
        # Get token
        self.get_token()
        # Search for a schedule
        match_type = 'Single' if len(self.players) < 3 else 'Dobles'
        schedule = self.closest_schedule(match_type)

        # Get players IDs
        self_id, players = self.get_players_ids()

        # Make the reservation
        day = 'Hoy' if datetime.datetime.now().day == self.day else 'Manana'
        print(self.get(
            url=f'/reservas/makeReserva/{self_id}/1/{day}/{schedule}/{match_type}/{players}').json())
