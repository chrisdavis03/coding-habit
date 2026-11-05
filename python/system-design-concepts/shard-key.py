'''
Sharding is a method to scale writes in Relational DBs.
Here I will do some experimentation with choosing a shard.
'''

from uuid import uuid4
import hashlib

def pick_shard(user_id: str, num_shards: int) -> int:
    '''
    Naive approach to picking a shard. Modulo the hash of the user_id by the number of shards.
    '''
    
    hash_bytes = hashlib.md5(user_id.encode(), usedforsecurity=False)
    print (hash_bytes.hexdigest())
    print(int(hash_bytes.hexdigest(), 16))
    return int(hash_bytes.hexdigest(), 16) % num_shards

if __name__ == '__main__':
    users = []
    shards= []
    for i in range(100):
        users.append(uuid4())
        shard_id = pick_shard(user_id=str(users[i]), num_shards=4)
        shards.append(shard_id)
    print (shards)
