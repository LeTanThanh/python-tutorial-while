if __name__ == "__main__":
  # Introduction to the Python while statement

  """
  while condition:
    body
  """

  # Python while statement examples

  # 1) Simple Python while statement example

  max = 5
  counter = 0

  while counter < max:
    print(counter)
    counter += 1

  # 2) Using the Python while statement to build a simple command prompt program

  command = ""
  while command.lower() != "quit":
    command = input(">")
    print(f"Echo: ${command}")
