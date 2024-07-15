class Solution(object):
    def survivedRobotsHealths(self, positions, healths, directions):
        robots = list(zip(positions, healths, directions, range(len(positions))))
        robots.sort()  # Sort based on positions

        stack = []
        survived = []

        for pos, health, dir, idx in robots:
            if dir == 'R':
                stack.append((pos, health, dir, idx))
            else:
                while stack and health > 0:
                    last_pos, last_health, last_dir, last_idx = stack[-1]
                    if last_dir == 'R':
                        if last_health > health:
                            stack[-1] = (last_pos, last_health - 1, last_dir, last_idx)
                            health = 0
                        elif last_health < health:
                            stack.pop()
                            health -= 1
                        else:
                            stack.pop()
                            health = 0
                    else:
                        break
                if health > 0:
                    survived.append((pos, health, dir, idx))

        survived.extend(stack)

        survived.sort(key=lambda x: x[3])
        return [health for _, health, _, _ in survived]
