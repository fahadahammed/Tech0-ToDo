from ToDo import app
import pymongo
from bson.objectid import ObjectId
import datetime

MCONN = pymongo.MongoClient(app.config["TODO_DB_HOST"], app.config["TODO_DB_PORT"], connect=False)


class MongoOperations:
    def __init__(self, collection_name=None):
        self.client = MCONN
        database_name = str(app.config["ToDo_DB_NAME"]).lower()
        self.db = self.client[database_name]
        if collection_name:
            self.collection = self.db[collection_name]
        else:
            dynamic_collection_name = DynamicName().get_collection_name()
            self.collection = self.db[dynamic_collection_name]

    def get_collections(self):
        return self.db.collection_names()

    def get_count_of_all_objects(self):
        return self.collection.count()

    def insert_data(self, data_json):
        self.collection.insert(data_json)
        return data_json

    def get_data(self, data_json):
        to_return = []
        for i in self.collection.find(data_json):
            to_return.append(i)
        return to_return

    def get_all_data(self):
        alls = []
        for i in self.collection.find({}).sort("created_at"):
            alls.append(i)
        return alls

    def get_specific_data(self, search_params):
        alls = []
        new_search_params = {}
        for i in search_params.keys():
            if i == "log_id":
                i_new = "_id"
                if search_params[i]:
                    new_search_params[i_new] = search_params[i]
            else:
                if search_params[i]:
                    new_search_params[i] = search_params[i]
        for i in self.collection.find(new_search_params).sort("created_at"):
            alls.append(i)
        return alls

    def update_data(self, old_data_condition, new_data):
        if self.collection.update_one(old_data_condition, {"$set": new_data}):
            return True
        else:
            return False

    def delete_data(self, condition_to_delete):
        if self.collection.delete_one(condition_to_delete):
            return True
        else:
            return False

    def delete_data_fake(self, delete_data_condition):
        new_data = {
            "active": False
        }
        if self.collection.update_one(delete_data_condition, {"$set": new_data}):
            return True
        else:
            return False

    def collection_create_index(self, field, name, ascending):
        try:
            if ascending:
                return self.collection.create_index([(field, pymongo.ASCENDING)], name=name)
            else:
                return self.collection.create_index([(field, pymongo.DESCENDING)], name=name)
        except pymongo.errors.OperationFailure:
            return False

    def delete_collection(self, collection_name):
        try:
            if self.db.drop_collection(name_or_collection=collection_name):
                return True
            else:
                return False
        except pymongo.errors.OperationFailure:
            return False


class DynamicName:
    def __init__(self):
        self.str_year = datetime.datetime.now().strftime("%Y")
        self.str_year_month = datetime.datetime.now().strftime("%Y%m%d")
        self.collection_name = "ToDo" + str(self.str_year_month)
        self.database_name = "TODO" + str(self.str_year)

    def get_collection_name(self):
        return self.collection_name

    def get_database_name(self):
        return self.database_name
from ToDo import app
import pymongo
from bson.objectid import ObjectId
import datetime

MCONN = pymongo.MongoClient(app.config["TODO_DB_HOST"], app.config["TODO_DB_PORT"], connect=False)


class MongoOperations:
    def __init__(self, collection_name=None):
        self.client = MCONN
        database_name = str(app.config["ToDo_DB_NAME"]).lower()
        self.db = self.client[database_name]
        if collection_name:
            self.collection = self.db[collection_name]
        else:
            dynamic_collection_name = DynamicName().get_collection_name()
            self.collection = self.db[dynamic_collection_name]

    def get_collections(self):
        return self.db.collection_names()

    def get_count_of_all_objects(self):
        return self.collection.count()

    def insert_data(self, data_json):
        self.collection.insert(data_json)
        return data_json

    def get_data(self, data_json):
        to_return = []
        for i in self.collection.find(data_json):
            to_return.append(i)
        return to_return

    def get_all_data(self):
        alls = []
        for i in self.collection.find({}).sort("created_at"):
            alls.append(i)
        return alls

    def get_specific_data(self, search_params):
        alls = []
        new_search_params = {}
        for i in search_params.keys():
            if i == "log_id":
                i_new = "_id"
                if search_params[i]:
                    new_search_params[i_new] = search_params[i]
            else:
                if search_params[i]:
                    new_search_params[i] = search_params[i]
        for i in self.collection.find(new_search_params).sort("created_at"):
            alls.append(i)
        return alls

    def update_data(self, old_data_condition, new_data):
        if self.collection.update_one(old_data_condition, {"$set": new_data}):
            return True
        else:
            return False

    def delete_data(self, condition_to_delete):
        if self.collection.delete_one(condition_to_delete):
            return True
        else:
            return False

    def delete_data_fake(self, delete_data_condition):
        new_data = {
            "active": False
        }
        if self.collection.update_one(delete_data_condition, {"$set": new_data}):
            return True
        else:
            return False

    def collection_create_index(self, field, name, ascending):
        try:
            if ascending:
                return self.collection.create_index([(field, pymongo.ASCENDING)], name=name)
            else:
                return self.collection.create_index([(field, pymongo.DESCENDING)], name=name)
        except pymongo.errors.OperationFailure:
            return False

    def delete_collection(self, collection_name):
        try:
            if self.db.drop_collection(name_or_collection=collection_name):
                return True
            else:
                return False
        except pymongo.errors.OperationFailure:
            return False


class DynamicName:
    def __init__(self):
        self.str_year = datetime.datetime.now().strftime("%Y")
        self.str_year_month = datetime.datetime.now().strftime("%Y%m%d")
        self.collection_name = "ToDo" + str(self.str_year_month)
        self.database_name = "TODO" + str(self.str_year)

    def get_collection_name(self):
        return self.collection_name

    def get_database_name(self):
        return self.database_name
