@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=40  4, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]
    
    # Validate student is not already signed up
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student is already signed up")
        # Example activities data structure (add more activities as requested)
        if not hasattr(signup_for_activity, "activities_initialized"):
            activities.update({
                "soccer": {"type": "sport", "participants": []},
                "basketball": {"type": "sport", "participants": []},
                "painting": {"type": "artistic", "participants": []},
                "music": {"type": "artistic", "participants": []},
                "chess": {"type": "intellectual", "participants": []},
                "debate": {"type": "intellectual", "participants": []},
            })
            signup_for_activity.activities_initialized = True
    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}    