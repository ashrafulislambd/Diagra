# Diagra Backend
This is the backend for Diagra, a tool to generate diagrams and flowchart from natural language prompts. This is written using CrewAI, llama3, Django and Django REST Framework. (The frontend project is available at https://github.com/ashrafulislambd/Diagra-frontend)

# Requirements
Make sure you have installed latest version of **Python** and **Pip** on your computer

# Usage
Clone this into your local folder by running the following command,

`git clone https://github.com/ashrafulislambd/Diagra.git`

After that change into the directory and run the following commands to start your application

```bash
cd Diagra
pip install -r requirements.txt
```

The above command is required only the first time you run. From each of the next time you only run the following command,

`python manage.py runserver`

This will start the server on http://127.0.0.1:8000 

# API Endpoints

**GET** */article/?topic=<**topic_name**>*

It will generate a graphviz dot diagram on `topic_name` and return like this,

**Response**:

```json
{
    "output": "digraph {... diagram ...}"
}
```

# Team Members
* Md. Ashraful Islam - imdashraful17@gmail.com
* Zannatul Fedous Maliha - zannatulferdousmaliha6@gmail.com
* Md. Farhan Ishraq - farhanishraq777@gmail.com
* Abrar Mahmud Hasan - abrarhasan2003@gmail.com

# Special Thanks To #

* Python and it's awsome community
* CrewAI
* LangChain
* Llama3
* Graphviz
* All the people who helped testing, developing and improving the project.
* All the team members.
