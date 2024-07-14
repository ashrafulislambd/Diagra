import urllib.request
from langchain_groq import ChatGroq
import urllib


from langchain_community.llms.ollama import Ollama
from crewai import Agent, Task, Crew

llama3 = ChatGroq(temperature=0,
                  model="llama3-70b-8192",
                  api_key="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")
topic_explainer = Agent(
    role = "Senior Explainer",
    goal = """You will be prompted on a certain topic or subject 
        and you will have to explain the processes or steps of it""",
    backstory = """
        A topic/subject will be provided to you. And you will create
        step by step processes or information about how it works. It should
        be a good explainer.
    """,
    allow_delegation = False,
    verbose = True,
    llm = llama3,
)

explain_topic = Task(
    description = "Explain the topic provided by the prompt {prompt}",
    expected_output = "Step by step explanation or process that is easy to understand",
    agent = topic_explainer
)

diagram_creator = Agent(
    role = "Expert Diagram Creator",
    goal = "You will be given process about certain topic"
        " and you will create diagram from that",
    backstory = """
        A diagram need to be generated on a certain topic.
        How it happens, or it's processes will be explained to
        you and you will create a GraphViz dot diagram from that
    """,
    allow_delegation = False,
    verbose = True,
    llm = llama3,
)

create_diagram = Task(
    description = "Generate diagram from the explanation provided by the Senior Explainer",
    expected_output = "The diagram in graphviz dot language without any additional text. Even not beginning and ending with ``` and ```. Completely raw graphviz dot language code",
    agent = diagram_creator
)

crew = Crew(
    agents=[topic_explainer, diagram_creator],
    tasks=[explain_topic, create_diagram],
)

pagebody = urllib.request.urlopen("https://www.daraz.com.bd/#hp-just-for-you").read()

def get_diagram(topic):
    return crew.kickoff(inputs={
        "prompt": topic
    })