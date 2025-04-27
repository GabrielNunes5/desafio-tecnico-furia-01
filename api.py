import os
import requests
from datetime import datetime

TOKEN = os.getenv("PANDASCORE_TOKEN")
BASE_URL = "https://api.pandascore.co/teams/furia/matches"
headers = {"Authorization": f"Bearer {TOKEN}"}


def fetch_matches(future: bool, limit: int = 3):
    """
    Retorna JSON com as partidas futuras (future=True) ou passadas (future=False),
    limitadas a ‘limit’ resultados.
    """
    params = {
        "filter[future]": str(future).lower(),
        "sort": "begin_at" if future else "-begin_at",
        "page[number]": 1,
        "page[size]": limit
    }
    resp = requests.get(BASE_URL, headers=headers, params=params)
    resp.raise_for_status()
    return resp.json()


def format_match(match: dict, future: bool) -> str:
    dt = datetime.fromisoformat(match["begin_at"].replace("Z", "+00:00"))
    # Pega o adversário
    opps = match["opponents"]
    opponent = next((o["opponent"]["name"]
                    for o in opps if o["opponent"]["name"] != "FURIA"), "TBD")

    if not future and "results" in match:
        # Mapeia scores por team_id
        scores = {r["team_id"]: r["score"] for r in match["results"]}
        furia_id = next(o["opponent"]["id"]
                        for o in opps if o["opponent"]["name"] == "FURIA")
        oppo_id = next(o["opponent"]["id"]
                       for o in opps if o["opponent"]["name"] != "FURIA")
        return f"{dt:%d/%m %H:%M} – {opponent} ({scores.get(oppo_id, 0)}) vs FURIA ({scores.get(furia_id, 0)})"
    return f"{dt:%d/%m %H:%M} – vs {opponent}"


def main():
    print("Próximas 3 partidas:")
    for m in fetch_matches(True):
        print(" •", format_match(m, True))

    print("\nÚltimas 3 partidas:")
    for m in fetch_matches(False):
        print(" •", format_match(m, False))


if __name__ == "__main__":
    main()
