from reservatuspot import ReservaTuSpot

if __name__ == '__main__':
    # Params
    user_name = 'XXXXX@gmail.com'
    password = 'XXXXXXX'
    players = ['Julian_BXXXX', 'XXXX_GXXXX']
    schedule = '11 19.10'
    # Command.
    service = ReservaTuSpot(
        user_name, password, players, schedule)
    service.book()
