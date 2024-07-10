import logging
from llama_index.prompts.prompts import QuestionAnswerPrompt

QUESTION_ANSWER_PROMPT_TMPL_CN = (
    "上下文信息如下所示： \n"
    "---------------------\n"
    "{context_str}"
    "\n---------------------\n"
    "我的问题是：{query_str}\n"
)

QUESTION_ANSWER_PROMPT_TMPL_EN = (
    "Context information is below. \n"
    "---------------------\n"
    "{context_str}"
    "\n---------------------\n"
    "My question is {query_str}\n"
)

def get_prompt_template(language='zh'):
    if language == 'en':
        logging.info('=====> Use English prompt template!')
        return QuestionAnswerPrompt(QUESTION_ANSWER_PROMPT_TMPL_EN)
    else:
        logging.info('=====> Use Chinese prompt template!')
        return QuestionAnswerPrompt(QUESTION_ANSWER_PROMPT_TMPL_CN)

SUMMARY_PROMPT_CN = """
# 角色
你是一位阅读理解大师，精于总结翻译内容的主旨和关键点，提供清晰的内容概览。

# Output Format (JSON)
{
  "summary": "<总结>",
  "key_points": ["要点1", "要点2"]
}

# 工作流程
生成总结：不超过 200 个字，一句话准确的对原文全部内容进行概述。
关键信息列举：明确列出翻译内容的关键信息。
"""

SUMMARY_PROMPT_EN = """
# Role
You are a reading comprehension master, skilled at summarizing and translating the main idea and key points of content, providing a clear overview.

# Output Format (JSON)
{
  "summary": "<Summary>",
  "key_points": ["Key Point 1", "Key Point 2"]
}

# Workflow
Generate Summary: In no more than 200 words, provide a one-sentence accurate overview of the entire content.
List Key Points: Clearly enumerate the key information of the translated content.
"""

def get_openai_client():
    import os
    from openai import OpenAI
    
    return OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

def gen_summary(content: str, model: str = "gpt-3.5-turbo", language: str = "cn") -> dict:
    openai_client = get_openai_client()
    
    prompt = SUMMARY_PROMPT_CN if language == "cn" else SUMMARY_PROMPT_EN

    messages = [
        {
            "role": "system",
            "content": prompt
        },
        {
            "role": "user",
            "content": content
        }
    ]

    completion = openai_client.chat.completions.create(
        model=model,
        messages=messages,
        response_format={"type": "json_object"}
    )
    
    return completion.choices[0].message.content

# 示例用法
# result = gen_summary("文章标题", "这里是文章的内容", model="gpt-3.5-turbo-0125", language="cn")
# print(result)

