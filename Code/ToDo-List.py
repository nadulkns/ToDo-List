

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

    def add_new_task(self):
        count = input("How many Task do you want to add : ")
        count = int(count)

        for i in range(count):
            title = input("\nEnter Task's Title : ")
            des = input("Enter Task's Description : ")
            due = input("Enter Task's Due Date (yyyy-mm-dd) :")
            status = input("Enter Task Status : ")

            if self.head is None:
                node = Task(i+1, title, des, due, status)
                self.head = node

            else:
                itr = self.head
                while itr.next:
                    itr = itr.next
                node = Task(i+1, title, des, due, status)
                itr.next = node

        self.mainmenu()

    def print(self):
        print("\n\t *** My To-Do List ***")
        itr = self.head
        while itr:
            print(f"Task No : {itr.no}")
            print(f"Title :{itr.title}")
            print(f"Description :{itr.des}")
            print(f"Due Date :{itr.due}")
            print(f"Status :{itr.status} \n")
            itr = itr.next

        self.mainmenu()

    def mainmenu(self):
        print("\t *** To-Do List Manager ***")
        print("\n\t Main Menu")
        print("\n1.Add a Task")
        print("2.View All Tasks")
        print("5.Exit")

        choice = input("\nEnter your choice : ")

        match choice:
            case "1":
                self.add_new_task()

            case "2":
                self.print()

            case "5":
                SystemExit(0)

    def main(self):
        self.mainmenu()


if __name__ == '__main__':
    ll = LinkedList()
    ll.main()
