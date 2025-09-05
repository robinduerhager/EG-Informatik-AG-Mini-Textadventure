_inventory = {
    'gold': 0,
    'items': [
        {'type': 'WEAPON', 'weapon_type': 'BLADE', 'name': 'test_blade',
         'damage_multiplier': 2},
        {'type': 'WEAPON', 'weapon_type': 'BOW', 'name': 'test_bow',
         'damage_multiplier': 3}
    ],
    'size': 5
}


def add_item(item) -> str:
    if _inventory['size'] is len(_inventory['items']):
        return 'Inventory is already full'

    _inventory['items'].append(item)
    return 'Item added to the Inventory'


def remove_item(item_index):
    _inventory['items'].pop(item_index)


def get_item(item_index):
    return _inventory['items'][item_index]


def list_items():
    print('Inventory Items:')
    for idx, item in enumerate(_inventory['items']):
        print(str(idx) + ' - ' + item['name'])
