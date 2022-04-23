import time
import random
from pettingzoo.butterfly import knights_archers_zombies_v9

env = knights_archers_zombies_v9.env()
env.reset()

manual_policy = knights_archers_zombies_v9.ManualPolicy(env)

def policy(obs, agent):
    return random.randint(0, 5) 

for agent in env.agent_iter():
    observation, reward, done, info = env.last()

    if agent == manual_policy.agent:
        action = manual_policy(observation, agent)
    else:
        action = policy(observation, agent)

    env.step(action)

    env.render()
    time.sleep(0.05)

    if done:
        env.reset()