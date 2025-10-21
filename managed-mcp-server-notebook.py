# Databricks notebook source
# MAGIC %md
# MAGIC #Managed MCP servers in Databricks
# MAGIC
# MAGIC MCP servers are like connectors that allow AI agents to use outside data and tools. With Databricks, you don’t need to build these connections yourself — the managed MCP servers let your agents quickly plug into Unity Catalog data, vector search, and custom functions. Please refer in our [documentation page](https://docs.databricks.com/aws/en/generative-ai/mcp/managed-mcp) to find out more about managed mcp servers available in Databricks.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ## 0. Get started with the Genie MCP managed servers in Databricks
# MAGIC
# MAGIC In this accelerator, we’ll work with a healthcare dataset to show how agents and Genie as a Databricks managed MCP server can be applied in practice. We’ll use [Genie](https://docs.databricks.com/aws/en/genie/) inside Databricks to explore the data, ask questions in natural language, and quickly generate insights. This example illustrates how MCP-powered agents can help domain experts interact with complex datasets without writing from scratch these capabilities.
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## 1. Create a Genie space in Databricks
# MAGIC
# MAGIC In order to get started first you need to create your Genie space in your Databricks Workspace. To setup your Genie workspace, refer to the [documentation](https://docs.databricks.com/aws/en/genie/set-up#-create-a-genie-space). To make sure your Genie space is setup with the best practices, have a look [here](https://docs.databricks.com/gcp/en/genie/best-practices). In our example we have setup our genie space as below:<br><br>
# MAGIC
# MAGIC
# MAGIC <img src="https://github.com/natyra-bajraktari/mcp-accl/blob/main/img/genie-space.png?raw=true" style="width: 800px; margin-left: 10px">
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. Use the Genie MCP server in your agent code. 
# MAGIC
# MAGIC In Databricks you can build agents in the framework of your choice. In our example we have used LangGraph to build the agent in the Databricks [Mosaic AI framework](https://docs.databricks.com/aws/en/generative-ai/agent-framework/create-agent) and expose the Genie capabilities from the managed MCP server. For the managed Databricks MCP servers, you would just need to put the specific managed MCP server url, in our case we would need to put the url of the Genie space we have created.  Below, we're showing how you can immdeately test the managed MCP server such Genie in AI Playground with a model endpoint of your choice. Since at the moment the code cannot be exported, to see how you'd include it in code, check the [mcp-tool-call-agent](url) notebook.
# MAGIC

# COMMAND ----------

# MAGIC %pip install databricks-mcp databricks-langchain uv langgraph==0.3.4
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ## Test the Genie MCP server in AI Playground
# MAGIC
# MAGIC Test the Databricks Genie MCP server directly in the Databricks [AI Playground](https://docs.databricks.com/aws/en/large-language-models/ai-playground#use-ai-playground). You would just need to add your Genie space and then start asking questions using the model endpoint of your choice. In future, you'd be able to also export the notebook code from the playground as normally is possible for non-MCP agentic applications. Additionally, you could also expose the Genie capabilities to external client application such as Claude Desktop. To see how is this done, you could follow the instructions explained [here](https://github.com/alexxx-db/databricks-genie-mcp).

# COMMAND ----------

# MAGIC %md
# MAGIC <img src="https://github.com/natyra-bajraktari/mcp-accl/blob/main/img/playground-1.png?raw=true" style="width: 800px; margin-left: 10px">
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Then start asking questions.

# COMMAND ----------

# MAGIC %md
# MAGIC <img src="https://github.com/natyra-bajraktari/mcp-accl/blob/main/img/playground-2.png?raw=true" style="width: 800px; margin-left: 10px">
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Additionally, you could also inspect the View Trace option after each response to see how is the tool calling being made.

# COMMAND ----------

# MAGIC %md
# MAGIC <img src="https://github.com/natyra-bajraktari/mcp-accl/blob/main/img/playground-3.png?raw=true" style="width: 800px; margin-left: 10px">
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ## UC functions as tools or MCP server tools?
# MAGIC
# MAGIC You might be wondering when you would be using [UC functions](https://docs.databricks.com/aws/en/udf/unity-catalog) or using Databricks managed MCP servers. Both of them being very important to provide capabilities to your agents, UC function would be defintely recommend if you know in advance what functions your agent needs and you are building them complelety in databricks, this way bring all the governance benefits that UC funtions powered by Unity Catalog bring. However if you building a multi-agentic system and you need to share the capabilities across either coming from Databricks Managed MCP servers or you need to do some additional external API calls (custom MCPs) then exposing these as tools in a MCP server would be very efficient for your agentic system.
