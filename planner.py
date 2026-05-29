from datetime import datetime, timedelta

def generate_plan(subjects, days, hours_per_day):

    study_plan = []

    start_date = datetime.today()

    hours_per_subject = hours_per_day / len(subjects)

    for i in range(days):

        current_day = start_date + timedelta(days=i)

        day_plan = {
            "date": current_day.strftime("%Y-%m-%d"),
            "tasks": []
        }

        for subject in subjects:
            day_plan["tasks"].append({
                "subject": subject,
                "hours": round(hours_per_subject, 1)
            })

        study_plan.append(day_plan)

    return study_plan