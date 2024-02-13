class HashMap:
    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        hash = self._hash_function(key)
        for pair in self.hash_table[hash]: #check if k-v needs to be updated, if the key is not found append new k-v pair 
            if pair[0] == key:
                pair.append(value) # appending allows multiple values to be stored with the same key
                return 
        self.hash_table[hash].append([key, value])

    def get(self, key):
        hash = self._hash_function(key)
        for pair in self.hash_table[hash]:
            if pair[0] == key:
                return pair[1:]
        return None
        
    def remove(self, key, value):
        bucket = self.hash_table[self._hash_function(key)]

        for pair in bucket: #k-v has only one value, remove the entire pair 
            if pair[0] == key and len(pair) == 2:
                bucket.remove(pair)
            else: # k-v pair has more than one value, just remove that value 
                for val in pair[1:]:
                    if val == value:
                        pair.remove(value)

    def display(self):
        for bucket in self.hash_table:
            print(bucket)

    def max_passengers_in_flight(self, flight_number):
        flight = self.get(flight_number)

        max = 0
        if len(flight) > 2:
            for f in flight:
                if f.passengers > max:
                    max = f.passengers
        else:
            max = flight[1].passengers
        return max
    
class FlightNode:
    def __init__(self, flight_number, trip_id, passengers):
        self.flight_number = flight_number
        self.trip_id = trip_id
        self.passengers = passengers

if __name__ == "__main__":

    # Display the hash map
    my_hash_map = HashMap(7)
    0, 1, 4, 9, 16, 25, 36, 49, 64, 81
    my_hash_map.put("aaa", 0)
    my_hash_map.put("bbb", 1)
    my_hash_map.put("ccc", 4)
    my_hash_map.put("ddd", 9)
    my_hash_map.put("eee", 16)
    my_hash_map.put("fff", 25)
    my_hash_map.put("ggg", 36)
    my_hash_map.put("hhh", 49)
    my_hash_map.put("ccc", 64)
    my_hash_map.put("ccc", 81)
    my_hash_map.display()  

    # Retrieve values
    print("Retrieve values:")
    print("aaa:", my_hash_map.get("aaa"))  
    print("bbb:", my_hash_map.get("bbb"))
    print("ccc:", my_hash_map.get("ccc"))

    # Remove a key-value pair
    my_hash_map.remove("bbb", 1)  

    # Display the updated hash map
    my_hash_map.display() 

    #Max Passengers on Trip
    my_map = HashMap(11)
    # Add flight nodes (flight_number, trip_id, passengers)
    my_map.put(16, FlightNode(16, "Trip 1", 300))
    my_map.put(16, FlightNode(16, "Trip 2", 700))
    my_map.put(29, FlightNode(29, "Trip 1", 800))
    my_map.put(29, FlightNode(29, "Trip 2", 250))
    my_map.put(36, FlightNode(29, "Trip 3", 500))
    my_map.put(36, FlightNode(36, "Trip 1", 500))
    my_map.put(36, FlightNode(36, "Trip 2", 340))
    my_map.put(36, FlightNode(36, "Trip 3", 900))
    my_map.put(36, FlightNode(36, "Trip 4", 400))
    my_map.put(49, FlightNode(49, "Trip 1", 250))
    my_map.put(49, FlightNode(49, "Trip 2", 550))

    max_passengers = my_map.max_passengers_in_flight(49)

    if max_passengers is not None:
        print("Largest number of people in flight at once :", max_passengers)
    else:
        print("Flight not found in the map")
