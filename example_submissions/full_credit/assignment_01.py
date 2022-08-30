"""
This is the first test assignment.
"""

def say_hello(prompt: str) -> str:
    """
    Please edit this function to return "Hello" if the prompt passed to it is either "Hello", "Hi", or "Greetings".
    This should not be case sensitive.
    Otherwise, this function should return "I'm sorry, I don't understand."
    """

    # Begin student code
    # This solution should get full credit
    print(f"Testing {prompt}")
    if prompt.lower() in ["hello","hi","greetings"]:
        print("I should say Hello")
        return "Hello"
    else:
        print("This is not something I should say Hello to")
        return "I'm sorry, I don't understand."