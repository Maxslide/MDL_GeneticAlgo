import json
import requests
import numpy as np
import random
######### DO NOT CHANGE ANYTHING IN THIS FILE ##################
API_ENDPOINT = 'http://10.4.21.147'
PORT = 3000
MAX_DEG = 11
arr = [0.0, 0.1240317450077846, -6.211941063144333, 0.04933903144709126, 0.03810848157715883, 8.132366097133624e-05, -6.018769160916912e-05, -1.251585565299179e-07, 3.484096383229681e-08, 4.1614924993407104e-11, -6.732420176902565e-12]
#### functions that you can call
# def modify_decimal(test_arr):
    
def get_errors(id, vector):
    """
    returns python array of length 2 
    (train error and validation error)
    """
    for i in vector: assert -10<=abs(i)<=10
    assert len(vector) == MAX_DEG

    return json.loads(send_request(id, vector, 'geterrors'))

def submit(id, vector):
    """
    used to make official submission of your weight vector
    returns string "successfully submitted" if properly submitted.
    """
    for i in vector: assert -10<=abs(i)<=10
    assert len(vector) == MAX_DEG
    return send_request(id, vector, 'submit')

#### utility functions
def urljoin(root, port, path=''):
    root = root + ':' + str(port)
    if path: root = '/'.join([root.rstrip('/'), path.rstrip('/')])
    return root

def send_request(id, vector, path):
    api = urljoin(API_ENDPOINT, PORT, path)
    vector = json.dumps(vector)
    response = requests.post(api, data={'id':id, 'vector':vector}).text
    if "reported" in response:
        print(response)
        exit()

    return response

def Cross_2parent():
    with open('data.json') as f:
        data = json.load(f)
    vector1 = random.choice(data)["arr"]
    vector2 = random.choice(data)["arr"]
    vector = vector
    # for i in range(len(vector)):
        
def BitComplement():
    with open('data.json') as f:
        data = json.load(f)
    vector = random.choice(data)["arr"]
    print(vector)
    for i in range(1,len(vector)):
        for j in range(random.choice(list(range(3)))):
            temp = list('{:.27f}'.format(vector[i]))
            mini = 3
            for k in range(3,len(temp)):
                if(temp[k] != '0'):
                    mini = k
                    break
            maxi = len(temp)
            if(i in list(range(5))):
                maxi = 17
            if(i in list(range(5,9))):
                maxi = 23
            mid = (mini+maxi)/2
            # for i in range(len(temp) -1, 2):
            #     if(temp[i])
            rand = random.choice(list(range(int((mini+mid)/2),int((maxi+mid)/2)))) 
            temp[rand] = str(random.choice(list(range(10))))
            # print(i)
            vector[i] = float(''.join(temp))
    return vector 
        
def Add_To_File(arr,err):
    with open('data.json') as f:
        data = json.load(f)
    y = {"arr" : arr, "Terr": err[0], "Verr" : err[1]}
    data.append(y)
    with open('data.json','w') as f:
        json.dump(data,f,indent=4)
    print("Added to the file", y)
    return
if __name__ == "__main__":
    """
    Replace "i0ZxSBn9KTktTOfG5xlLZ9CrNY2hEhg8SnLisL4CHNHGtYuqLf" with your secret ID and just run this file 
    to verify that the server is working for your ID.
    """
    vector = BitComplement()
    err = get_errors('JtabQSXoKd2CihU78SWRmmvFUqe7N2yFho55eMMQbplTwMGxus', vector)
    assert len(err) == 2
    print(err)
    if(len(err) == 2 and len(arr) == 11):
        Add_To_File(vector,err)
    

    # submit_status = submit('i0ZxSBn9KTktTOfG5xlLZ9CrNY2hEhg8SnLisL4CHNHGtYuqLf', list(-np.arange(0,1.1,0.1)))
    # assert "submitted" in submit_status
    
