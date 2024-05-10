class Task:
    def __init__(self, no=None, title=None, des=None, due=None, status=None):
        self.no = no
        self.title = title
        self.des = des
        self.due = due
        self.status = status
        self.next = None


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_new_task(self, task):

        if self.head is None:
            node = Task(task.no, task.title, task.des, task.due, task.status)
            self.head = node

        itr = self.head
        while itr.next:
            itr = itr.next
        node = Task(task.no, task.title, task.des, task.due, task.status)
        itr.next = node

    def print(self):
        itr = self.head
        while itr:
            print(f"Task No : {itr.no}")
            print(f"Title :{itr.title}")
            print(f"Description :{itr.des}")
            print(f"Due Date :{itr.due}")
            print(f"Status :{itr.status} \n")
            itr = itr.next

    def mainmenu(self):
        print("\t *** To-Do List Manager ***")
        print("\n\t Main Menu")
        print("\n1.Add a Task")
        print("\n2.View All Tasks")

        choice = input("Enter your choice : ")

        match choice:
            case "1":
                self.add_new_task(None)

            case "2":
                self.print()

    def main(self):
        mytask = LinkedList()
        task1 = Task(1, "CS", "Python Project", "23/05/2024", "Not Completed")
        task2 = Task(2, "Maths", "Real Analysis", "20/05/2024", "Completed")
        mytask.add_new_task(task1)
        mytask.add_new_task(task2)
        mytask.print()


if __name__ == '__main__':
    ll = LinkedList()
    ll.main()
