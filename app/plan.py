import dao.reportingDAO
import dao.csrsDAO
import json
import logging

logging.basicConfig(filename='app.log', level=logging.INFO)

def plan():
    logging.info("Starting preparing plan...")

    orgs = dao.csrsDAO.get_all_organisation_ids_and_abbreviations()
    profs = dao.csrsDAO.get_all_profession_ids_and_names()
    grades = dao.csrsDAO.get_all_grade_ids_and_code()

    course_completion_events = dao.reportingDAO.get_all_completion_events()

    plan = []

    logging.info(f"Creating a plan for {len(course_completion_events)} course completion events...")

    for event in course_completion_events:
        logging.info("Creating plan for event with ID " + str(event["eventId"]))
        event_plan = {
            "eventId": event["eventId"],
            "updates": []
        }

        if event["organisation_abbreviation"] == None:
            organisation_abbreviation = next(organisation["abbreviation"] for organisation in orgs if organisation["id"] == event["organisationId"])
            event_plan["updates"].append({
                "row": "organisation_abbreviation",
                "value": organisation_abbreviation
            })
            logging.info("  - Added organisation_abbreviation update to the plan.")

        if event["profession_name"] == None:
            profession_name = next(profession["name"] for profession in profs if profession["id"] == event["professionId"])
            event_plan["updates"].append({
                "row": "profession_name",
                "value": profession_name
            })
            logging.info("  - Added profession_name update to the plan.")

        if event["grade_code"] == None:
            grade_code = next((grade["code"] for grade in grades if grade["id"] == event["gradeId"]), None)
            event_plan["updates"].append({
                "row": "grade_code",
                "value": grade_code
            })
            logging.info("  - Added grade_code update to the plan.")
            

        plan.append(event_plan)

    with(open("plan.json", "w")) as plan_file:
        plan_file.write(json.dumps(plan))