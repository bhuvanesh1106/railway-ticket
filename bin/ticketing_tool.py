from utils import insert_data,fetch_data
import uuid


class TicketingTool:
    def __init__(self, uid, name, email_id, number, address):
        print("Constructor")


        self.uid = uuid.uuid4()
        self.name = name
        self.id = email_id
        self.number = number
        self.address = address

    def get_user_info(self):
        print( self.uid, self.name, self.id, self.number, self.address)

    def insert_data(self):
        insert_data(  self.uid, self.name,self.id,self.number,self.address)

class SqlData:
    def fetch_data(self):
     return fetch_data()



id = uuid.uuid4()
# Id generated using uuid4()
print("The id generated using uuid4() : ",end="")
print(id)



if __name__ == "__main__":
    uuid.uuid4()
     name = input("Enter your name")
     mail_id = input("Enter your mail id")
     number = input("Enter your number")
     address = input("Enter your address")
     Object1 = TicketingTool(name, mail_id, number, address)
     Object1.get_user_info()
     Object1.insert_data()
     #object1=SqlData()
     #data=object1.fetch_data()
     #print(data)

