import json
from watson_developer_cloud import ConversationV1
import ast


Backend_apis = {}
Backend_apis['node_8_1480632213867'] = 'get_next_quiz_date'

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

  def get_next_quiz_date(self):
    return "date"


def Backendhandler(user_name,intent, entity,node):
   
   #Handler = AIBackend(user_name = user_name,intent = intent, entity = entity,node = node)
   function_name = Backend_apis[node] 
   Handler = AIBackend(user_name)
   response =  getattr(Handler, function_name)()
   return response



