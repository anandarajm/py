def new(num_buckets=256):
    amap=[]
    for i in range(0,num_buckets):
        amap.append([])
    return amap

def hash_key(amap,key):
    return hash(key) % len(amap)

def get_bucket(amap,key):
    bucket_id=hash_key(amap,key)
    return amap[bucket_id]

def get_slot(amap,key,default=None):
    bucket=get_bucket(amap,key)

    for i, kv in enumerate(bucket):
        k,v = kv
        if key == k:
            return i,k,v
    return -1, key, default

def get(amap,key,default=None):
    i,k,v=get_slot(amap,key,default=default)
    return v

def set(amap,key,value):
    bucket=get_bucket(amap,key)
    i,k,v=get_slot(amap,key)

    if i>= 0:
        bucket[i]=(key,value)
    else:
        bucket.append((key,value))

def delete(amap,key):
    bucket=get_bucket(amap,key)
    for i in xrange(len(bucket)):
        k,v=bucket[i]
        if key == k:
            del bucket[i]
            break

def list(amap):
    for bucket in amap:
        if bucket in amap:
            for k,v in bucket:
                print k,v
