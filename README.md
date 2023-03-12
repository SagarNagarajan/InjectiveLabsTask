# Q1. 

To solve the first question, I have used the following approach: 

a) Parallelize the process method in the LimitOrderBook class with synchronization. This is done using a combination of multithreading and synchronization primitives such as Lock and Condition.

b) Modify the LimitOrderBook class to add a new process_lock attribute that will be used to synchronize access to the order book.

c) Modify the process method in the LimitOrderBook class to use the process_lock to synchronize access to the order book.

d) Create a new ParallelLimitOrderBook class that inherits from the original OrderBook class and adds multithreading to parallelize the processing of orders.

e) This new class adds several new attributes:

_num_threads_: the number of parallel threads to use.

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

# Q2

The equation shown is a partial differential equation that describes the dynamics of a system. Specifically, it describes the time evolution of three functions C(t), E(t), and F(t) that depend on time t.

One approach to solve this differential equation numerically is to use numerical methods to discretize the equation and solve it iteratively. Discretization involves breaking the continuous equation into a set of smaller, discrete equations that approximate the behavior of the original equation over smaller time intervals. The general idea is to convert the continuous differential equation into a set of discrete equations that can be solved numerically. In this approach, the continuous time variable is divided into discrete time steps, and the differential equation is approximated using difference equations. The solution is then obtained by iteratively solving the set of difference equations using numerical methods until the solution converges to a stable solution. 

There are several numerical methods that can be used for this purpose, including finite difference methods and finite element methods:

a) The finite difference method is a common numerical method used for solving partial differential equations (PDEs). It involves approximating the derivatives in the PDE using difference equations, which are equations that describe the rate of change of a quantity in terms of the difference between values at neighboring points in space or time. To apply the finite difference method, the domain of the PDE is discretized into a grid of points, with the derivative at each point approximated using the values of the function at neighboring points. This approximation results in a system of linear equations that can be solved using matrix algebra. In particular, the finite difference method involves using a set of finite difference approximations for the partial derivatives in the PDE. For example, the first-order derivative with respect to time can be approximated using the forward difference formula:

df/dt ≈ (f(t+Δt) - f(t)) / Δt, where Δt is the time step size. 

Similarly, the second-order derivative with respect to space can be approximated using the central difference formula:

d^2f/dx^2 ≈ (f(x+Δx) - 2f(x) + f(x-Δx)) / Δx^2, where Δx is the spacing between adjacent grid points.

Using these finite difference approximations, the original PDE is converted into a system of linear equations, which can be solved using matrix algebra. The resulting numerical solution provides an approximation to the solution of the original PDE at each grid point in the domain. 

b) The finite element method (FEM) is another numerical method commonly used for solving partial differential equations (PDEs). Unlike the finite difference method, which approximates the solution on a grid of points, the finite element method divides the domain of the PDE into a mesh of smaller, finite elements.

The basic idea of the finite element method is to represent the solution of the PDE as a weighted sum of basis functions, defined over each element in the mesh. The solution is then approximated by solving a set of linear equations for the coefficients of these basis functions. The process of determining these coefficients involves imposing boundary conditions, which specify the behavior of the solution at the edges of the domain.

The finite element method is particularly useful for problems with complex geometries, as it allows for the domain to be divided into irregular shapes, which can be combined to approximate the solution over the entire domain. Additionally, the finite element method can handle a wide range of boundary conditions, including those that are not easily represented on a regular grid.

In practice, the finite element method involves several steps, including mesh generation, element assembly, and solution of the resulting linear equations. These steps can be computationally expensive for large or complex problems, but modern software packages and hardware make it possible to solve even very complex problems using the finite element method.

## Possible softwares:

### Matlab: 

MATLAB offers built-in functions such as "pdepe" and "pde toolbox" for solving PDEs using finite difference and finite element methods respectively. These functions are designed to handle a wide range of problems, including problems with complex geometries and boundary conditions. Additionally, MATLAB provides tools for visualizing the solutions of PDEs, making it easy to analyze and interpret the results of a simulation.

The "pdepe" function in MATLAB is used for solving PDEs with initial and boundary conditions using the method of lines. This function discretizes the PDE using finite difference approximations, and then solves the resulting system of ordinary differential equations (ODEs) using a stiff ODE solver. This approach is particularly useful for problems with simple geometries and regular grids.

On the other hand, the "pde toolbox" in MATLAB is used for solving PDEs using the finite element method. This toolbox provides a range of functions for generating meshes, specifying boundary conditions, and solving the resulting system of linear equations. The toolbox also includes tools for visualizing the results of a simulation, such as contour plots and animations.

### Python:

Python has several libraries for solving partial differential equations such as NumPy, SciPy, and FEniCS.

NumPy can be used for solving PDEs using various numerical methods, such as finite difference method (FDM) and finite element method (FEM). To solve a PDE using FDM with NumPy, we first need to discretize the problem domain into a grid of discrete points. We then approximate the derivatives in the PDE using finite difference approximations, and create a system of equations that can be solved using linear algebra. NumPy provides functions such as numpy.gradient for calculating numerical derivatives and numpy.linalg.solve for solving linear equations.

To solve PDEs using Scipy, we first need to define the problem domain and discretize it into a grid of discrete points. We then approximate the derivatives in the PDE using finite difference or finite element approximations, and create a system of equations that can be solved using linear algebra. Scipy provides functions such as scipy.sparse.linalg.spsolve for solving sparse linear systems efficiently. Scipy also includes a submodule called scipy.integrate that provides functions for solving initial value problems (IVPs) and boundary value problems (BVPs) of ordinary differential equations (ODEs) and PDEs. The scipy.integrate.solve_ivp function can be used to solve IVPs, while the scipy.integrate.solve_bvp function can be used to solve BVPs. These functions use advanced numerical algorithms such as adaptive time-stepping and shooting methods to solve the problems efficiently and accurately. In addition, Scipy also provides specialized functions for solving specific types of PDEs, such as the scipy.special.erfc function for solving the diffusion equation with an error function boundary condition, and the scipy.special.airy function for solving the Airy equation.

To use FEniCS, one first needs to define the PDE and its boundary conditions using its high-level language syntax. This involves defining the weak form of the PDE, which is a variation of the original PDE that is written in terms of integrals over the domain. FEniCS then automatically generates the finite element discretization of the weak form, which can be solved using standard numerical methods.