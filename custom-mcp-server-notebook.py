# Databricks notebook source
# MAGIC %md
# MAGIC # Custom MCP servers in Databricks
# MAGIC
# MAGIC Besides the already available managed Databricks MCP servers that you could use to expose different capabilities to your agents as shown in [managed-mcp-server-notebook]($./managed-mcp-server-notebook), you could also create your own MCP servers with your own tools and host them in Databricks using Databricks Apps. These are known as [custom MCP servers](https://docs.databricks.com/aws/en/generative-ai/mcp/custom-mcp).

# COMMAND ----------

# MAGIC %md
# MAGIC ## Get started with custom MCP servers
# MAGIC
# MAGIC To host your own MCP server in Databricks, you should be acquanted with [Databricks Apps](https://learn.microsoft.com/en-us/azure/databricks/dev-tools/databricks-apps/) that enables users securely and efficiently deploy apps in Databricks, by providing all the compute and governance capabiltiies of the platform . To get started with the Databricks apps, for our example we have been following the steps from [here](https://docs.databricks.com/aws/en/generative-ai/mcp/custom-mcp#host-an-mcp-server-as-a-databricks-app), by creating the [three main files]($./mcp-custom-server) neccessary for the Databricks Apps: 
# MAGIC
# MAGIC - app.yaml - specifying the CLI command to run your server.
# MAGIC - requirements.txt - adding all your Python dependencies to the server
# MAGIC - server.py - adding all your custom code for your tools
# MAGIC
# MAGIC Then to deploy it to the Databricks Apps, you could either use the [command line](https://docs.databricks.com/aws/en/generative-ai/mcp/custom-mcp#upload-the-mcp-server-as-a-databricks-appr) or the [UI](https://learn.microsoft.com/en-us/azure/databricks/dev-tools/databricks-apps/get-started) and point to the directory with these files.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Our example
# MAGIC
# MAGIC In our example we are using a healthcare dataset and we are using Genie already hosted as a managed MCP server in Databricks to explorate the dataset and derive insights, as we have shown in [managed-mcp-server-notebook]($./managed-mcp-server-notebook). Further, we want to extend the capabilities of our agentic system by making the agent capable of quantifying a patient’s health risk by calling a risk API. The agent would be capable to retrieve recent lab results from an external source. Lastly, the agent would be also able to schedule a patient’s appointment with a scheduler system. These capabilities are provided as tools in our [server.py]($./mcp-custom-server/server.py) for our custom MCP server.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Test the custom MCP server in the AI Playground
# MAGIC
# MAGIC In order to test our agentic system with the capabilties provided in our custom MCP server as well as already available Databricks managed MCP server, we will be using the AI playground to see how is our system working. In the future, you'd be able to also export the notebook code with the MCP servers. In case you'd like to see how this would look like in code, use the [langgraph-mcps-agent]($./langgraph-mcps-agent) notebook.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC First, we need to add our MCP servers as tools:

# COMMAND ----------

# MAGIC %md
# MAGIC <img src="https://github.com/natyra-bajraktari/mcp-accl/blob/main/img/playground-4.png?raw=true" style="width: 800px; margin-left: 10px">

# COMMAND ----------

# MAGIC %md
# MAGIC To make sure, that the model is recognizing the tools from the MCP servers provided, we can ask the model to list all the tools available. Additionally, we can also view the trace to see how the call is being made.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC <img src="https://github.com/natyra-bajraktari/mcp-accl/blob/main/img/playground-5.png?raw=true" style="width: 800px; margin-left: 10px">
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Then you can continue asking questions and inspect the calls being made:

# COMMAND ----------

# MAGIC %md
# MAGIC <img src="https://github.com/natyra-bajraktari/mcp-accl/blob/main/img/playground-6.png?raw=true" style="width: 800px; margin-left: 10px">
# MAGIC
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Below, we can see the trace that the model takes to recognize the tools and get the neccessary information on responding the question:
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC <img src="https://github.com/natyra-bajraktari/mcp-accl/blob/main/img/playground-7.png?raw=true" style="width: 800px; margin-left: 10px">
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Agent with MCP servers in code
# MAGIC
# MAGIC Though in the future, you'd be able to export the code for the interactions above in AI playground with the MCP servers as tools as well, if you would like to see how you can wrap your MCP servers in code, please refer to this [langgraph-mcps-agent]($./langgraph-mcps-agent).
