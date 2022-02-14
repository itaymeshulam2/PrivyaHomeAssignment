from flask import Flask, request,jsonify
import re
from math import floor
from flask_cors import CORS


def solve(s):
    s = list(s[::-1])
    ans = get_term(s)
    while s:
      op, term = s.pop(), get_term(s)
      if op == "+":
        ans += term
      else:
        ans -= term
    return ans 

def get_value(s):
  sign = 1
  if s and s[-1] == "-":
     s.pop()
     sign = -1
  value = 0
  while s and s[-1].isdigit():
    value *= 10
    value += int(s.pop())
  return sign * value

def get_term(s):
  term = get_value(s)
  while s and s[-1] in "*/":
    op = s.pop()
    value = get_value(s)
    if op == "*":
      term *= value
    else:
      term = floor(1.0 * term / value)
  return term



def calculate_recursion(formula):
 
  next_start = formula.find('A')
  if(next_start == -1):
    return str(solve(formula))

  count = 1
  for i in range(next_start + 1,len(formula)):
    if formula[i] == 'A':
      count+=1
    elif formula[i] == 'Z':
      count-=1
      if(count == 0):
        return  calculate_recursion(formula[:next_start] + calculate_recursion(formula[next_start + 1:i]) +  formula[i + 1:])


def chek_if_string_is_valid(formula):
  #Check if all characters are valid  
  x = re.findall("[^0-9+-/*AZ]",formula)
  if len(x) > 0:
    return False
  
  #Check if all brackets are valid 
  brackets_stack = []
  for i in formula:
    if i == 'A':
      brackets_stack.append('A')
    if i == 'Z':
      brackets_stack.pop()
  if(len(brackets_stack)) > 0:
    return False

  return True



app = Flask(__name__)
CORS(app)

@app.route('/calculator', methods=["GET"])
def getResult():
    
    calculate = request.args.get("calculate", None)

    if(chek_if_string_is_valid(calculate)):
      result = jsonify({'result' : calculate_recursion(calculate)}) 
    else:
      result = jsonify({'result' : 'Input not valid'})
    # Enable Access-Control-Allow-Origin
    result.headers.add("Access-Control-Allow-Origin", "*")
    return result

if __name__ == "__main__":
    app.run(debug=True)