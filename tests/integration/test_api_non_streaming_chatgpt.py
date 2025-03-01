#!/usr/bin/env python

from chatgpt_wrapper.backends.openai.api import OpenAIAPI
from chatgpt_wrapper.core.config import Config

def test_api_non_streaming():
    config = Config(profile='test')
    config.set('backend', 'chatgpt-api')
    config.set('debug.log.enabled', True)
    gpt = OpenAIAPI(config)
    success, response, user_message = gpt.ask("Say hello!")
    if success:
        print("\nRESPONSE:\n")
        print(response)
    assert success

if __name__ == '__main__':
    test_api_non_streaming()
