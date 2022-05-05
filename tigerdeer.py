from pettingzoo.magent import tiger_deer_v3
import numpy as np

env = tiger_deer_v3.env()
env.reset() 
done = False

agent_list = env.possible_agents
# print(agent_list)
# action_space = env.action_space([-1])
# print(action_space)

observation, reward, done, info = env.last()
print(type(observation), type(reward), type(done), type(info))
print(observation.shape)

# from pettingzoo.utils import random_demo
# random_demo(env, render=False, episodes=1)

# while not done:
#     action_dict = {agent: env.action_space(agent).sample() for agent in agent_list}
#     print(type(action_dict), action_dict)
#     next_state, reward_dict, done_dict, _ = env.step(action_dict) 
#     done = all(done_dict.values())