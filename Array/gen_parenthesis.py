def gen_valid_parenthesis(n):
    if n < 1:
        return []

    all_valid_parenthesis = ['()']

    for i in range(1, n):
        current_valid_parenthesis_count = len(all_valid_parenthesis)
        for j in range(current_valid_parenthesis_count):
            p = all_valid_parenthesis[j]
            all_valid_parenthesis += [f'{p}()', f'({p})']
            if f'{p}()' != f'(){p}':
                all_valid_parenthesis += [f'(){p}']
        del all_valid_parenthesis[:current_valid_parenthesis_count]

    return all_valid_parenthesis


print(gen_valid_parenthesis(3))
