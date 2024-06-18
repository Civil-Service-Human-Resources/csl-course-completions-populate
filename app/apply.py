import json
import dao.reportingDAO
import logging

logging.basicConfig(filename='app.log', level=logging.INFO)

def apply():
    plan = json.loads(open("plan.json").read())

    confirmation = input(f"You are about to update {len(plan)} course completion rows. Are you sure? (Y/n): ")

    if confirmation == "Y":
        logging.info(f"Appling for {len(plan)} course completion events.")

        for event in plan:
            event_id = event["eventId"]
            updates = event["updates"]

            logging.info(f"Event with ID {event_id}:")
            logging.info(f" - {len(updates)} updates")

            for update in updates:
                row_name = update["row"]
                row_value = update["value"]
                
                dao.reportingDAO.set_row_value_for_event_id(row_name, row_value, event_id)

                logging.info(f"  - Updated {row_name}")