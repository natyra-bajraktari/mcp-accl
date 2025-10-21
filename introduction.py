# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC #Databricks MCP Acclerator
# MAGIC
# MAGIC
# MAGIC This solution accelerator introduces different ways to integrate **Model Context Protocol (MCP)** and **Agents** within Databricks.  
# MAGIC Each section gives a short explanation of the approach and links to detailed examples or demo notebooks.  
# MAGIC Use this **introduction** notebook as your entry point to explore the different integration patterns.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### 1. Managed MCP with Agent on Databricks
# MAGIC
# MAGIC In this setup, an agent runs inside Databricks and uses MCPs that are managed by the platform.
# MAGIC This combines the reliability of managed MCPs with the flexibility of running your own agent workflows. Use the [managed-mcp-server]($./managed-mcp-server-notebook) notebook to get started. It will soon be also possible to export code directly from the Playground, making experimentation and deployment much smoother. 
# MAGIC
# MAGIC Additionally, you could also use Databricks Managed MCP servers i.e Genie, via external clients such as Claude Desktop. This way you'd be able to equip your agent with all the capabilities of Genie and leverage them through a standardized application interface such as Claude Desktop. To see how it works in practice, have a look at this [repo](https://github.com/alexxx-db/databricks-genie-mcp).

# COMMAND ----------

# MAGIC %md
# MAGIC ### 2. Custom MCP with Agent on Databricks
# MAGIC
# MAGIC In this section, we would like to extend the capabilities to our agent by building a custom MCP server, deployed via Databricks App. This way, the agent besides being able to derive insight from Genie as a managed MCP server in Databricks, we want to make it capable of also quantifying a patient’s health risk by calling a risk API. The agent would be also capable to retrieve recent lab results from an external source. Use the [custom-mcp-server-notebook]($./custom-mcp-server-notebook) to get started.

# COMMAND ----------

# MAGIC %md
# MAGIC ### 3. Add your MCP servers in your agent code
# MAGIC
# MAGIC If you would like to see how you can wrap your MCP servers as tools in your agent code, in our example we have been using both Genie as a Databricks managed MCP server and our custom MCP server hosted via Databricks Apps, then referr to the [langgraph-mcps-agents]($./langgraph-mcps-agent) notebook. Additionally, in the future you'd be also able to export the code from the AI playground.

# COMMAND ----------

# MAGIC %md
# MAGIC ### 4. External MCP with Agent on Databricks
# MAGIC
# MAGIC In this setup, the agent connects to an MCP server that is hosted **outside of Databricks**. You can register the external MCP in the UI and make it available to your agent without writing code. This allows you to integrate existing services or partner APIs directly into your agent workflows. Use the [external-mcp-server-notebook]($./external-mcp-server-notebook) to get started.
