# deployment_engineer.py

import os
import subprocess

class DeploymentEngineer:
    def __init__(self, project_path):
        self.project_path = project_path
    
    def plan_deployment(self):
        # Create deployment plan
        deployment_plan = self._create_deployment_plan()
        
        # Save deployment plan to file
        self._save_deployment_plan(deployment_plan)
        
        return deployment_plan
    
    def execute_deployment(self):
        # Load deployment plan from file
        deployment_plan = self._load_deployment_plan()
        
        # Execute deployment plan
        self._execute_commands(deployment_plan)
    
    def _create_deployment_plan(self):
        # Define deployment plan as a list of commands
        deployment_plan = [
            "docker build -t ai_prompt_generation .",
            "docker run -d -p 5000:5000 ai_prompt_generation",
            "kubectl apply -f deployment.yaml",
            "kubectl apply -f service.yaml"
        ]
        
        return deployment_plan
    
    def _save_deployment_plan(self, deployment_plan):
        # Save deployment plan to a file
        with open(os.path.join(self.project_path, "deployment_plan.txt"), "w") as file:
            for command in deployment_plan:
                file.write(command + "\n")
    
    def _load_deployment_plan(self):
        # Load deployment plan from file
        deployment_plan = []
        
        with open(os.path.join(self.project_path, "deployment_plan.txt"), "r") as file:
            for line in file:
                deployment_plan.append(line.strip())
        
        return deployment_plan
    
    def _execute_commands(self, commands):
        # Execute commands in the deployment plan
        for command in commands:
            subprocess.run(command, shell=True)

# Example usage
if __name__ == "__main__":
    project_path = os.path.dirname(os.path.abspath(__file__))
    deployment_engineer = DeploymentEngineer(project_path)
    
    deployment_plan = deployment_engineer.plan_deployment()
    print("Deployment plan created:", deployment_plan)
    
    deployment_engineer.execute_deployment()
    print("Deployment executed successfully.")
