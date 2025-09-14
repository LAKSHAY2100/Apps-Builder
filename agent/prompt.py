def planner_prompt(user_prompt):
    prompt = f"""
You are a planner agent. Convert the user prompt into a complete engineering project plan.

User Prompt: {user_prompt}

Please create a detailed project plan that includes:
1. A clear project name and description
2. Appropriate technology stack for the project
3. Key features the application should have
4. A list of files that need to be created with their purposes

Make sure to be specific and practical in your recommendations.
"""
    return prompt