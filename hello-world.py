from havoc import Demon, RegisterCommand

def hello_world( demonID, *params ):
    TaskID : str    = None
    demon  : Demon  = None
    # create an instance of the argument packer
    packer = Packer()
    # get an instance of the demon
    demon  = Demon(demonID)

    # create a task ID  
    TaskID = demon.ConsoleWrite( demon.CONSOLE_TASK, f"Tasked demon to execute Hello World BOF" )

    # instruct Havoc to run a BOF with certain parameters
    demon.InlineExecute( TaskID, "go", f"hello-world.o", packer.getbuffer(), False )

    # return the new task ID
    return TaskID
    
RegisterCommand( hello_world, "", "hello-world", "Prints a simple message.", 0, "Usage: hello-world", "Example: hello-world" )
