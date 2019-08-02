from string import ascii_lowercase

def build_update_key_pair(val, old='', final=[], first=False):
    if isinstance(val, dict):
        for k in val.keys():
            final = build_update_key_pair(val[k], old + ('' if first else '.') + str(k), final)
    elif isinstance(val, list):
        for i,k in enumerate(val):
            final = build_update_key_pair(k, old + '.' + str(i), final)
    else:
        final.append({ 'key': old, 'value': val })

    return final


def build_expressions(method='SET', key_pair, first=False):
    update_expression = method
    expression_attribute_values = {}

    for index, expression in enumerate(key_pair):
        key = expression['key']
        value = expression['value']
        placeholder = ascii_lowercase[index]

        update_expression = update_expression + (', ' if index > 0 else '') + ' {} = :{}'.format(key, placeholder)
        expression_attribute_values[':' + placeholder] = value

    return update_expression, expression_attribute_values
