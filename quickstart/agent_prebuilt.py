from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import math
import os

load_dotenv(".env")


def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

def plus(num1: int, num2: int) -> int:
    """Function that returns the sum of two numbers"""
    return num1 + num2

def multiply(num1: int, num2: int) -> int:
    """A function that returns the product of two numbers"""
    return num1 * num2

def minus(num1: int, num2: int) -> int:
    """Function that returns the difference of two numbers"""
    return num1 - num2

def divide(num1: int, num2: int) -> float:
    """Function that returns the division of two numbers"""
    if num2 == 0:
        raise ValueError("Cannot divide by zero.")
    return num1 / num2

def power(num1: int, num2: int) -> int:
    """Function that returns the result of num1 raised to the power of num2"""
    return num1 ** num2

def modulo(num1: int, num2: int) -> int:
    """Function that returns the remainder of division of two numbers"""
    if num2 == 0:
        raise ValueError("Cannot divide by zero.")
    return num1 % num2

def floor_division(num1: int, num2: int) -> int:
    """Function that returns the floor division result of two numbers"""
    if num2 == 0:
        raise ValueError("Cannot divide by zero.")
    return num1 // num2

def sqrt(num: int) -> float:
    """Function that returns the square root of a number"""
    if num < 0:
        raise ValueError("Cannot take square root of negative number.")
    return math.sqrt(num)

def absolute(num: int) -> int:
    """Function that returns the absolute value of a number"""
    return abs(num)

def gcd(num1: int, num2: int) -> int:
    """Function that returns the greatest common divisor of two numbers"""
    return math.gcd(num1, num2)

def lcm(num1: int, num2: int) -> int:
    """Function that returns the least common multiple of two numbers"""
    return math.lcm(num1, num2)

def factorial(num: int) -> int:
    """Function that returns the factorial of a number"""
    if num < 0:
        raise ValueError("Cannot take factorial of negative number.")
    return math.factorial(num)


llm = ChatOpenAI(
        model="gpt-4o-mini",
        # **params
    )

agent = create_react_agent(
    # model=llm,
    model="anthropic:claude-3-7-sonnet-latest",
    # tools=[get_weather, plus, multiply, minus, divide, power, modulo, floor_division, sqrt, absolute, gcd, lcm, factorial],
    tools=[],
    prompt="You are a helpful assistant. Respond in Korean."
)

# Run the agent
# question = "수원 날씨 어때?"
# question = "내가 처음에 120개 사과를 가지고 있었는데 20%를 남기고 모두 지인들에게 나눠줬어. 그다음 3개를 내가 먹었어. 지인들이 감사하게도 배를 5개 내게 줬어. 현재 내가 가지고 있는 과일은 각각 몇개일까?"
question = ""
res = agent.invoke(
    {"messages": [{"role": "user", "content": question}]}
)
# print(f"q: {question}")
# print(f"a: {res}")

messages = res["messages"]

for msg in messages:
    print(f"msg: {msg.content}")