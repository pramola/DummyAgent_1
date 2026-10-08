from langchain_community.utilities import SearxSearchWrapper #this is an old module and not runnable
from langchain_community.tools import SearxSearchRun #this is a BaseTool implementation and is runnable

# Connect to your local SearxNG instance 
#searxNG is hosted upon docker and you need to pull that docker instance & update the settings.yml file
#settings.yml is the configuration to allow json output rather than html
search = SearxSearchWrapper(searx_host="http://localhost:8888")


tool = SearxSearchRun(wrapper=search)

# Now you have the full Runnable interface:
result = tool.invoke("what is langchain")   # ✅
print(result)
result = tool.batch(["query1", "query2"])   # ✅
print(result)

# Test the connection
results = search.run("Top 5 pc games of 2026")
print(results)   