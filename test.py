from LLM.optimizer import ResumeOptimizer
import os
from dotenv import load_dotenv



# Load environment variables from .env file
load_dotenv()
# Check if the API key is available
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OpenAI API key is missing. Please set the OPENAI_API_KEY environment variable.")

if __name__ =="__main__":
    with open("Data/job_description.txt", 'r') as file:
        job_description = file.read()
    with open("Data/resume.json", 'r') as file:
        resume = file.read()
        
    resumeObject = ResumeOptimizer(api_key=api_key)
    resumeObject.generate_resume(job_description=job_description,resume=resume)
    

    resume_output_str = resumeObject.output

    # Save the JSON string to a file
    with open('Data/resume_output.json', 'w') as f:
        f.write(resume_output_str.strip())  

        
    
    