
import json
import logging
from app.fetch_web_post import scrape_website
from app.prompt import gen_summary

def summary_handle(url: str, req_id=None) -> dict:
    # 爬取内容
    content = scrape_website(url)
    logging.info(content)
    # 提取摘要
    result = gen_summary(content)
    result = json.loads(result)
    logging.info(result)
    
    # 结果处理
    r_dict = {
        "code": 0,
        "data": {},
        "req_id": req_id
    }
    if 'summary' in result and result['summary']:
        r_dict['data']['summary'] = result['summary']
    if 'key_points' in result and len(result['key_points']) > 0:
        r_dict['data']['key_points'] = result['key_points']
        
    return r_dict
