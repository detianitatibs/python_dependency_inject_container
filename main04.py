from abc import ABCMeta, abstractclassmethod
from dataclasses import dataclass

from injector import Injector, inject, Module, Binder

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
    @inject
    def __init__(self, presentor: PresentorInterface):
        # ここは抽象クラスであるPresentorInerfaceを使う
        # Presentorなのか、PresentorTestなのかは知らなくて良い
        self.presentor = presentor

    def print(self, task: Task):
        self.presentor.presentor(task)


class TaskDIModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(PresentorInterface, to=Presentor)


class TaskDIMduleTest(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(PresentorInterface, to=PresentorTest)

# Injectorを使うことで、DIコンテナを使うことができる
# DIコンテナ経由で使うことで、TaskDIModule, TaskDIModuleTestのように
# それぞれの用途にそったモジュールを切り替えることができる
# テストのときは、テスト用のDIコンテナを指定するだけであとは変えなくても良い
if __name__ == '__main__':
    task01 = Task(num=1, status='new', subject='task01')
    injector = Injector([TaskDIModule()])
    application = injector.get(ApplicationTask)
    application.print(task01)

    task02 = Task(num=2, status='new', subject='task02')
    injector = Injector([TaskDIMduleTest()])
    application = injector.get(ApplicationTask)
    application.print(task02)

