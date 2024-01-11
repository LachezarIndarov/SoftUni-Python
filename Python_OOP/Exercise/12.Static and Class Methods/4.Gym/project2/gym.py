from project2.customer import Customer
from project2.equipment import Equipment
from project2.exercise_plan import ExercisePlan
from project2.subscription import Subscription
from project2.trainer import Trainer

class Gym:

    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer in self.customers:
            return
        self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer in self.trainers:
            return
        self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment in self.equipment:
            return
        self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan in self.plans:
            return
        self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription in self.subscriptions:
            return
        self.subscriptions.append(subscription)

    @staticmethod
    def __find_by_id(entities, entity_id):
        for entity in entities:
            if entity.id == entity_id:
                return entity

    def subscription_info(self, subscription_id):
        result = repr(self.__find_by_id(self.subscriptions, subscription_id)) + "\n"
        result += repr(self.__find_by_id(self.customers, subscription_id)) + "\n"
        result += repr(self.__find_by_id(self.trainers, subscription_id)) + "\n"
        result += repr(self.__find_by_id(self.equipment, subscription_id)) + "\n"
        result += repr(self.__find_by_id(self.plans, subscription_id)) + "\n"

        return result.strip()