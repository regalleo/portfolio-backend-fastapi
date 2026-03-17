# Portfolio Backend - Database Data Feeding Task

## Steps to Complete:

### Step 1: Create seed script [✅ COMPLETED]
### Step 2: Update Docker Compose [✅ COMPLETED]
- File: `seed_data.py`
- Run: `cd portfolio_backend_fastapi && python seed_data.py`

### Step 2: Update Docker Compose [PENDING]
- File: `docker-compose.yml`
- Remove MongoDB service

### Step 3: Test Server [PENDING]
- Dev: `cd portfolio_backend_fastapi && ./run.sh`
- Visit: http://localhost:8080/docs

### Step 4: Feed Data [PENDING]  
- Option A: Use Swagger UI POST endpoints
- Option B: Run seed script
- Verify: `sqlite3 portfolio.db "SELECT COUNT(*) FROM projects;"`

### Step 5: Docker [PENDING]
- `docker-compose up --build`

## API Endpoints for Manual Data Entry:
- POST /api/about/
- POST /api/experience/
- POST /api/projects/
- POST /api/skills/
- POST /api/contact/ (form submissions)

