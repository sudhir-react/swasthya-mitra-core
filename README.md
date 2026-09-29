# Swasthya Mitra Core Engine (Day 26 Operational Stack)

An enterprise-grade, high-performance Asynchronous REST API infrastructure seamlessly integrated with indexed relational disk storage and automated robust web scraping frameworks. Engineered to handle secure, high-traffic medical dataset querying with absolute runtime efficiency.

## 🚀 Key Architectural Layout Features

- **Asynchronous REST Routing:** Engineered using **FastAPI** and **Uvicorn** to run microsecond-level non-blocking event loops across Python 3.14 runtime boundaries.
- **Relational Storage Matrix:** Moving away from volatile memory arrays into persistent local disk operations utilizing **SQLite3** (`health_registry.db`).
- **Logarithmic Search Acceleration:** Implemented a binary **B-Tree Search Index** (`idx_doctors_search`) lowering query traversal complexities directly to **O(log N)**.
- **HTTP Telemetry Middleware:** Embedded a non-blocking request interceptor layer tracking client footprint telemetry (IP, Method, Path) without choking throughput.
- **Robust Scraper Infrastructure:** Outfitted with a class-based, secure context manager automation engine (`robust_oop_scraper.py`) built to evade advanced anti-bot firewalls via organic user-agent transformations.

---

## 📊 Live Performance Benchmarks (Load Tested)

Under a simultaneous load stress simulation injecting 50 parallel client network requests at the exact same millisecond:

- **Total Stress Test Traversal Time:** `1170.99 ms`
- **Average Throttle Speed Per Unit:** `23.42 ms`
- **Packet Loss / Drop Frames:** `0%` (100% Load Integrity Verified)

---

## 🛠️ Execution & Deployment Guide

### 1. Initialize Relational Storage Vault

```bash
python database_builder.py
```

### 2. Boot Up High-Speed Asynchronous API Server

```bash
python -m uvicorn medical_api_server:app --reload --ws none
```

The server will boot locally and actively listen at: `http://localhost:8000/docs`

### 3. Launch Concurrency Load Test Suite

```bash
python stress_test_engine.py
```

### 4. Run Secure Object-Oriented Automation Scraper

```bash
python robust_oop_scraper.py
```

---

## 🔒 Security & Confidentiality Framework

All telemetry elements, dynamic cookies, and cached viewports are automatically flushed out of local memory boundaries upon system teardown inside strict resource containment pools via Python's native `__exit__` hooks, guaranteeing 100% process privacy.
