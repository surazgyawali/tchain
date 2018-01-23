import tblock as Block
import datetime as date
class next_block:
    def __index__(self,last_block):
        self.last_block = last_block
        # self.Block = Block

    def next_block(last_block):
        this_index = last_block.index+1
        this_timestamp = date.datetime.now()
        this_data = "single block"+str(this_index)
        this_hash = last_block.hash
        return Block.Block(this_index,this_timestamp,this_data,this_hash)
