Task 1: 
It is by default that Django signals are executed synchronously. 
In the code below the "Step 1" will will be be printed first. Then, due to pre_save "Step 2" will be printed by the signal handler.
After this finally "Step 3" will be printed by the caller.

Task 2:
Yes, the Django signals run in the same thread as the caller by default.
In this code the output will give ID for the threads being run by the signal handler and caller.
Both the IDs will be same which shows that same thread is being run by signal and caller.

Task 3:
Yes, Django signals run in the same database transaction as the caller.
In the code below a signal is used to modify an attribute of a model.
Then it is verified that the change is applied in the same transaction as the save operation.

Task 4:
A list is used to store the attributes and iterate through it using Python's built-in iter() function.
iter() function is used to stop iteration automatically.
