from datetime import datetime
from datetime import date


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

            due_date = date.fromisoformat(due)

            if self.head is None:
                node = Task(i+1, title, des, due_date, status)
                self.head = node

            else:
                itr = self.head
                while itr.next:
                    itr = itr.next
                node = Task(i+1, title, des, due_date, status)
                itr.next = node

        self.mainmenu()

    def addnew(self, no, title, des, due, status):
        due_date = date.fromisoformat(due)
        if self.head is None:
            node = Task(no, title, des, due_date, status)
            self.head = node

        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            node = Task(no, title, des, due_date, status)
            itr.next = node

    def mytasklist(self):
        print("\n\t *** My To-Do List ***")
        itr = self.head
        while itr:
            print(f"Task No : {itr.no}")
            print(f"Title : {itr.title}")
            print(f"Description : {itr.des}")
            print(f"Due Date : {itr.due}")
            print(f"Status : {itr.status} \n")
            itr = itr.next

        self.mainmenu()

    def print_task(self, task):
        print(f"Task No : {task.no}")
        print(f"Title : {task.title}")
        print(f"Description : {task.des}")
        print(f"Due Date : {task.due}")
        print(f"Status : {task.status} \n")

    def mark_completed_task(self):
        no = input("\nEnter task No : ")
        no = int(no)
        itr = self.head

        while itr:
            if itr.no == no:
                itr.status = "Completed"
                break
            itr = itr.next
        print("Status change is Successful !!!\n")

        self.mainmenu()

    def view_completd_task(self):
        print("\t*** Completed Tasks ***\n")
        itr = self.head

        while itr:
            if itr.status == "Completed":
                self.print_task(itr)
                itr = itr.next
            else:
                itr = itr.next

        self.mainmenu()

    def edit_task(self):
        print("\t *** Edit Task's Details ***")
        no = input("\nEnter Task No. : ")
        no = int(no)

        itr = self.head

        while itr:
            if itr.no == no:
                title = input("Enter New Title : ")
                des = input("Input New Description : ")
                due = input("Enter new Due Date (yyyy-mm-dd) : ")
                due_date = date.fromisoformat(due)

                itr.title = title
                itr.des = des
                itr.due = due_date
                break

            itr = itr.next

        print("Edit a Task is Successful !!!\n")
        self.mainmenu()

    def delete_task(self):
        print("\t *** Delete a Task ***")
        no = input("\nEnter Task No. : ")
        no = int(no)

        itr = self.head

        while itr:
            if itr.no == no-1:
                x = itr.next.no
                itr.next = itr.next.next
                itr.next.no = x

                break

            itr = itr.next

        print("Task Deleted Successfuly !!!\n")
        self.mainmenu()

    def dueToday(self):
        print("\t*** Task Due Today ***\n")
        itr = self.head

        while itr:
            if itr.due == date.today():
                self.print_task(itr)
                itr = itr.next
            else:
                itr = itr.next

        self.mainmenu()

    def sortbyDue(self):
        itr = self.head.next
        itr_prev = self.head

        while itr.next:
            if itr_prev.due < itr.due:
                self.print_task(itr)
                itr = itr.next
                itr_prev = itr_prev.next
            else:
                itr = itr.next
                itr_prev = itr_prev.next
                self.print_task(itr)

    def mainmenu(self):
        print("\t *** To-Do List Manager ***")
        print("\n\t Main Menu")
        print("\n1.Add a Task")
        print("2.View All Tasks")
        print("3.Mark Completed Tasks")
        print("4.View Completed Tasks")
        print("5.Edit a Task")
        print("6.Delete a Task")
        print("7.Tasks Due Today")
        print("8.Sort by Due Date")
        print("10.Exit")

        choice = input("\nEnter your choice : ")

        match choice:
            case "1":
                self.add_new_task()

            case "2":
                self.mytasklist()

            case "3":
                self.mark_completed_task()

            case "4":
                self.view_completd_task()

            case "5":
                self.edit_task()

            case "6":
                self.delete_task()

            case "7":
                self.dueToday()

            case "8":
                self.sortbyDue()

            case "10":
                SystemExit(0)


if __name__ == '__main__':
    ll = LinkedList()
    ll.addnew(1, "CS", "Project", "2024-05-12", "Not Completed")
    ll.addnew(2, "Maths", "Real Analysis", "2024-05-25", "Not Completed")
    ll.addnew(3, "Trip", "To Galle", "2024-05-17", "Not Completed")
    ll.mainmenu()
