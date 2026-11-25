def tally(rows):
    MP = {}
    W = {}
    D = {}
    L = {}

    for row in rows:
        data = row.split(';')
        MP[data[0]] = MP.get(data[0],0) + 1
        MP[data[1]] = MP.get(data[1],0) + 1
        if data[2] == 'win':
            W[data[0]] = W.get(data[0],0) + 1
            L[data[1]] = L.get(data[1],0) + 1
        elif data[2] == 'loss':
            L[data[0]] = L.get(data[0],0) + 1
            W[data[1]] = W.get(data[1],0) + 1
        else:
            D[data[0]] = D.get(data[0],0) + 1
            D[data[1]] = D.get(data[1],0) + 1
            
    sorted_teams = sorted(
        MP.keys(),
        key=lambda team: (-(W.get(team, 0) * 3 + D.get(team, 0)), team)
    )
    header = f"{'Team':<31}|{' MP ':^4}|{'  W ':^4}|{'  D ':^4}|{'  L ':^4}|{'  P':^3}"
    result = [header]

    for key in sorted_teams:
        mp = MP[key]
        w = W.get(key, 0)
        d = D.get(key, 0)
        l = L.get(key, 0)
        p = w * 3 + d
        result.append(f'{key:<31}|{str(mp)+" ":>4}|{str(w)+" ":>4}|{str(d)+" ":>4}|{str(l)+" ":>4}|{str(p):>3}')


    return result
