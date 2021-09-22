from src.ticket import Ticket

import json


CONFIG_LOCATION = "config.json"


def main():
    ticket = Ticket(default_config=get_default_config())
    ticket.ask_for_title()
    ticket.ask_for_description()
    print(ticket)


def get_default_config():
    default_config = {}
    with open(CONFIG_LOCATION) as f:
        default_config = json.load(f)
    return default_config.get("defaults", {})


if __name__ == "__main__":
    main()
