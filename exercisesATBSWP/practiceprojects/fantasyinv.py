inventory = {
    'rope': 1,
    'torch': 6,
    'gold coin': 42,
    'dagger': 1,
    'arrow': 12
}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'ruby', 'rope', 'rope', 'rope']


def display_inventory(player_inventory):
    print("Inventory:")
    for item, amount in inventory.items():
        print(f"{str(amount)} {item}(s)")


def add_to_inventory(player_inventory, added_items):
    for loot in added_items:
        if loot in player_inventory.keys():
            player_inventory[loot] += 1
        if loot not in player_inventory.keys():
            player_inventory[loot] = 1
    return player_inventory


final_inventory = add_to_inventory(inventory, dragon_loot)
display_inventory(final_inventory)
