

def print_table(portfolio, attri_list):
    print(' '.join('%10s' % fieldname for fieldname in attri_list))
    print(('-' * 10 + ' ') * len(attri_list))
    for record in portfolio:
        print(' '.join('%10s' % getattr(record, fieldname) for fieldname in attri_list))