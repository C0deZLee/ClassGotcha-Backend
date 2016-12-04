import json
from watson_developer_cloud import ConversationV1
import ast


Backend_apis = {}
Backend_apis['node_10_1480632588841'] = 'get_next_date'
Backend_apis['node_6_1480624843769'] = 'get_next_date'
Backend_apis['node_4_1480624787256'] = 'get_next_date'
Backend_apis['node_5_1480624810822'] = 'get_next_date'
Backend_apis['node_1_1480624710459'] = 'get_schedule_for_today'
Backend_apis['node_16_1480800992131'] = 'get_document_for_course'
Backend_apis['node_11_1480800130206'] = 'get_document_for_course'
Backend_apis['node_20_1480801214514'] = 'book_a_place'
Backend_apis['node_19_1480801185469'] = 'order_food'
Backend_apis['node_17_1480801109168'] = 'find_study_group'
Backend_apis['node_21_1480825496553'] = 'register_a_course'


def run(message=None,context=None):
    conversation = ConversationV1(
      username='28f2a25a-38d1-4f3e-9d02-391bb41edbde',
      password='PEb7dCc2jGrB',
      version='2016-09-20'
    )

    # Replace with the context obtained from the initial request
    if context == None:
        context = {}
    else:
        d = ast.literal_eval(json.dumps(context))
        context = d
    
    	

    workspace_id = 'f663996e-4c77-4b64-b188-5f10ebbbb27b'

    response = conversation.message(
      workspace_id=workspace_id,
      message_input={'text': message},
      context=context
    )

    #return(json.dumps(response, indent=2))
    return response

class AIBackend():
  
  def __init__(self,user_name):
    self.user_name = user_name
    #self.intent = intent
    #self.entity = entity
    #self.node = node
    return 

  def get_next_date(self,intent,entity):

    if entity[0]=="Exam":
      return entity[0]
    elif entity[0]=="lab":
      return entity[0]
    elif entity[0]=="quiz":
      return entity[0]
    elif entity[0]=="homework":
      return entity[0]
    else:

      return entity[0]

  def get_schedule_for_today(self,intent,entity):

    return intent

  def get_document_for_course(self,intent,entity):

    if entity[1]=="syllabus":
      return entity[0],intent
    elif entity[1] =="note":
      return entity[0],intent

  def find_study_group(self,intent,entity):
    # the course is entity[0]
    return entity[0]
    
  def order_food(self,intent,entity):
    # the restaurant is entity[0]
    return entity[0]

  def book_a_place(self,intent,entity):
    
    return "I will book a place for you"

  def register_a_course(self,intent,entity):

    return entity[0]


def Backendhandler(user_name,intent, entity,node):
   
   #Handler = AIBackend(user_name = user_name,intent = intent, entity = entity,node = node)
   function_name = Backend_apis[node] 
   Handler = AIBackend(user_name)
   response =  getattr(Handler, function_name)(intent,entity)
   return response



