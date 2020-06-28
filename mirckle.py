from hashlib import sha256 as hash

def cipherEngine(s):
    print(s,': ',hash(s.encode()).hexdigest())
    return hash(s.encode()).hexdigest()
def mirckle_hash(arr):
    if len(arr) > 0:
        #print(arr)
        if len(arr)==1:
            return cipherEngine(arr[0])
        else:
            intermidiate_state=  cipherEngine(mirckle_hash(arr[:len(arr)//2])+mirckle_hash(arr[len(arr)//2:]))
            print('intermidiate state hash : ',intermidiate_state)
            return intermidiate_state
if __name__ == '__main__':
    a=["abhi","mishra","1816413002","It-02"]
    
    print('====================FINAL HASH============================\n\n','"/" : ',mirckle_hash(a))