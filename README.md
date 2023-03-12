#Q1. 

To solve the first question, I have used the following approach: 

a) Parallelize the process method in the LimitOrderBook class with synchronization. This is done using a combination of multithreading and synchronization primitives such as Lock and Condition.

b) Modify the LimitOrderBook class to add a new process_lock attribute that will be used to synchronize access to the order book.

c) Modify the process method in the LimitOrderBook class to use the process_lock to synchronize access to the order book.

d) Create a new ParallelLimitOrderBook class that inherits from the original OrderBook class and adds multithreading to parallelize the processing of orders.

e) This new class adds several new attributes:

num_threads: the number of parallel threads to use.
threads: a list of the Thread objects that will be used to run each parallel thread.
orders_queue: a Condition object that will be used to synchronize access to the orders list.
process_orders: a new method that will be used to process orders in parallel using multithreading.
process_order_book: a modified version of the original process_order_book method that now uses multithreading to process orders in parallel.

f) The process_orders method processes a list of orders using a Condition object to synchronize access to the orders list. Each thread in the pool will call this method with a chunk of orders to process.

g) The process_order_book method divides the list of orders into chunks and starts a new thread for each chunk. Once all threads are done, it returns the updated order book.

##Performance
To compare the performance of running the processes sequentially vs running them in parallel, we define another function: orderbook_tests_parallel.py. In this function, we create a ParallelLimitOrderBook and add 100 randomly generated orders to it. In the orderbook_tests.py we create a LimitOrderBook and add 100 randomly generated orders to it. We then process these orders sequentially. The number of orders to be generated is passed as a command line argument. 