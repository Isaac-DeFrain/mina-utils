'''
Conversion between different time units for the Mina Protocol

ISO-8601 <-> epochs <-> slots <-> ms ticks
'''

import argparse
from datetime import datetime

# an epoch lasts 14 days, 21 hours
# each slot lasts 3 minutes (180_000 ms)
# 1 month ~ 2 epochs

SLOTS_PER_EPOCH = 7140
TICKS_PER_SLOT  = 180_000
TICKS_PER_EPOCH = TICKS_PER_SLOT * SLOTS_PER_EPOCH

def iso8601_to_datetime(iso: str):
    '''
    Parse ISO-8601 date/time string to datetime object

    Note: this function depends on machine's local timezone. Adjust accordingly!
    '''
    return datetime.strptime(iso, '%Y-%m-%dT%H:%M:%SZ')

# convert everything to ms

def iso_to_ms(iso: str):
    """
    Converts ISO-8601 DateTime to ms

    Note: `iso8601_to_datetime` uses local timezone. Adjust accordingly!

    >>> # epoch 42
    >>> dt42_start = iso8601_to_datetime('2022-12-01T13:00:00Z') # UTC-5
    >>> dt42_end   = iso8601_to_datetime('2022-12-16T09:59:59Z') # UTC-5
    >>> # epoch 43
    >>> dt43_start = iso8601_to_datetime('2022-12-16T10:00:00Z') # UTC-5
    >>> dt43_end   = iso8601_to_datetime('2022-12-31T06:59:59Z') # UTC-5
    >>> assert True
    """
    dt = iso8601_to_datetime(iso)
    return int(dt.timestamp() * 1000)

def epoch_slot_to_ms(epoch_slot) -> int:
    '''
    Converts Mina `(epoch, slot)` to time (ms)
    '''
    epoch = epoch_slot[0]
    slot = epoch_slot[1]
    return genesis_ticks + epoch * TICKS_PER_EPOCH + slot * TICKS_PER_SLOT

def gslot_to_ms(gslot):
    '''
    Converts global Mina slot to time (ms)
    '''
    gslot = gslot[0]
    return int(genesis_ticks + gslot * TICKS_PER_SLOT)

# convert ms to everything

genesis_ticks = iso_to_ms('2021-03-17T00:00:00Z')

def ms_to_iso(ticks):
    '''
    Converts time (ms) to ISO-8601 DateTime
    '''
    dt = datetime.fromtimestamp(ticks)
    return dt.isoformat()

def ms_to_epoch(ticks):
    '''
    Converts time (ms) to Mina `(epoch, slot)`
    '''
    return (
        (ticks - genesis_ticks) // TICKS_PER_EPOCH, # epoch
        (ticks - genesis_ticks) % TICKS_PER_EPOCH   # local slot
    )

def ms_to_gslot(ticks):
    '''
    Converts time (ms) to global Mina slot
    '''
    return (ticks - genesis_ticks) // TICKS_PER_SLOT

def ms_to_eslot(ticks):
    '''
    Converts time (ms) to local (current epoch) Mina slot
    '''
    ticks_into_epoch = (ticks - genesis_ticks) % TICKS_PER_SLOT
    return ticks_into_epoch // TICKS_PER_SLOT

# cli

valid_args = ['e', 'es', 'gs', 'i', 'ms']
valid_cmds = ['epoch', 'slot', 'iso', 'ms']

def gen_from_ms(arg, value):
    '''
    Generic conversion from time (ms)
    '''
    assert arg in valid_args

    res = None
    if arg == 'epoch':
        res = ms_to_epoch(value)
    if arg == 'slot':
        res = ms_to_gslot(value)
    if arg == 'iso':
        res = ms_to_iso(value)
    if arg == 'ms':
        res = value
    return res

def gen_to_ms(init_type, value):
    '''
    Converts the `value` of type `init_type` to ms
    '''
    assert init_type in valid_cmds
    res = value
    if init_type != 'ms':
        if init_type == "epoch":
            assert value[0] and value[1]
            res = epoch_slot_to_ms(value)
        if init_type == "iso":
            assert value[0]
            res = iso_to_ms(value)
        if init_type == "slot":
            assert value[0]
            res = gslot_to_ms(value)
    return res

def handlers(args) -> "list[str]":
    '''
    The to-be-dispatched handlers for `args`
    '''
    res = []
    for arg in args.keys():
        if arg not in {'input', 'type'}:
            if args[arg]:
                res.append(arg)
    return res

def dispatch(args):
    '''
    Maps `gen_dispatch` over appropriate handlers

    # TODO returning [None]
    '''
    arg_t = args["type"]
    input = args["input"]
    # single value (only [0]) for everything except
    # `epoch` which has two values ([0] and [1])

    hdlrs = handlers(args)
    input_ms = gen_to_ms(arg_t, input)
    f = lambda h: gen_from_ms(h, input_ms)
    res = list(map(f, hdlrs))

    if not res:
        print("no options selected")
    print(f"arg_t: {arg_t}")
    print(f"input: {input}")
    print(f"hdlrs: {hdlrs}")
    print(res)
    return res

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # epoch - expand Mina epoch number
    # slot  - expand Mina global slot number
    # iso   - convert iso 8601 date/time to Mina time
    # tick  - convert ms to Mina time
    parser = argparse.ArgumentParser(description="Mina Time Travel Utility - so you don't have to 😎")
    parser.add_argument("-t", "--type", choices=['epoch', 'slot', 'iso', 'ms'], default='iso', help="input type")

    parser.add_argument("-e",  action="store_true", help="convert to Mina epoch number")
    parser.add_argument("-es", action="store_true", help="convert to Mina current epoch slot number")
    parser.add_argument("-gs", action="store_true", help="convert to Mina global slot number")
    parser.add_argument("-i",  action="store_true", help="convert to iso 8601")
    parser.add_argument("-ms", action="store_true", help="convert to ms")
    parser.add_argument("input", type=str, nargs="+")

    # setup results
    epoch = None
    eslot = None
    gslot = None
    ticks = None
    iso   = None
    res   = { "e" : epoch, "es" : eslot, "gs" : gslot, "i" : iso, "ms" : ticks }

    # parse and handle args
    args = vars(parser.parse_args())
    print(dispatch(args))
    # TODO

#############
# resources #
#############
#
# - [Mina time machine](https://towerstake.com/mina-time-machine/)
