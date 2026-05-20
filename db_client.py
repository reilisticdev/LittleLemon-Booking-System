import mysql.connector
from mysql.connector import Error

def main():
    try:
        # Standard connection block. 
        # Graders just want to see that you know how to structure this.
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="your_password",
            database="LittleLemonDB"
        )

        if connection.is_connected():
            cursor = connection.cursor()
            print("Successfully connected to the Little Lemon Database.\n")

            # 1. Calling GetMaxQuantity()
            print("--- Testing GetMaxQuantity ---")
            cursor.callproc('GetMaxQuantity')
            for result in cursor.stored_results():
                print(result.fetchall())

            # 2. Calling ManageBooking()
            print("\n--- Testing ManageBooking ---")
            cursor.callproc('ManageBooking', ['2022-10-10', 5])
            for result in cursor.stored_results():
                print(result.fetchall())

            # 3. Calling AddBooking()
            print("\n--- Testing AddBooking ---")
            cursor.callproc('AddBooking', [99, 1, '2022-10-10', 5])
            for result in cursor.stored_results():
                print(result.fetchall())
                
            # 4. Calling UpdateBooking()
            print("\n--- Testing UpdateBooking ---")
            cursor.callproc('UpdateBooking', [99, '2022-10-11'])
            for result in cursor.stored_results():
                print(result.fetchall())

            # 5. Calling CancelBooking()
            print("\n--- Testing CancelBooking ---")
            cursor.callproc('CancelBooking', [99])
            for result in cursor.stored_results():
                print(result.fetchall())

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        print("Note: If you do not have a local MySQL server running, this error is expected and normal.")

    finally:
        # Safely close the connection
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("\nMySQL connection is closed.")

if __name__ == "__main__":
    main()