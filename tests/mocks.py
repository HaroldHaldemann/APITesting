import utils

MOCK_CLUBS = [
    {
        "name":"Simply Lift",
        "email":"john@simplylift.co",
        "points":"130"
    },
    {
        "name":"Iron Temple",
        "email": "admin@irontemple.com",
        "points":"4"
    },
    {   "name":"She Lifts",
        "email": "kate@shelifts.co.uk",
        "points":"12"
    }
]


MOCK_COMPETITIONS = [
        {
            "name": "Push&Pull",
            "date": "2023-11-24 18:30:00",
            "numberOfPlaces": "27"
        },
        {
            "name": "MrHuman",
            "date": "2023-08-11 08:00:00",
            "numberOfPlaces": "10"
        },
        {
            "name": "Spring Festival",
            "date": "2020-03-27 10:00:00",
            "numberOfPlaces": "5"
        },
        {
            "name": "Fall Classic",
            "date": "2020-10-22 13:30:00",
            "numberOfPlaces": "13"
        }
    ]

MOCK_PAST_COMPETITIONS = utils.get_past_competitions(MOCK_COMPETITIONS)

MOCK_PRESENT_COMPETITIONS = utils.get_present_competitions(MOCK_COMPETITIONS)
