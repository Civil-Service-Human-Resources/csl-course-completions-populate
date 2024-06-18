from dao import reportingDAO
import json
import logging

logging.basicConfig(filename='app.log', level=logging.INFO)
def revert():
    plan = json.loads(open("plan.json").read())

    logging.info(f"Reverting updates for {len(plan)} rows.")
    
    for event in plan:
        event_id = event["eventId"]
        updates = event["updates"]
        row_names = [update["row"] for update in updates]
        
        for row_name in row_names:
            reportingDAO.set_row_value_for_event_id(row_name, None, event_id)

        logging.info(f"Reverted update for event with ID: {event_id}")
        
