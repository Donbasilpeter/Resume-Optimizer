from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from LLM.content import Content


class ResumeOptimizer:
    def __init__(self, api_key, model_name="gpt-3.5-turbo") -> None:
        self.llm = ChatOpenAI(model_name=model_name, openai_api_key=api_key)
        self.prompt = ChatPromptTemplate.from_messages([
                        ("system", Content.system_prompt),
                        ("user",Content.user_prompt + "JOB DESCRIPTION :\n {description} \n\nINPUT RESUME :\n\n{resume}")
                    ])        
        self.chain = self.prompt | self.llm | StrOutputParser()
        
    def generate_resume(self,job_description,resume):
        self.output = self.chain.invoke({"description":job_description,"resume":resume})
        