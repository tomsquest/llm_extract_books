retry_policy RetryTwice {
  max_retries 2
}

client<llm> GPT4 {
  provider openai
  retry_policy RetryTwice
  options {
    model gpt-4
    api_key env.OPENAI_API_KEY
    temperature 0
  }
}

client<llm> GPT4o {
  provider openai
  retry_policy RetryTwice
  options {
    model gpt-4o
    api_key env.OPENAI_API_KEY
    temperature 0
  }
}

client<llm> ClaudeHaiku {
  provider anthropic
  retry_policy RetryTwice
  options {
    model claude-3-haiku-20240307
    api_key env.ANTHROPIC_API_KEY
    max_tokens 1000
    temperature 0
  }
}

client<llm> ClaudeSonnet {
  provider anthropic
  retry_policy RetryTwice
  options {
    model claude-3-5-sonnet-20240620
    api_key env.ANTHROPIC_API_KEY
    max_tokens 1000
    temperature 0
  }
}

client<llm> GeminiFlash {
  provider vertex-ai
  retry_policy RetryTwice
  options {
    model gemini-1.5-flash-001
    project_id env.GCP_PROJECT_ID
    location env.GCP_PROJECT_LOCATION
    credentials env.GCP_CREDENTIALS_FILE
    generationConfig {
      maxOutputTokens 1000
      temperature 0
    }
  }
}

client<llm> GeminiPro {
  provider vertex-ai
  retry_policy RetryTwice
  options {
    model gemini-1.5-pro-001
    project_id env.GCP_PROJECT_ID
    location env.GCP_PROJECT_LOCATION
    credentials env.GCP_CREDENTIALS_FILE
    generationConfig {
      maxOutputTokens 1000
      temperature 0
    }
  }
}