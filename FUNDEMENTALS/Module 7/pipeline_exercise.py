def take(count, iterable):
    """
    Take first count of elements .

    Args:
        count: which item to stop at
        iterable: the collection to iterate through
    Yields:
        yields item every iteration until returned
    Returns:
        empty return when count is reached
    """
    # - take is then run until it encounters a yield, to which it then pauses
    # - it ends on the forth iteration because now the counter is at 3 and instead of yielding another value
    # it has an empty return to terminate the generators execution
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


def run_take():
    """
    Runs the take function.
    Uses a for loop to print all iterations yielded.
    Prints stop at count number specified (count, iterable)
    """
    # pass the string "stopSumTime" to take generator to iterate over every character
    # with the count of 3 to stop after the 3rd character is taken
    # the for loop requests an iteration from take, giving control over to take -
    # after getting value from generator it is then used in the for block of code
    # it then repeats these steps until the 4th iteration -
    # once execution is terminated there are no more values to be requested
    # the for loop has nothing to iterate over therefore terminating itself, (the gen iterable ends - no more yields)
    for item in take(3, 'stopSumTime'):
        print(item)


def distinct(iterable):
    """
    Return unique items by eliminating duplicates.

    Args:
        iterable: the source collection
    Yield:
        unique item to string
    """
    # - a local set is created
    # the iterable is then iterated over for each item
    # each item is added to the local set - seen
    # if an item exists in set (already added) - this makes it not unique and the rest of the loop block is skipped
    # this is done with the continue keyword which skips the rest of the block and goes to next iteration
    # when the item is checked to be unique it is then yielded to outer loop
    # - when another request is made it first starts by adding the unique item from the previous iteration to seen set()
    # it then looks through the next iteration of the iterable
    # this showcases the pause - resume functionality because it stopped mid for loop block and
    # resumed, finished that block iteration and went to next, to then do the same and stop and resume
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)


def run_distinct():
    # pass the string "stopsumtime" to use with generator to iterate over every character
    # each iteration prints a unique character in order of string (no duplicates)
    # the for loop requested a value -
    # when a value is yielded back it is then printed
    # this is done it heads to the next request -
    # in this case this is done until iterable is completed
    for item in distinct("stopsumtime"):
        print(item)


def run_pipeline():
    # pass the string "stopsumtime" to get an iterable to the count input in take generator
    # then use yielded values from take to only return the unique ones from distinct
    # this evaluation follows starting with take to get the value -
    # - then to distinct to determine if it is unique (in distinct) -
    # then giving control back to outer loop to print
    # - this entirely runs until no more values are yielded from take (reached count) and return ends generator -
    # - this then leading to the end of distinct with no more values to yield leading to implicit return
    # this can be dont with take() using distinct as yields, will produce same output
    # this just instead checks for character uniqueness before sending it to distinct
    for item in distinct(take(9, "stopsumtime")):
        print(item)
    # probably more preferred way because a character un-unique character is stopped after first generator
    # in the one above all are sent to second generator distinct while in one below distinct only sends if character
    # is unique
    for item in take(9, distinct('stopsumtime')):
        print(f"dst-tak = {item}")
    # the advantages to these approaches are only the necessary values are requested instead of constructing
    # the full iterable
    # in a regular function the whole distinct set would have had to been constructed but instead it is only constructed
    # to the first 9 unique characters of the string to where is then ended because no more values are requested


if __name__ == '__main__':
    """Control Flow"""
    # run_take()
    run_pipeline()
