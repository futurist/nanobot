def split_tool_call_id(item_id, tool_call_data):
    if item_id:
        return item_id
    else:
        # Create a unique hash from the tool call data to ensure deterministic IDs
        return hash(tuple(tool_call_data.items()))

# In the convert_messages function:
# Replace the old ID generation logic with:
"id": item_id or split_tool_call_id(None, tool_call_data)
