from voluptuous import Schema, PREVENT_EXTRA
valid_trainer = Schema(
    {"status": "success",
    "data":
            [
                {
                "id":str,
                "trainer_name":str,
                "level":str,
                "pokemons":list,
                "pokemons_alive":list,
                "pokemons_in_pokeballs":list,
                "get_history_battle":str,
                "is_premium":bool,
                "premium_duration":int,
                "avatar_id":int,
                "city":str
                }
            ]   
    },
    extra=PREVENT_EXTRA,
    required=True
)

invalid_intager_trainer = Schema(
    {
        "status": str,
        "message": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

invalid_string_trainer = Schema(
    {
        "detail": [
            {
                "type": str,
                "loc": [str, str],
                "msg": str,
                "input": str,
                "url": str
            }
        ]
    },
    extra=PREVENT_EXTRA,
    required=True
)