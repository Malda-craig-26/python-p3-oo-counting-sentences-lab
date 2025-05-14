#!/usr/bin/env python3

import re

class MyString:
  def __init__(self,value = ""):
    if isinstance(value,str):
      print("The value must be a string.")
      self.value = value 
    else:
        self.value = ""

  def is_sentence(self):
     return self.value.endswith(".")  

  def is_question(self): 
     return self.value.endswith("?") 
  
  def is_exclamation(self):
      return self.value.endswith("!")
  
  def count_sentences(self):
     sentences = re.split(r'[.?!]+(?=\s|$)', self.value)
     return len([s for s in sentences if s.strip()])
  
text = MyString("Hello! How are you? This is a test. Another sentence.")
print("Is sentence?",text.is_sentence())
print("Is question?",text.is_question()) 
print("Is exclamation?",text.is_exclamation())
print("Number of sentences:",text.count_sentences)

      
