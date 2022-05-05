# run with conda env 'hcpark'

import pettingzoo.mpe.simple_tag_v2 as simple_tag_v2
import numpy as np

# env = simple_tag_v2.env(continuous_actions=True)
# env = simple_tag_v2.env()
env = simple_tag_v2.parallel_env(num_obstacles = 0)
env.reset() 
done = False

agent_list = env.possible_agents
print(agent_list)
action_space = env.action_space('agent_0')
action_space2 = env.action_space('adversary_0')
print(action_space, action_space2)

# for _ in range(100):
#     print(action_space.sample(), action_space2.sample())

# res = env.last()
# observation, reward, done, info = res
# print(res, observation.shape)

rewards_list = []
while not done:
    # Use policy here to pick an action
    action_dict = {agent: env.action_space(agent).sample() for agent in agent_list}
    # print(type(action_dict), action_dict)
    next_state, reward_dict, done_dict, _ = env.step(action_dict) 

    # 💡 relative position test
    N = len(agent_list)
    MY_XPOS = 2
    MY_YPOS = 3
    xpos = [0] * N
    ypos = [0] * N
    for idx, (agentName, obs) in enumerate(next_state.items()):
        xpos[idx] = obs[MY_XPOS]
        ypos[idx] = obs[MY_YPOS]

    cmpDouble = lambda f1, f2 : (f1-f2) < 1e-6 # compare two doubles

    for idx, (agentName, obs) in enumerate(next_state.items()):
        # Assumption : obs filled starting with the next agent -> No! in order of world.agents 
        for k in range(N-1): # all other agents except me
            nidx = k + (1 if k >= idx else 0) # other agent's index, passing me
            relX = obs[4 + 2*k] # other pos X (relative)
            relY = obs[4 + 2*k + 1] # other pos Y (relative)
            absX = xpos[idx] + relX 
            absY = ypos[idx] + relY
            print(f"rel to agent[{idx}] {agentName} {(relX, relY)}, abs pos {(absX, absY)}")
            # assert(absX == xpos[nidx] and absY == ypos[nidx])
            assert(cmpDouble(absX, xpos[nidx]) and cmpDouble(absY, ypos[nidx])) # confirmed visibility

    rewards_list.append(reward_dict)
    done = all(done_dict.values())

for i, rew in enumerate(rewards_list):
    print(i, rew)



