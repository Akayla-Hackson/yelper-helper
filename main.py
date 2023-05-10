
import json


# makes the original datasets a valid json file
def make_valid_json(input_file, output_file):
    # Read input JSON file
    with open(input_file, 'r') as f:
        data = f.readlines()

    # Create output JSON file
    with open(output_file, 'w') as f:
        # Start of JSON array
        f.write('[')

        # Loop through input JSON objects
        count = 0
        for line in data:
            try:
                # Load JSON object
                obj = json.loads(line)
            except json.JSONDecodeError:
                # Skip non-JSON lines
                continue

            # Write JSON object to output file
            if count > 0:
                # Add comma separator between objects
                f.write(',')
            json.dump(obj, f)
            count += 1

        # End of JSON array
        f.write(']')


# make_valid_json('yelp_academic_dataset_business.json', 'full_business.json')
# make_valid_json('yelp_academic_dataset_tip.json', 'full_tip.json')
# make_valid_json('yelp_academic_dataset_checkin.json', 'full_checkin.json')
# make_valid_json('yelp_academic_dataset_review.json', 'full_review.json')
# make_valid_json('yelp_academic_dataset_user.json', 'full_user.json')


# gets all the food businesses from the input file and returns them into the output file
def filter_restaurants(input_file, output_file):
    # Open the input and output files
    with open(input_file, 'r') as input_file, open(output_file, 'w') as output_file:
        # Load the input JSON data
        data = json.load(input_file)

        # Create a list to store the filtered objects
        filtered_objects = []
        positive_count = 0
        negative_count = 0
        # Loop through each object in the JSON data
        for obj in data:
            # Check if "Food" is in the category array
            if obj.get("categories") and ("food" in obj["categories"].lower() or "restaurant" in obj["categories"].lower()):
                # Add the object to the filtered list
                filtered_objects.append(obj)
                positive_count += 1
            else:
                print(obj)
                negative_count += 1

        # Write the filtered objects to the output file
        json.dump(filtered_objects, output_file)

# filter_restaurants('full_business.json', 'food_businesses.json')


# prints the amount of json objects in a file
def print_length_json(input_file):
    with open(input_file, 'r') as file:
        # Load the JSON data
        data = json.load(file)
        # Get the number of objects
        count = len(data)
        # Print the count
        print(f"The JSON file contains {count} objects.")

#print_length_json('full_business.json')
#print_length_json('food_businesses.json')


# returns an array of all the elements from the input_file
# ex: gets the business_id's from the food_businesses.json file
def get_element_from_json(input_file, element):
    with open(input_file, 'r') as file:
        # Load the JSON data
        data = json.load(file)
        # Initialize an empty list to store the business IDs
        elements = []
        # Loop through each object in the JSON data
        for obj in data:
            # Get the business ID from the current object
            target_element = obj[element]
            # Add the business ID to the list
            elements.append(target_element)
        return elements

# looks through input_file for element matching in the element_array
# ex: filter the review file based off the business_id element using the food_business_ids array
def filter_by_element(input_file, output_file, element_array, element_name):
    with open(input_file, 'r') as input_file, open(output_file, 'w') as output_file:
        # Load the JSON data
        data = json.load(input_file)
        # Initialize an empty list to store the filtered objects
        filtered_objects = []
        positive_count = 0
        negative_count = 0
        # Loop through each object in the JSON data
        for obj in data:
            # Get the element from the current object
            target_element = obj.get(element_name)
            # Check if the target_element is in the element_array
            if target_element in element_array:
                # Add the object to the filtered list
                filtered_objects.append(obj)
                positive_count += 1
            else:
                negative_count += 1
        # Write the filtered objects to the output file
        json.dump(filtered_objects, output_file)


food_business_ids = get_element_from_json('food_businesses.json', 'business_id')
# filter_by_element('full_review.json', "restaurant_reviews.json", food_business_ids, 'business_id')
# filter_by_element('full_checkin.json', "restaurant_checkin.json", food_business_ids, 'business_id')
# filter_by_element('full_tip.json', "restaurant_tip.json", food_business_ids, 'business_id')


