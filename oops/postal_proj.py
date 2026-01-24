import requests

# --- 1. THE MODEL: Represents a single real-world object ---
class PostOffice:
    def __init__(self, data):
        self.name = data.get('Name', 'N/A')
        self.branch_type = data.get('BranchType', 'N/A')
        self.delivery_status = data.get('DeliveryStatus', 'N/A')
        self.district = data.get('District', 'N/A')
        self.state = data.get('State', 'N/A')
        self.pincode = data.get('Pincode', 'N/A')

    def to_row_string(self):
        """Formats the object data for the table row."""
        return (f"{self.name:<30} | {self.branch_type:<15} | "
                f"{self.delivery_status:<15} | {self.district:<15} | "
                f"{self.state:<15} | {self.pincode:<10}")


# --- 2. THE SERVICE: Handles the "Business Logic" (API) ---
class PostalService:
    BASE_URL = "https://api.postalpincode.in"

    def fetch_offices(self, search_term, search_by_pincode=True):
        endpoint = "pincode" if search_by_pincode else "postoffice"
        url = f"{self.BASE_URL}/{endpoint}/{search_term}"

        try:
            response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
            response.raise_for_status()
            data = response.json()

            # LOGICAL ERROR CHECK: Did the API find results?
            if not data or data[0]["Status"] != "Success":
                return [] # Return empty list, don't crash

            # Convert raw JSON dicts into PostOffice Objects
            raw_offices = data[0].get("PostOffice", [])
            # Only return valid objects (sometimes API returns None for the list)
            if raw_offices is None: 
                return []
                
            return [PostOffice(item) for item in raw_offices]

        except requests.exceptions.RequestException as e:
            print(f"Network Error: {e}")
            return []


# --- 3. THE CONTROLLER/UI: Handles User Interaction ---
# This is NOT a class. It's the application flow.
def main():
    service = PostalService()
    
    print("\n--- Indian Postal Service Search ---")
    choice = input("Search by:\n1. Pincode\n2. Area Name\nEnter 1 or 2: ")

    search_term = ""
    is_pincode = True

    if choice == '1':
        search_term = input("Enter Pincode: ")
        is_pincode = True
    elif choice == '2':
        search_term = input("Enter Area Name: ")
        is_pincode = False
    else:
        print("Invalid choice!")
        return

    print("\nFetching data... please wait.")
    results = service.fetch_offices(search_term, is_pincode)

    if not results:
        print(f"No records found for '{search_term}'.")
    else:
        # HEADER
        header = (f"{'OFFICE NAME':<30} | {'BRANCH TYPE':<15} | "
                  f"{'DELIVERY':<15} | {'DISTRICT':<15} | "
                  f"{'STATE':<15} | {'PINCODE':<10}")
        print("-" * len(header))
        print(header)
        print("-" * len(header))

        # DATA ROWS
        for office in results:
            print(office.to_row_string())
        print("-" * len(header))

if __name__ == "__main__":
    main()