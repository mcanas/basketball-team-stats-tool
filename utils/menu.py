import constants

menus = {}


def add_menu_item(index, option, item_map):
    key = constants.ALPHABET[index]
    label = option[0]
    item_map[key] = {
        'text': f'{key}) {label}',
        'option': option
    }
    return item_map


def add_menu(id, header=None, options=None, input_message='Enter an option', include_back=True, include_quit=True, previous_menu=None):
    menus[id] = {
        'id': id,
        'header': header,
        'options': options,
        'input_message': input_message,
        'include_back': include_back,
        'include_quit': include_quit,
        'previous_menu': previous_menu
    }
    return menus


def show_menu(id):
    config = menus[id]
    item_map = {}

    if config['options']:
        for index, option in enumerate(config['options']):
            item_map = add_menu_item(index, option, item_map)

    if config['include_back']:
        item_map = add_menu_item(
            len(item_map.keys()), (constants.BACK_LABEL, config['previous_menu']), item_map)

    if config['include_quit']:
        item_map = add_menu_item(len(item_map.keys()),
                                 (constants.QUIT_LABEL, None), item_map)

    while True:
        if config['header']:
            print(f'\n---- {config["header"]} ----\n')
        print('\n'.join([item['text'] for item in item_map.values()]))
        choice = input(f'\n{config["input_message"]}: ')
        try:
            if choice not in item_map.keys():
                raise ValueError(f'"{choice}" is not a valid option.')
            else:
                break
        except ValueError as err:
            print(f'\nOops! Something went wrong: {err}')

    return item_map[choice]['option']
