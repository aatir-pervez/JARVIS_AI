last_topic = None
conversation_history = []

MAX_HISTORY = 5

def set_topic(topic):
    global last_topic
    last_topic = topic

def get_topic():
    return last_topic


def add_to_memory(role, message):
    conversation_history.append({"role": role, "content": message})

    if len(conversation_history) > MAX_HISTORY:
        conversation_history.pop(0)

def get_memory():
    context = ""
    for chat in conversation_history:
        context += f"{chat['role']}: {chat['content']}\n"
    return context