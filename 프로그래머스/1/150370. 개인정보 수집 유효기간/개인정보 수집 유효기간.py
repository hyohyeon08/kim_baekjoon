def solution(today, terms, privacies):
    today = today.replace('.', '')

    di = {}
    for i in terms:
        n, m = i.split()
        di[n] = int(m)

    result = []
    for idx, privacy in enumerate(privacies, start=1):
        date_str, term_type = privacy.split()
        year, month, day = map(int, date_str.split('.'))

        month += di[term_type]
        if month > 12:
            year += (month - 1) // 12
            month = ((month - 1) % 12) + 1

        expiration_date = f"{year}{month:02d}{day:02d}"
        expiration_date = int(expiration_date)

        if int(today) >= expiration_date:
            result.append(idx)
    return result