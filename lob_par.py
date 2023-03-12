class ParallelOrderBook(LimitOrderBook):
    def __init__(self, *args, num_threads=4, **kwargs):
        super().__init__(*args, **kwargs)
        self.num_threads = num_threads
        self.threads = []
        self.orders_queue = th.Condition()

    def process_orders(self, orders):
        with self.orders_queue:
            for order in orders:
                self.orders_queue.notify()
                self.orders_queue.wait()
                self.process(order)
            self.orders_queue.notify_all()

    def process_order_book(self, orders):
        chunk_size = (len(orders) + self.num_threads - 1) // self.num_threads
        chunks = [orders[i:i+chunk_size] for i in range(0, len(orders), chunk_size)]
        for i in range(self.num_threads):
            t = th.Thread(target=self.process_orders, args=(chunks[i],))
            t.start()
            self.threads.append(t)
        for t in self.threads:
            t.join()
