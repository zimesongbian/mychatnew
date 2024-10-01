from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class ActionOrderFood(Action):
    def name(self):
        return "action_order_food"

    def run(self, dispatcher, tracker, domain):
        food = tracker.get_slot('food')
        dispatcher.utter_message(text=f"Ordering {food} for you!")
        return [SlotSet('food', None)]
