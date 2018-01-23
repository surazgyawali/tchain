import datetime as date
import tblock as Block


class genesis:

    def genesis_block_creation():
        #manually adding a genesis block
        return Block.Block(0, date.datetime.now(),"Genesis Block","0")