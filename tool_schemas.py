tools = [
    {
        "type": "function",
        "name": "register_patient",
        "description": "Register a new patient.",
        "parameters": {
            "type": "object",
            "properties": {
                "full_name": {"type": "string"},
                "dob": {"type": "string"},
                "phone": {"type": "string"},
                "email": {"type": "string"}
            },
            "required": ["full_name", "dob", "phone", "email"],
            "additionalProperties": False
        }
    },
    {
        "type": "function",
        "name": "update_insurance",
        "description": "Add or update insurance.",
        "parameters": {
            "type": "object",
            "properties": {
                "patient_id": {"type": "string"},
                "provider": {"type": "string"},
                "member_id": {"type": "string"},
                "group_number": {"type": "string"}
            },
            "required": ["patient_id", "provider", "member_id", "group_number"],
            "additionalProperties": False
        }
    },
    {
        "type": "function",
        "name": "schedule_appointment",
        "description": "Schedule appointment.",
        "parameters": {
            "type": "object",
            "properties": {
                "patient_id": {"type": "string"},
                "date": {"type": "string"},
                "time": {"type": "string"},
                "provider": {"type": "string"}
            },
            "required": ["patient_id", "date", "time", "provider"],
            "additionalProperties": False
        }
    },
    {
        "type": "function",
        "name": "cancel_appointment",
        "description": "Cancel appointment.",
        "parameters": {
            "type": "object",
            "properties": {
                "appointment_id": {"type": "string"}
            },
            "required": ["appointment_id"],
            "additionalProperties": False
        }
    },
    {
        "type": "function",
        "name": "reschedule_appointment",
        "description": "Reschedule appointment.",
        "parameters": {
            "type": "object",
            "properties": {
                "appointment_id": {"type": "string"},
                "new_date": {"type": "string"},
                "new_time": {"type": "string"}
            },
            "required": ["appointment_id", "new_date", "new_time"],
            "additionalProperties": False
        }
    }
]