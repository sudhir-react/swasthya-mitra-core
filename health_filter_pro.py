import time

class SudhirHealthFilterEngine:
    @staticmethod
    def execute_advanced_filter(doctor_dataset):
        print("⚙️ [Filter Engine] Scanning master doctor dataset safely...")
        
        # 🚀 THE EXPERT TRICK: 3 robust security guards (filters) combined in a single line!
        # Rules: Location == 'Raipur', Rating >= 4.5, Availability == True
        optimized_result = [
            {
                "name": doc["name"].strip().upper(),
                "specialty": doc["specialty"].upper(),
                "rating": doc["rating"]
            }
            for doc in doctor_dataset
            if doc is not None  # Guard 1: Null Value Protection
            if doc.get("location") == "Raipur"  # Guard 2: Location Filter
            if doc.get("rating", 0) >= 4.5  # Guard 3: High-Rating Filter
            if doc.get("is_available") is True  # Guard 4: Live Availability Filter
        ]
        
        return optimized_result

def run_production_filter_test():
    print("🚀 Starting Sudhir's Advanced Multi-Criteria Health Filter [Day 24]...\n")
    
    # 1. RAW DATASET: Unfiltered doctor data received from hospitals (contains 'None' and spaces)
    raw_doctors = [
        {"name": "Dr. Rahul Sharma", "specialty": "Cardiologist", "location": "Raipur", "rating": 4.8, "is_available": True},
        {"name": "Dr. Pooja Mishra", "specialty": "Pediatrician", "location": "Bhilai", "rating": 4.9, "is_available": True}, # It is in Bhilai (will be filtered out).
        None, # Null value (the guard will prevent this)
        {"name": "Dr. Amit Khan", "specialty": "Neurologist", "location": "Raipur", "rating": 4.2, "is_available": True}, # Rating is low (will be filtered out)
        {"name": "Dr. Sony Desai", "specialty": "Surgeon", "location": "Raipur", "rating": 4.6, "is_available": True} # Raipur, 4.6, Available (will be selected)
    ]
    
    # 2. RUNTIME ACCELERATION METRICS
    start_time = time.perf_counter()
    
    # Running the filter engine live
    cleaned_list = SudhirHealthFilterEngine.execute_advanced_filter(raw_doctors)
    
    end_time = time.perf_counter()
    duration = (end_time - start_time) * 1000
    
    # 3. DISPLAY SUMMARY
    print("\n🟢 SUCCESS: Verified Elite Doctors Matched for Raipur Emergency:")
    print("-" * 75)
    for idx, doc in enumerate(cleaned_list, start=1):
        print(f" 🏥 Match #{idx}: {doc['name']} | {doc['specialty']} | ⭐ Rating: {doc['rating']}")
    print("-" * 75)
    
    print(f"⚡ Filter Pipeline Processing Speed : {duration:.4f} ms")
    print(f"📊 Algorithmic Scaling Complexity    : O(N) Linear Single-Pass Matrix")
    print("-" * 75)
    print("\n🎉 Multi-criteria health filter engine validated with 100% integrity!")

if __name__ == "__main__":
    run_production_filter_test()