library(ellmer)

chat <- chat_anthropic()
chat$set_system_prompt(
  interpolate_file("prompt.md", role = "Yoda")
)
chat$get_system_prompt()
