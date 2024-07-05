import pickle

# create an object
my_dict = {'name': 'Robert', 'birthdate': '4-17-81', 'sex': 'Male', 'hair_color': 'brown'}

with open('my_data.dat', 'wb') as file_for_writing:
    pickle.dump(my_dict, file_for_writing)

with open('my_data.dat', 'rb') as file_for_reading:
    pickled_object = pickle.load(file_for_reading)

print(pickled_object)
