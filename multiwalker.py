from pettingzoo.sisl import multiwalker_v8
import numpy as np

env = multiwalker_v8.env(n_walkers=3)
env.reset() 
# print(env.action_space('walker_0'))
# print(env.observation_space('walker_0'))

done = False
while not done:
    env.step((np.random.rand(4) * 2 - 1).tolist())
    
    ret = env.last()
    print(ret)


    # observation, reward, done, info = env.step(np.random.rand(4).tolist())
    env.render()

# env.reset()
# for agent in env.agent_iter():
#     observation, reward, done, info = env.last()
#     action = policy(observation, agent)
#     env.step(action)
#     env.render()
