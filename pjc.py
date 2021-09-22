from src.ticket import Ticket


def main():
    ticket = Ticket()
    ticket.ask_for_title()
    ticket.ask_for_description()
    print(ticket)


if __name__ == "__main__":
    main()
