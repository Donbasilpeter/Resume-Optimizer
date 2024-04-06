class Content:
    system_prompt = " You are world class Resume Writer. You could write resumes that can score high on any Applicant Tracking Software (ATS)."
    user_prompt = """You are given a resume and a job description. Update the resume so that the new resume better matches the job description. The end goal is to score high in any ATS system.
The resume is given as a JSON object and the output should also be the same.

The input and output resume format is given below :
{{
  "name": "",
  "title": "",
  "intro": "",
  "phone": "",
  "mail": "",
  "tools": [""],
  "education": [
    {{
      "institution": "",
      "location": "",
      "course": "",
      "start_date": "",
      "end_date": ""
    }}
  ],
  "skills": [
    ""
  ],
  "projects": [
    {{
      "name": "",
      "start_date": "",
      "end_date": "",
      "location": "",
      "position": "",
      "skills": [
        ""
      ]
    }}
  ],
  "experience": [
    {{
      "name": "",
      "start_date": "",
      "end_date": "",
      "location": "",
      "position": "",
      "skills": [
        ""
      ]
    }}
  ],
  "reference": ""
}}


Given below are the tasks:
1) Modify the content of the resume to better match the job description.
2) Don't change the context of the resume. Given resume has so much content. Output resume should highlight the parts that are relevant to the current job description.
3) Don't add false information. The content should be based on the input resume.
 for example, adding fake experience or adding skills that are not in the resume but are in the job description is not allowed.
4) Add keywords in the job description that we may miss in the resume. And give importance to experience that matters.
5) If the resume is not fit for the job description in any ways leave it as it is.

The following are the job description and input resume: 
"""



