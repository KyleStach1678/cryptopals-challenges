def parse_cookie(cookie):
    mode = 'key'
    dict = {}
    current_key = ''
    current_value = ''

    for c in cookie:
        if mode == 'key':
            if c == '=':
                mode = 'value'
            else:
                current_key += c
        elif mode == 'value':
            if c == '&':
                mode = 'key'
                dict[current_key] = current_value
                current_key = ''
                current_value = ''
            else:
                current_value += c

    dict[current_key] = current_value
    return dict
