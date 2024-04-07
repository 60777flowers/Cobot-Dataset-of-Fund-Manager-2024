from openai import OpenAI


def get_chat_messages(prompt_text):
    client = OpenAI(
        api_key="sk-HpSfwZkjQXPYqvLsmn85spia4W075KYu0lX3mdFIayxJhyX5",
        base_url="https://api.chatanywhere.tech/v1"
    )
    chat_completion = client.chat.completions.create(
        messages=prompt_text,
        model="gpt-3.5-turbo",
    )
    return chat_completion.choices[0].message.content


conversation_history = []

while True:
    user_input = input("请输入您的问题（输入'退出'以结束）：")
    if user_input.lower() == '退出':
        break
    conversation_history.append({"role": "user", "content": user_input})
    response_content = get_chat_messages(conversation_history)
    conversation_history.append({"role": "assistant", "content": response_content})
    print(response_content)
