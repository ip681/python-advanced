def team_lineup(*args):
    country_data = {}
    for pl, ctr in args:
        if ctr in country_data:
            country_data[ctr].append(pl)
        else:
            country_data[ctr] = [pl]

    sorted_ctr = dict(sorted(country_data.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])))

    rt = []
    for ctr, country_players in sorted_ctr.items():
        rt.append(f"{ctr}:")

        for pl in country_players:
            rt.append(f"  -{pl}")

    return "\n".join(rt)