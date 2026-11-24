"""Charm the commuter: forecast a city that isn't.

This program writes a single original one-line weather
forecast to /output/entry.txt, for a city that does not
exist. The forecast is a fixed string, the same text on
every run, with no randomness, no network use, and no
extra output.

The line keeps the register of a real broadcast forecast:
the city is named first, then the weather, then a timing
detail, in the forecast's own rhythm. The city, Hobbleton,
is invented. The weather itself is bent: breakfasts fall
scattered, like showers. The concrete detail is the 8:15
fog, a commuter's kind of weather: a fog with a timetable. The
turn at the end is the joke that makes a bored commuter
smile, because the fog is running late exactly the way
everyone at the bus stop is running late.
"""

import os

FORECAST = (
    "Hobbleton: overcast, with scattered second breakfasts; "
    "the 8:15 fog is running ten minutes late, like everyone else."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    """Write the forecast to the output file, with no trailing newline."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(FORECAST)


if __name__ == "__main__":
    main()
