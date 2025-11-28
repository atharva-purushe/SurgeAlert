import random
from datetime import datetime

_state = {
    "beds": 1200,
    "icu": 140,
    "opd": 800,
    "pm25": 250,
    "pm10": 300,
    "aqi": 290,
    "festival_days_left": 5
}


def _bounded(value, min_v, max_v):
    return max(min_v, min(value, max_v))


def generate_pollution():
    _state["pm25"] += random.randint(-5, 15)
    _state["pm10"] += random.randint(-10, 20)

    _state["pm25"] = _bounded(_state["pm25"], 150, 550)
    _state["pm10"] = _bounded(_state["pm10"], 180, 600)

    _state["aqi"] = int(_state["pm25"] * 0.7 + _state["pm10"] * 0.3)

    return {
        "pm25": _state["pm25"],
        "pm10": _state["pm10"],
        "aqi": _state["aqi"]
    }


def generate_festival_impact():
    _state["festival_days_left"] -= 1
    if _state["festival_days_left"] < 0:
        _state["festival_days_left"] = random.randint(4, 10)

    festival_impact = max(0.1, 1.0 - (_state["festival_days_left"] * 0.1))

    return {
        "festival_days_left": _state["festival_days_left"],
        "festival_impact": round(festival_impact, 2)
    }


def generate_capacity():
    _state["beds"] += random.randint(-10, 40)
    _state["icu"] += random.randint(-2, 8)
    _state["opd"] += random.randint(-20, 80)

    _state["beds"] = _bounded(_state["beds"], 400, 2500)
    _state["icu"] = _bounded(_state["icu"], 50, 350)
    _state["opd"] = _bounded(_state["opd"], 300, 2000)

    return {
        "beds": _state["beds"],
        "icu": _state["icu"],
        "opd": _state["opd"]
    }


def generate_mobility():
    return {
        "mobility_transit": random.randint(-10, 40),
        "mobility_retail": random.randint(-20, 60),
        "mobility_workplace": random.randint(-15, 20)
    }


def generate_full_signal_packet(hospital_id: int = 1):
    pollution = generate_pollution()
    festival = generate_festival_impact()
    capacity = generate_capacity()
    mobility = generate_mobility()

    return {
        "hospital_id": hospital_id,
        "pm25": pollution["pm25"],
        "pm10": pollution["pm10"],
        "aqi": pollution["aqi"],
        "beds": capacity["beds"],
        "icu": capacity["icu"],
        "opd": capacity["opd"],
        "festival_days_left": festival["festival_days_left"],
        "festival_impact": festival["festival_impact"],
        "mobility_transit": mobility["mobility_transit"],
        "mobility_retail": mobility["mobility_retail"],
        "mobility_workplace": mobility["mobility_workplace"],
        "timestamp": datetime.utcnow().isoformat()
    }
