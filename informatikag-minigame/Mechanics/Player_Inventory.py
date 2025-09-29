_player_inventory = {
    'gold': 100,
    'items': [],
    'max_size': 5
}


def add_item(item) -> str:
    if _player_inventory['max_size'] is len(_player_inventory['items']):
        return 'Inventory is already full'

    _player_inventory['items'].append(item)
    return 'Item added to the Inventory'


def remove_item(item_index):
    _player_inventory['items'].pop(item_index)


def get_item(item_index):
    return _player_inventory['items'][item_index]


def get_gold():
    return _player_inventory['gold']


def set_gold(gold):
    _player_inventory['gold'] = gold


def list_items():
    print("""Player Inventory:
ID - NAME - PRICE""")
    for idx, item in enumerate(_player_inventory['items']):
        print(str(idx) + ' - ' + item['name'] + ' - ' + str(item['price']))

    print()  # Prints a new line so it looks a bit better in the output
