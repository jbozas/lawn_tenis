from reservatuspot import ReservaTuSpot
import sys

if __name__ == "__main__":
    if len(sys.argv) != 7:
        print(
            "Usage: python reserva_spot.py <user_name> <password> <player1> <player2> <schedule>"
        )
        sys.exit(1)

    service = ReservaTuSpot(
        sys.argv[1], sys.argv[2], sys.argv[3:5], sys.argv[5], sys.argv[6]
    )
    service.book()
