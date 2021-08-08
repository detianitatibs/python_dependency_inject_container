from dataclasses import dataclass


@dataclass(frozen=True)
class Task():
    num: int
    status: str
    subject: str


class Presentor():
    def presentor(self, task: Task):
        print('num is {}, status is {}, subject is {}'.format(
            task.num, task.status, task.subject
        ))


class PresentorTest():
    def presentor(self, task: Task):
        print('[Test]: num is {}, status is {}, subject is {}'.format(
            task.num, task.status, task.subject
        ))


class ApplicationTask():
    def print(self, task: Task, presentor: Presentor):
        presentor.presentor(task)
    
    def print_test(self, task: Task, presentor: PresentorTest):
        presentor.presentor(task)

# データ保持とデータ出力の機能を分離した
# ついでにApprlicationTaskという動かす部分を作った
# ApplicationTaskにPresentorが依存している
# ->例えば、presentorの出力をするときに、printメソッド、print_testメソッドが必要
if __name__ == '__main__':
    task01 = Task(num=1, status='new', subject='task01')
    presentor01 = Presentor()
    ApplicationTask().print(task01, presentor01)

    task02 = Task(num=2, status='new', subject='task02')
    presentor02 = PresentorTest()
    ApplicationTask().print_test(task02, presentor02)
