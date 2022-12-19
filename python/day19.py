import re
lines = open('inputs/input.txt').readlines()
lines = [line.strip() for line in lines]

costs = list()
for line in lines: 
    costs.append([int(i) for i in re.findall(r'\d+', line)])

def quality_heuristic(state): 
    minutes, (robots, inventory, mined) = state
    return 1000*mined[3] + 100*mined[2] + 10*mined[1] + mined[0]

def bfs(costs, robots, num_minutes, top_queue = 30000):
    queue = list()
    queue.append((0, (robots, (0,0,0,0), (0,0,0,0)))) # (minutes, (robots, inventory, mined))
    max_geodes_mined = 0
    depth = 0
    while queue:
        minutes, (robots, old_inventory, mined) = queue.pop(0)

        if minutes > depth: 
            queue.sort(key=quality_heuristic, reverse=True)
            queue = queue[:top_queue]
            depth = minutes

        if minutes == num_minutes:
            max_geodes_mined = max(max_geodes_mined, mined[3])
            continue
       
        new_inventory = tuple([old_inventory[i] + robots[i] for i in range(4)])
        new_mined = tuple([mined[i] + robots[i] for i in range(4)])
        
        queue.append((minutes+1, (robots, new_inventory, new_mined)))

        for i in range(4):
            cost_robot = costs[i]

            if all([old_inventory[j] >= cost_robot[j] for j in range(4)]):
                new_robots = list(robots)
                new_robots[i] += 1
                new_robots = tuple(new_robots)

                new_inventory_state = tuple([new_inventory[j] - cost_robot[j] for j in range(4)])
                queue.append((minutes+1, (new_robots, new_inventory_state, new_mined)))
    return max_geodes_mined

max_minutes = 24
sum_quality = 0
for blueprint_id, cost_ore_robot, cost_clay_robot, ob_ore, obs_clay, geode_ore, geode_ob in costs:
    cost_per_robot = [
        (cost_ore_robot, 0, 0, 0),
        (cost_clay_robot, 0, 0, 0),
        (ob_ore, obs_clay, 0, 0),
        (geode_ore, 0, geode_ob, 0)
    ]
    num_mined = bfs(cost_per_robot, (1,0,0,0), max_minutes, top_queue=1000)

    sum_quality += num_mined*blueprint_id
    # Debugging
    # print(f'Blueprint {blueprint_id}: {num_mined} geodes mined')
print("Part 1", sum_quality)

max_minutes = 32
product_geodes = 1
for blueprint_id, cost_ore_robot, cost_clay_robot, ob_ore, obs_clay, geode_ore, geode_ob in costs[:3]:
    cost_per_robot = [
        (cost_ore_robot, 0, 0, 0),
        (cost_clay_robot, 0, 0, 0),
        (ob_ore, obs_clay, 0, 0),
        (geode_ore, 0, geode_ob, 0)
    ]
    num_mined = bfs(cost_per_robot, (1,0,0,0), max_minutes, top_queue=10000)
    product_geodes *= num_mined
    # Debugging
    # print(f'Blueprint {blueprint_id}: {num_mined} geodes mined')
print("Part 2", product_geodes)