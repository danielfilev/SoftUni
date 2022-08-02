from abc import ABC, abstractmethod
import time

# This is a test exercise of the Interface Segregation Principle.


class Workable(ABC):

    @abstractmethod
    def work(self):
        pass


class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass


class Worker(Workable, Eatable):

    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")
        time.sleep(5)


class SuperWorker(Workable, Eatable):

    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")
        time.sleep(3)


class Manager(ABC):

    def __init__(self):
        self.worker = None

    @abstractmethod
    def set_worker(self, worker):
        pass


class WorkManager:

    def set_worker(self, worker):
        assert isinstance(
            worker, Workable), "`worker` must be of type {}".format(Workable)

        self.worker = worker

    def manage(self):
        self.worker.work()


class BreakManager:

    def set_worker(self, worker):
        assert isinstance(
            worker, Eatable), "`worker` must be of type {}".format(Eatable)

        self.worker = worker

    def lunch_break(self):
        self.worker.eat()


class Robot(Workable):

    def work(self):
        print("I'm a robot. I'm working....")


work_manager = WorkManager()
break_manager = BreakManager()
work_manager.set_worker(Worker())
break_manager.set_worker(Worker())
work_manager.manage()
break_manager.lunch_break()
work_manager.set_worker(SuperWorker())
break_manager.set_worker(SuperWorker())
work_manager.manage()
break_manager.lunch_break()
work_manager.set_worker(Robot())
work_manager.manage()

try:
    break_manager.set_worker(Robot())
    break_manager.lunch_break()
# the class is working correctly because the Robot worker does not require a lunch break, like in the unoptimized version of this exercise.
except:
    pass
