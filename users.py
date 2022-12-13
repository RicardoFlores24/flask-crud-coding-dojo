from mysqlconnection import connectToMySQL

class User:  #db
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls): #getting the db
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
        users = [] #empty list
        for u in results: # showing the dict
            users.append( cls(u) ) # showing the dict
        return users # returning the list

    @classmethod
    def save(cls, data): #inserting data to the db
        query = "INSERT INTO users (first_name,last_name,email) VALUES (%(first_name)s,%(last_name)s,%(email)s);"

        result = connectToMySQL('users_schema').query_db(query,data)
        return result