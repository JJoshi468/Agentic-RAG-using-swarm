# from swarm import Swarm, Agent, Response
# client = Swarm()


# def transfer_to_agent_b():
#     return agent_b
#
#
# agent_a = Agent(
#     name="Agent A",
#     instructions="You are a helpful agent.",
#     functions=[transfer_to_agent_b],
# )
#
# agent_b = Agent(
#     name="Agent B",
#     instructions="Only speak in Gujarati. Welcome the user.",
# )
#
# response = client.run(
#     agent=agent_a,
#     messages=[{"role": "user", "content": "I want to talk to agent B."}],
# )
#
# print(response.messages[-1]["content"])

from swarm import Swarm, Agent
from openai import OpenAI

ollama_client = OpenAI(
    base_url = 'http://localhost:11434/v1',
    api_key='ollama'# required, but unused
)
# Initialize the Swarm client with a Llama model
client = Swarm(client=ollama_client)  # Specify the Llama model here

# Define the Sales Agent
sales_agent = Agent(
    model= 'llama3.2',
    name="Sales Agent",
    instructions="""Be enthusiastic about selling honey.
1. Greet the customer and ask for their name.
2. Find out if they have any specific concerns.
3. Explain the benefits of honey.
4. Offer a special discount.
5. Close the sale and thank the customer.
"""
)

# Example interaction with the Sales Agent
messages = [{"role": "user", "content": "I'm interested in buying some honey."}]
response = client.run(agent=sales_agent, messages=messages)

# Print the response from the Sales Agent
# print(response.messages[-1]["content"])
print(response)


