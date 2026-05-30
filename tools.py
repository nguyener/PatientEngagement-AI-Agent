import uuid
from store import patients, insurance_records, appointments


def register_patient(full_name, dob, phone, email):
    patient_id = str(uuid.uuid4())[:8]
    patients[patient_id] = {
        "patient_id": patient_id,
        "full_name": full_name,
        "dob": dob,
        "phone": phone,
        "email": email
    }
    return {"success": True, "message": f"Registered successfully. Patient ID: {patient_id}"}


def update_insurance(patient_id, provider, member_id, group_number):
    if patient_id not in patients:
        return {"success": False, "message": "Patient ID not found."}

    insurance_records[patient_id] = {
        "provider": provider,
        "member_id": member_id,
        "group_number": group_number
    }
    return {"success": True, "message": "Insurance updated successfully."}


def schedule_appointment(patient_id, date, time, provider):
    if patient_id not in patients:
        return {"success": False, "message": "Patient ID not found."}

    appointment_id = str(uuid.uuid4())[:8]
    appointments[appointment_id] = {
        "appointment_id": appointment_id,
        "patient_id": patient_id,
        "date": date,
        "time": time,
        "provider": provider,
        "status": "scheduled"
    }
    return {"success": True, "message": f"Appointment scheduled. Appointment ID: {appointment_id}"}


def cancel_appointment(appointment_id):
    if appointment_id not in appointments:
        return {"success": False, "message": "Appointment ID not found."}

    appointments[appointment_id]["status"] = "cancelled"
    return {"success": True, "message": "Appointment cancelled successfully."}


def reschedule_appointment(appointment_id, new_date, new_time):
    if appointment_id not in appointments:
        return {"success": False, "message": "Appointment ID not found."}

    appointments[appointment_id]["date"] = new_date
    appointments[appointment_id]["time"] = new_time
    appointments[appointment_id]["status"] = "rescheduled"
    return {"success": True, "message": "Appointment rescheduled successfully."}


tool_functions = {
    "register_patient": register_patient,
    "update_insurance": update_insurance,
    "schedule_appointment": schedule_appointment,
    "cancel_appointment": cancel_appointment,
    "reschedule_appointment": reschedule_appointment,
}