import uuid

from openai import OpenAI

api_key_to_make_openapi_library_work = uuid.uuid4().hex
client = OpenAI(base_url="http://localhost:1234/v1", api_key=api_key_to_make_openapi_library_work)


def _retrieve_model_id():
    models = client.models.list()
    model_name = models.data[0].id
    return model_name


def _test_python_code():
    completion = client.chat.completions.create(
        model=_retrieve_model_id(),
        messages=[
            {
                "role": "user",
                "content": "How do I output all files in a directory using Python?",
            },
        ],
    )
    print(completion.choices[0].message.content)


def _test_is_python_code_playbook_compliant():
    system_message = """You are a judge that evaluates whether a given Python code snippet is compliant with the playbook. \
The playbook is a set of rules that define the best practices for writing Python code. \
The first line of your answer should be either "Yes" or "No". \
If the answer is "No", the second line should be a brief explanation of why the code is not compliant. \
The explanation should contain the rule number from the playbook."""
    playbook_rules = """The playbook contains the following rules:
1. Use 4 spaces per indentation level.
2. Limit all lines to a maximum of 79 characters.
3. Do not use wildcard imports.
4. Do not log complex objects directly."""
    user_input = """body = {}
logger.debug("The following is going to be sent: %s", body)"""
    completion = client.chat.completions.create(
        model=_retrieve_model_id(),
        messages=[
            {
                "role": "system",
                "content": system_message,
            },
            {
                "role": "user",
                "content": f"```{user_input}```",
            },
            {
                "role": "assistant",
                "content": playbook_rules,
            },
        ],
        temperature=0,
        max_tokens=1000,
    )
    print(completion.choices[0].message.content)


if __name__ == "__main__":
    _test_is_python_code_playbook_compliant()
