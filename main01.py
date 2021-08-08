from dataclasses import dataclass


@dataclass(frozen=True)
class Task():
    num: int
    status: str
    subject: str

    def presentor(self):
        print('num is {}, status is {}, subject is {}'.format(
            self.num, self.status, self.subject
        ))

@dataclass(frozen=True)
class TaskTest():
    num: int
    status: str
    subject: str

    def presentor(self):
        print('[Test]: num is {}, status is {}, subject is {}'.format(
            self.num, self.status, self.subject
        ))

# Taskにデータ保持と出力機能がある
# 一部分変えたいときでも、全て複製する必要がある
if __name__ == '__main__':
    task01 = Task(num=1, status='new', subject='task01')
    task01.presentor()

    task02 = TaskTest(num=2, status='new', subject='task02')
    task02.presentor()