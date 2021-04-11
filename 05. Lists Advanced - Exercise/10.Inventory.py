def is_items_in_list(d, i):
    if i in collecting_items:
        return True
    return False


def collect_items(d, i):
    if not is_items_in_list(d, i):
        collecting_items.append(i)
        return collecting_items


def drop_items(d, i):
    if is_items_in_list(d, i):
        collecting_items.remove(i)
    return collecting_items


def combine_items(d, i):
    old_item = i.split(':')[0]
    new_items = i.split(':')[1]
    if is_items_in_list(collecting_items, old_item):
        index_old_item = collecting_items.index(old_item)
        index_new_item = index_old_item + 1
        collecting_items.insert(index_new_item, new_items)
    return collecting_items


def renew_items(d, i):
    if is_items_in_list(d, i):
        collecting_items.remove(i)
        collecting_items.append(i)
    return collecting_items


collecting_items = input().split(', ')
command = input()
while not command == 'Craft!':
    data, item = command.split(' - ')
    if data == 'Collect':
        collect_items(data, item)
    elif data == 'Drop':
        drop_items(data, item)
    elif data == 'Combine Items':
        combine_items(data, item)
    elif data == 'Renew':
        renew_items(data, item)
    command = input()

print(", ".join(collecting_items))