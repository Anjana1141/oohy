from pymongo import MongoClient

class MongoDBUtils:
    
    def __init__(self, host, port, db_name):
        self.host = host
        self.port = port
        self.db_name = db_name
        self.client = None
        self.db = None
        self.connect()

    def connect(self):
        try:
            self.client = MongoClient(self.host, self.port)
            self.db = self.client[self.db_name]
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")

   

    def insert_data(self, collection_name, document):
        """
        Insert a document into the specified MongoDB collection.

        Args:
            collection_name (str): The name of the collection to insert the document into.
            document (dict): The document to be inserted into the collection.

        Returns:
            ObjectId or None: The ObjectId of the inserted document, or None if insertion failed.
        """
        try:
            if self.db:
                collection = self.db[collection_name]
                result = collection.insert_one(document)
                return result.inserted_id
            else:
                print("MongoDB connection not established.")
                return None
        except Exception as e:
            print(f"Error inserting document into collection '{collection_name}': {e}")
            return None

    def insert_document(self, collection_name, document):
        """
        Insert a document into the specified MongoDB collection.

        Args:
            collection_name (str): The name of the collection to insert the document into.
            document (dict): The document to be inserted into the collection.

        Returns:
            ObjectId or None: The ObjectId of the inserted document, or None if insertion failed.
        """
        try:
            if self.db:
                collection = self.db[collection_name]
                result = collection.insert_one(document)
                return result.inserted_id
            else:
                print("MongoDB connection not established.")
                return None
        except Exception as e:
            print(f"Error inserting document into collection '{collection_name}': {e}")
            return None

        
    def close(self):
        try:
            if self.client:
                self.client.close()
        except Exception as e:
            print(f"Error closing MongoDB connection: {e}")

# Usage example:
mongodb_utils = MongoDBUtils(host='54.166.103.115', port=27017, db_name='dataoohy')
document = {"name": "John", "age": 30}
inserted_id = mongodb_utils.insert_document(collection_name='your_collection_name', document=document)
print("Inserted document ID:", inserted_id)

# Don't forget to close the connection when done
mongodb_utils.close()
