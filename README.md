# GenAI Samples

Sample GenAI code and use cases are based on the following sources:
- [Autogen Notebook](https://github.com/microsoft/autogen/tree/main/notebook) Samples
- [Matthew Berman's gist](https://gist.github.com/mberman84/ea207e7d9e5f8c5f6a3252883ef16df3?permalink_comment_id=4870649) covering Autogen integration with Open Source LLMs using LiteLLM

The objective is to compare the behavior of the Autogen Framework using GPT4 vs Open Source LLMs, using a set of Jupyter Notebooks originally created for the OpenAI models.

## Background Information on AutoGen, Ollama, and LiteLLM
- Check out Matthew Berman's YouTube videos For some great "getting started" content
- [AutoGen + Ollama Tutorial](https://youtu.be/y7wMTwJN7rA?si=6YmkOyoAabm700d2)
- [AutoGen Studio 2.0 Tutorial](https://www.youtube.com/watch?v=4ZqJSfV4818)

## Installation

- the [litellm.py](src/litellm.py) is helpful for initial validation of Python, LiteLLM, and Ollama dependencies

### Python Modules

```bash
pip install pyautogen
pip install 'litellm[proxy]'
pip install youtube_transcript_api
```

### LiteLLM Configuration

```bash
litellm --model ollama/llama2
litellm --model ollama/mistral
litellm --model ollama/codellama
litellm --model ollama/mixtral
litellm --model ollama/llava
```