def ask_question(question):

    prompt = f"""
You are an HR AI assistant conducting an exit interview.

Ask the employee the following question clearly and politely.

Question:
{question}
"""

    return prompt
