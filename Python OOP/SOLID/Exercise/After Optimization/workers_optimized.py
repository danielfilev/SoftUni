from abc import ABC, abstractmethod

# This is a test exercise of the Dependency Inversion Principle.


class Manager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(
            worker, BaseWorker), '`worker` must be of type {}'.format(BaseWorker)

        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()


class BaseWorker(ABC):

    @abstractmethod
    def work(self):
        pass


class SuperWorker(BaseWorker):

    def work(self):
        print("I work very hard!!!")


class Worker(BaseWorker):

    def work(self):
        print("I'm working!!")
 

worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()

super_worker = SuperWorker()
try:
    manager.set_worker(super_worker)
    manager.manage()
    # if the manager class works correctly, then the output data must be "I'm working!!\n" + "I work very hard!!!" instead of AssertionError.
except AssertionError:
    print("manager fails to support super_worker....")
