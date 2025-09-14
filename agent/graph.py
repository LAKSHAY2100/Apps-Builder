from langchain_groq import ChatGroq
from pydantic import BaseModel,Field
import os
from dotenv import load_dotenv
from prompt import *

load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
llm=ChatGroq(model="openai/gpt-oss-120b")

user_prompt="Create a calculator web application?"
prompt=planner_prompt(user_prompt)


class File(BaseModel):
    path:str = Field(description="The path of the file to be created"),
    purpose:str = Field(description="The purpose of the file to be created , e.g. 'main app logic' , 'data processing module' , etc")


class Plan(BaseModel):
    name: str = Field(description="The name of the app to be built")
    description: str = Field(description="A oneline description of the app to be built")
    tech_stack: str = Field(description="The technology stack to be used to build the app eg:python,javascript,react,flask,etc")
    features: list[str] = Field(description="A list of features of that app should have e.g. 'user authentication,data visualization ,etc'")
    files: list[File] = Field(description="A list of files that should be created in the app , each with a path and purpose")

resp= llm.with_structured_output(Plan).invoke(prompt)


print(resp)