from datetime import datetime


def get_session():

    hour = datetime.now().hour

    if 0 <= hour < 7:
        session = "Sydney"

    elif 7 <= hour < 13:
        session = "Tokyo"

    elif 13 <= hour < 20:
        session = "London"

    else:
        session = "New York"

    return {

        "local_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "session": session,
        "volatility": "Unknown"

    }