import os
import time
import yaml
from julep import Julep
from dotenv import load_dotenv

load_dotenv()

try:
    client = Julep(api_key=os.environ.get("JULEP_API_KEY"))
    print("Client initialized successfully")

    agent = client.agents.create(
        name="Foodie Tour Planner",
        about="Creates food tours based on weather and local dishes.",
        instructions=[
            "Be friendly and helpful.",
            "Suggest indoor or outdoor dining based on weather.",
            "Pick 3 iconic local dishes per city.",
            "Find top-rated restaurants serving these dishes.",
            "Create a delightful one-day foodie tour narrative.",
        ],
        model="gpt-4o-mini",
    )
    print(f"Agent created successfully: {agent.id}")

    with open("foodie-tour.yaml", "r") as file:
        task_definition = yaml.safe_load(file)
    print("YAML loaded successfully")

    task = client.tasks.create(agent_id=agent.id, **task_definition)
    print(f"Task created successfully: {task.id}")

    execution = client.executions.create(
        task_id=task.id,
        input={"cities": ["New York"]}  # Start with just one city for testing
    )
    print(f"Execution started: {execution.id}")

    while True:
        result = client.executions.get(execution.id)
        print(f"Status: {result.status}")
        
        if result.status == "succeeded":
            print("Execution completed successfully!")
            print(result.output)
            break
        elif result.status == "failed":
            print("Execution failed!")
            
            try:
                execution_details = client.executions.get(execution.id, include="steps")
                print(f"Full execution object: {execution_details}")
            except Exception as detail_error:
                print(f"Could not get execution details: {detail_error}")
            
            break
        
        time.sleep(2)

except Exception as e:
    print(f"✗ Unexpected error: {e}")
    import traceback
    traceback.print_exc()
