import { Julep } from "@julep/sdk";
import fs from "fs";
import yaml from "yaml";
import dotenv from "dotenv";
dotenv.config();

// Initialize the client
const client = new Julep({
  apiKey: process.env.JULEP_API_KEY,
});

// Create the agent
const agent = await client.agents.create({
  name: "Foodie Tour Planner",
  about: "Creates food tours based on weather and local dishes.",
  instructions: [
    "Be friendly and helpful.",
    "Suggest indoor or outdoor dining based on weather.",
    "Pick 3 iconic local dishes per city.",
    "Find top-rated restaurants serving these dishes.",
    "Create a delightful one-day foodie tour narrative.",
  ],
  model: "gpt-4o-mini",
});

// Load the task definition
const taskDefinition = yaml.parse(fs.readFileSync("foodie-tour.yaml", "utf8"));

// Create the task
const task = await client.tasks.create(agent.id, taskDefinition);

// Create the execution
const execution = await client.executions.create(task.id, {
  input: {
    cities: ["New York", "London", "Paris", "Tokyo", "Sydney"],
  },
});

let result;
while (true) {
  result = await client.executions.get(execution.id);
  if (result.status === "succeeded" || result.status === "failed") break;
  console.log(result.status);
  await new Promise((resolve) => setTimeout(resolve, 1000));
}

// Print the result
if (result.status === "succeeded") {
  console.log(result.output);
} else {
  console.error(`Error: ${result.error}`);
}
