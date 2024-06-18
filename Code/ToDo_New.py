from datetime import date
import mysql.connector
import sys


db = mysql.connector.connect(
    host="localhost", user="root", password="", database="linkedlist")
cursor = db.cursor()

"""if db.is_connected():
    print("Connection Successfully")
else:
    print("Failed to Connect") """


class Node:
    def __init__(self, no=None, title=None, des=None, due=None, status=None):
        self.no = no
        self.title = title
        self.des = des
        self.due = due
        self.status = status
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.retrieve()

    def append_data(self, no, title, des, due, status):
        node = Node(no, title, des, due, status)

        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def retrieve(self):
        cursor.execute("show tables")
        lst = cursor.fetchall()

        if ("task",) in lst:

            query = "SELECT * FROM task"
            cursor.execute(query)
            rows = cursor.fetchall()

            for row in rows:
                self.append_data(row[0], row[1], row[2], row[3], row[4])

    def add_new_task(self):
        count = input("How many Task do you want to add : ")
        count = int(count)

        cursor.execute("show tables")
        lst = cursor.fetchall()

        for i in range(count):
            title = input("\nEnter Task's Title : ")
            des = input("Enter Task's Description : ")
            due = input("Enter Task's Due Date (yyyy-mm-dd) :")

            due_date = date.fromisoformat(due)

            if self.head is None and not ("task",) in lst:
                node = Node(None, title, des, due_date, "Not Completed")
                self.head = node

                query1 = "CREATE TABLE task(no INT AUTO_INCREMENT PRIMARY KEY,title VARCHAR(255) NOT NULL,des VARCHAR(255) NOT NULL, due date ,status VARCHAR(50))"

                cursor.execute(query1)

                query2 = "INSERT INTO task(title,des,due,status) VALUES (%s,%s,%s,%s)"
                val = (title, des, due, "Not Completed")
                cursor.execute(query2, val)
                db.commit()

            else:
                current = self.head
                while current.next:
                    current = current.next
                node = Node(None, title, des, due_date, "Not Completed")
                current.next = node

                query2 = "INSERT INTO task(title,des,due,status) VALUES (%s,%s,%s,%s)"
                val = (title, des, due, "Not Completed")
                cursor.execute(query2, val)
                db.commit()

        self.mainmenu()

    def mytasklist(self):
        print("\n\t *** My To-Do List ***")
        current = self.head

        if current == None:
            print("Task List is Empty")
        else:
            while current:
                print(f"No: {current.no}")
                print(f"Title: {current.title}")
                print(f"Description: {current.des}")
                print(f"Due: {current.due}")
                print(f"Status: {current.status}")
                print("--------------------")
                current = current.next

        self.mainmenu()

    def print_task(self, task):
        print(f"Task No : {task.no}")
        print(f"Title : {task.title}")
        print(f"Description : {task.des}")
        print(f"Due Date : {task.due}")
        print(f"Status : {task.status} \n")
        print("--------------------")

    def delete_task(self):
        print("\t *** Delete a Task ***")
        no = input("\nEnter Task No. : ")
        no = int(no)

        current = self.head

        while current:
            if current.no == no-1:
                # temp = current.next.no
                current.next = current.next.next
                # current.next.no = temp
                break

            current = current.next

        query = "DELETE FROM task WHERE no= %s"
        val = (no,)
        cursor.execute(query, val)
        db.commit()

        print("Task Deleted Successfuly !!!\n")
        self.mainmenu()

    def delete_all_task(self):
        query = "DROP TABLE task"
        cursor.execute(query)

        current = self.head
        while current:
            prev = current
            current = current.next
            del prev
        self.head = None

        print("All Tasks Deleted Successfully")
        self.mainmenu()

    def due_today(self):
        print("\t*** Task Due Today ***\n")

        query = "SELECT * FROM task WHERE due=%s"
        val = (date.today(),)
        cursor.execute(query, val)
        rows = cursor.fetchall()

        for row in rows:
            newnode = Node(row[0], row[1], row[2], row[3], row[4])
            self.print_task(newnode)

        self.mainmenu()
        del newnode

    def mark_completed_task(self):
        no = input("\nEnter task No : ")
        no = int(no)
        current = self.head

        while current:
            if current.no == no:
                current.status = "Completed"
                break
            current = current.next

        query = "UPDATE task SET status='Completed' WHERE no=%s"
        val = (no,)
        cursor.execute(query, val)
        db.commit()
        self.mainmenu()

    def view_completed_tasks(self):
        print("\t*** Completed Tasks ***\n")

        query = "SELECT * FROM task WHERE status='Completed'"
        cursor.execute(query)
        rows = cursor.fetchall()

        for row in rows:
            newnode = Node(row[0], row[1], row[2], row[3], row[4])
            self.print_task(newnode)

        self.mainmenu()
        del newnode

    def soted_by_due(self):
        current = self.head
        sortedHead = None

        while current != None:
            next = current.next
            current.next = None

            prev = None
            sortedCurrent = sortedHead

            while sortedCurrent != None and sortedCurrent.due < current.due:
                prev = sortedCurrent
                sortedCurrent = sortedCurrent.next

            if prev == None:
                sortedHead = current
            else:
                prev.next = current

            current.next = sortedCurrent
            current = next
        print("\t*** Sort By Due ***\n")
        while sortedHead != None:
            self.print_task(sortedHead)
            sortedHead = sortedHead.next

        self.mainmenu()

    def edit_task(self):
        print("\t *** Edit Task's Details ***")
        no = input("\nEnter Task No. : ")
        no = int(no)

        current = self.head

        while current:
            if current.no == no:
                title = input("\nEnter New Title : ")
                des = input("Enter New Description : ")
                due = input("Enter new Due Date (yyyy-mm-dd) : ")
                due_date = date.fromisoformat(due)

                current.title = title
                current.des = des
                current.due = due_date
                current.status = 'Not Completed'
                break

            current = current.next

        query = "UPDATE task SET title=%s,des=%s,due=%s,status=%s WHERE no=%s"
        val = (title, des, due_date, 'Not Completed', no)
        cursor.execute(query, val)
        db.commit()

        print("\n\tEdit a Task is Successful !!!\n")
        self.mainmenu()

    def mainmenu(self):
        print("\t *** To-Do List Manager ***")
        print("\n\t Main Menu")
        print("\n1.Add a Task")
        print("2.View All Tasks")
        print("3.Delete a Task")
        print("4.Delete All Tasks")
        print("5.Task's Due Today")
        print("6.Mark Completed Tasks")
        print("7.View Completed Tasks")
        print("8.Sort By Due")
        print("9.Edit a Task")
        print("10.Exit")

        choice = input("\nEnter your choice : ")

        match choice:
            case "1":
                self.add_new_task()

            case "2":
                self.mytasklist()

            case "3":
                self.delete_task()

            case "4":
                self.delete_all_task()

            case "5":
                self.due_today()

            case "6":
                self.mark_completed_task()

            case "7":
                self.view_completed_tasks()

            case "8":
                self.soted_by_due()

            case "9":
                self.edit_task()

            case "10":
                sys.exit(0)


if __name__ == '__main__':
    ll = LinkedList()
    ll.mainmenu()
