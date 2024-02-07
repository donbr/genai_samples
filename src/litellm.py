import autogen

# requires 2 litellm endpoints to be running
# refer to README.md for more information
config_list_mistral = [
    {
        'model': "ollama/mistral",
        'base_url': "http://0.0.0.0:8000",
        'api_key': "NULL"
    }
]

config_list_codellama = [
    {
        "model": "ollama/codellama",
        'base_url': "http://0.0.0.0:10704",
        'api_key': "NULL"
    }
]

llm_config_mistral={
    "config_list": config_list_mistral,
}

llm_config_codellama={
    "config_list": config_list_codellama,
}

coder = autogen.AssistantAgent(
    name="Coder",
    llm_config=llm_config_codellama
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir": "web"},
    llm_config=llm_config_mistral,
    system_message="""Reply TERMINATE if the task has been solved to full satisfaction.
Otherwise, reply CONTINUE, or the reason why the task is not solved yet."""
)

task="""
Write a python script to output numbers 1 to 100 and then the user_proxy agent should run the script
"""

user_proxy.initiate_chat(coder, message=task)