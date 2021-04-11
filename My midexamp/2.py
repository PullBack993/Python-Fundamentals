particles = input().split("|")

command = input()

while not command == 'Done':
    data = command.split()
    name = data[0]
    function = data[1]
    if name == 'Move':
        index = data[2]
        index = int(index)
        if function == 'Left':
            if 0 < index <= len(particles):
                save_index_particles = particles[index]
                particles.pop(index)
                particles.insert(index-1, save_index_particles)
        elif function == 'Right':
            if 0 <= index < len(particles):
                save_index_particles = particles[index]
                particles.pop(index)
                particles.insert(index+1, save_index_particles)
    if name == 'Check':
        if function == 'Odd':
            save_name = []
            for n in range(len(particles)):
                if n % 2 == 1:
                    save_name.append(particles[n])
            print(" ".join(save_name))

        elif function == 'Even':
            save_name = []
            for n in range(len(particles)):
                if n % 2 == 0:
                    save_name.append(particles[n])
            print(" ".join(save_name))
    command = input()

print(f"You crafted {''.join(particles)}!")