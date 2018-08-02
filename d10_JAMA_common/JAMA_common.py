import requests
import json

def get(url,username,password):
    response = requests.get(url, auth=(username, password))
    return json.loads(response.text)

# arrgh - the JAMA api only gets up to 50 items - need to do multiple requests
def get_all_data(url,username,password):
    # from https://community.jamasoftware.com/blogs/john-lastname/2017/09/29/managing-multiple-pages-of-results-in-the-jama-rest-api

    all_data = []
    allowed_results = 10
    max_results = "maxResults=" + str(allowed_results)
    
    result_count = -1
    start_index = 0
    
    while result_count != 0:
        start_at = "startAt=" + str(start_index)
        
        part_url = url + "?" + start_at + "&" + max_results 
        response = get(part_url,username,password)
        
        page_info = response["meta"]["pageInfo"]
        start_index = page_info["startIndex"] + allowed_results
        result_count = page_info["resultCount"]

        all_data.extend(response["data"])
    return all_data

    
    

def put(url, payload,username,password):
    response = requests.put(url, json=payload, auth=(username, password))
    return response.status_code

def get_id(base_url, string_to_find,username,password):
    url = base_url + "abstractitems?contains=" + string_to_find
    json_response = get(url,username,password)

    total_results = json_response["meta"]["pageInfo"]["totalResults"]

    if total_results == 1:
        data = json_response["data"]
        item = data[0]
        return item["id"]

    else:
        print("string_to_find wasn't unique")
        sys.exit(1)

def update_item(item_id, username,password):
    set_lock_state(True, item_id)
    item = get_item(item_id)
    item["fields"]["description"] += test_results()
    put_item(item_id, item, username,password)
    set_lock_state(False, item_id)

def set_lock_state(base_url, new_lock_state, item_id, username, password):
    payload = {
        "locked": new_lock_state
    }
    url = base_url + "items/" + str(item_id) + "/lock"
    put(url, payload,username,password)

def get_item(base_url, item_id,username,password):
    url = base_url + "items/" + str(item_id)
    json_response = get(url,username,password)

    return json_response["data"]

def put_item(base_url, item_id, item,username,password):
    print("put_item ", item_id)
    url = base_url + "items/" + str(item_id)
    status_code = put(url, item, username, password)
    if status_code < 400:
        print("Success", str(status_code))
    else:
        print("Fail", str(status_code))

def test_results():
    template = "<p><strong>Imported test results:</strong></p>Status:&nbsp;"
    test_passed = random.randrange(0,2)
    if test_passed == 1:
        return template + "pass"
    return template + "fail"
