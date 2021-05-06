def headline(text: str, align: bool = False) -> str:
  if align:
    return f"{text.title()}\n{'-' * len(text)}"
  else:
    return f" {text.title()} ".center(50, "o")

print(headline('hello world'))
print(headline.__annotations__)
print(__annotations__)