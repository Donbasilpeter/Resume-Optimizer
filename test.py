from LLM.optimizer import ResumeOptimizer
import os
from dotenv import load_dotenv
import json
import re



# Load environment variables from .env file
load_dotenv()
# Check if the API key is available
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OpenAI API key is missing. Please set the OPENAI_API_KEY environment variable.")

if __name__ =="__main__":
    with open("job_description.txt", 'r') as file:
        job_description = file.read()
    with open("resume.json", 'r') as file:
        resume = file.read()
        
    resumeObject = ResumeOptimizer(api_key=api_key)
    resumeObject.generate_resume(job_description=job_description,resume=resume)
    
    print(resumeObject.output)
    # Assuming `resumeObject.output` contains the string 'json {"name":"hh"}'
# Assuming `resumeObject.output` contains the JSON string: '\n {"name": "DON BASIL PETER"}'
    resume_output_str = resumeObject.output

    # Save the JSON string to a file
    with open('resume_output.json', 'w') as f:
        f.write(resume_output_str.strip())  # Remove leading/trailing whitespace if necessary

        
    
    