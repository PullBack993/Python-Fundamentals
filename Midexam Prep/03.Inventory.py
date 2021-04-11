collect_item = input().split(', ')

command = input()


def is_items_in_list(d, i):
    if i in collect_item:
        return True
    return False


def collect_items(d, i):
    if not is_items_in_list(d, i):
        collect_item.append(i)
        return collect_item


def drop_items(d, i):
    if is_items_in_list(d, i):
        collect_item.remove(i)
    return collect_item


def combine_items(d, i):
    old_item = i.split(':')[0]
    new_items = i.split(':')[1]
    if is_items_in_list(collect_item, old_item):
        index_old_item = collect_item.index(old_item)
        index_new_item = index_old_item + 1
        collect_item.insert(index_new_item, new_items)
    return collect_item

def renew_items(d, i):
    if is_items_in_list(d, i):
        collect_item.remove(i)
        collect_item.append(i)
    return collect_item


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

print(", ".join(collect_item))
