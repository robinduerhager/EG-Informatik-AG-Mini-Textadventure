from Entities import Item
from Mechanics import Player_Inventory


# While the Items module holds all Items of  the game, the Shop module utilizes the Items module to sell Items.
# A Player should always use the Shop to acquire Items.
def show_items() -> None:
    Item.list_items()

def buy_item(item_index) -> None:
    item = Item.get_item(item_index)
    if Player_Inventory.get_gold() < item['price']:
        raise Exception('You do not have enough gold to buy this item.')
    else:
        Player_Inventory.set_gold(Player_Inventory.get_gold() - item['price'])
        Player_Inventory.add_item(item)


def sell_item(item_index) -> None:
    Player_Inventory.remove_item(item_index)
