#wite aprogram to simulate a basic stack and queue using a list. 
# provide options to push, pop(Stack) enqueue, dequeeu(queue)
list = []
n = int(input("Enter the number of elements you want to add to the stack/queue: "))
for i in range(n):
    element = input("Enter an element to add to the stack/queue: ")
    list.append(element)
print("Current Stack/Queue:", list)
while True:
    choice = input("Choose an operation - (1) Push (2) Pop (3) Enqueue (4) Dequeue (5) Exit: ")
    
    if choice == '1':  # Push
        element = input("Enter an element to push onto the stack: ")
        list.append(element)
        print("Stack after push:", list)
   
    elif choice == '2':  # Pop
        if list:
            popped_element = list.pop()
            print(f"Popped element: {popped_element}")
            print("Stack after pop:", list)
        else:
            print("Stack is empty, cannot pop.")
            
    elif choice == '3':  # Enqueue
        element = input("Enter an element to enqueue into the queue: ")
        list.append(element)
        print("Queue after enqueue:", list)
        
    elif choice == '4':  # Dequeue
        if list:
            dequeued_element = list.pop(0)
            print(f"Dequeued element: {dequeued_element}")
            print("Queue after dequeue:", list)
        else:
            print("Queue is empty, cannot dequeue.")
            
    elif choice == '5':  # Exit
        print("Exiting the program.")
        break
        
    else:
        print("Invalid choice, please try again.")