from func_connections import connect_dydx

# MAIN FUNCTION
if __name__ == "__main__":
    print ("hello bot")
    
     # Connect to client
try:
    print("Connecting to Client...")
    client = connect_dydx()
except Exception as e:
    print("Error connecting to client: ", e)
   # send_message(f"Failed to connect to client {e}")
    exit(1)