from database import get_memories

def search_memory(user_query):

    memories = get_memories()

    user_query = user_query.lower()

    # Favourite color
    if "color" in user_query or "colour" in user_query:
        for memory in memories:
            if "favorite color" in memory.lower() or "favourite color" in memory.lower():
                return f"Your favourite color is {memory.split('is')[-1].strip()}."

    # Name
    if "name" in user_query:
        for memory in memories:
            if "my name is" in memory.lower():
                return f"Your name is {memory.split('is')[-1].strip()}."

    # Place
    if "live" in user_query:
        for memory in memories:
            if "i live in" in memory.lower():
                return f"You live in {memory.split('in')[-1].strip()}."

    return None