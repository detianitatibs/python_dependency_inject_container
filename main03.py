from abc import ABCMeta, abstractclassmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class Task():
    num: int
    status: str
    subject: str


class PresentorInterface(metaclass=ABCMeta):
    @abstractclassmethod
    def presentor(self, task: Task):
        pass


class Presentor(PresentorInterface):
    def presentor(self, task: Task):
        print('num is {}, status is {}, subject is {}'.format(
            task.num, task.status, task.subject
        ))


class PresentorTest(PresentorInterface):
    def presentor(self, task: Task):
        print('[Test]: num is {}, status is {}, subject is {}'.format(
            task.num, task.status, task.subject
        ))


class ApplicationTask():
    def print(self, task: Task, presentor: PresentorInterface):
        # ここは抽象クラスであるPresentorInerfaceを使う
        # Presentorなのか、PresentorTestなのかは知らなくて良い
        presentor.presentor(task)

# ApplicationはPresentorのインタフェースに依存する
# そのため、Presentorなのか、PresentorTestなのかは気にしなくてよい
# これが、DI
if __name__ == '__main__':
    task01 = Task(num=1, status='new', subject='task01')
    presentor01 = Presentor()
    ApplicationTask().print(task01, presentor01)

    task02 = Task(num=2, status='new', subject='task02')
    presentor02 = PresentorTest()
    ApplicationTask().print(task02, presentor02)