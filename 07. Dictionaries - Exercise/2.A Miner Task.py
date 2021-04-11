resource = input()
counter = 0
resources = {}
save_resource_name = resource
while not resource == 'stop':
    if save_resource_name == '':
        save_resource_name = resource
    counter += 1

    if counter % 2 == 0 and save_resource_name in resources:
        resources[save_resource_name] += int(resource)
        save_resource_name = ''
    elif counter % 2 == 0:
        resources[save_resource_name] = int(resource)
        save_resource_name = ''
    resource = input()

for key, value in resources.items():
    print(f'{key} -> {value}')