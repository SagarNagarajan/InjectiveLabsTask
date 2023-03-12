# Q1. 

To solve the first question, I have used the following approach: 

a) Parallelize the process method in the LimitOrderBook class with synchronization. This is done using a combination of multithreading and synchronization primitives such as Lock and Condition.

b) Modify the LimitOrderBook class to add a new process_lock attribute that will be used to synchronize access to the order book.

c) Modify the process method in the LimitOrderBook class to use the process_lock to synchronize access to the order book.

d) Create a new ParallelLimitOrderBook class that inherits from the original OrderBook class and adds multithreading to parallelize the processing of orders.

e) This new class adds several new attributes:

*num_threads*: the number of parallel threads to use.
_threads_: a list of the Thread objects that will be used to run each parallel thread.
_orders_queue_: a Condition object that will be used to synchronize access to the orders list.
_process_orders_: a new method that will be used to process orders in parallel using multithreading.
_process_order_book_: a modified version of the original process_order_book method that now uses multithreading to process orders in parallel.

f) The process_orders method processes a list of orders using a Condition object to synchronize access to the orders list. Each thread in the pool will call this method with a chunk of orders to process.

g) The process_order_book method divides the list of orders into chunks and starts a new thread for each chunk. Once all threads are done, it returns the updated order book.

## Performance

To compare the performance of running the processes sequentially vs running them in parallel, we define another function: orderbook_tests_parallel.py. In this function, we create a ParallelLimitOrderBook and add 100 randomly generated orders to it. In the orderbook_tests.py we create a LimitOrderBook and add 100 randomly generated orders to it. We then process these orders sequentially. The number of orders to be generated is passed as a command line argument. 

a) With sequential processing the orders take around 0.5986554718017578 ms to process while with parallel processing the orders take 0.6055831909179688 ms to process. The parallel process takes slightly longer for the following reasons:

To maintain the consistency of the orderbook we lock the entire book before passing it to a process. This means that only one of the threads can make changes to the orderbook at one time. And since in our operation, almost every instruction involves writing to the orderbook, multiple threads cannot make changes to the orderbook at the same time. Also, locking the thread involves the execution of additional instructions which slighlty increases the time. Potential improvements to be made would be to improve the code or data structures in such a way so as to have any/all read instructions in one function so that multiple threads can read from it at one time. This would help leverage the benefits of parallel processing in a significant manner making it a multi-reader single writer problem.

