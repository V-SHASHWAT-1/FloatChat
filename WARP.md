# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

FloatChat is an AI-powered ARGO ocean data platform featuring:
- **Backend**: FastAPI with SQLAlchemy ORM, PostgreSQL/SQLite database
- **Frontend**: React 18 + TypeScript + Tailwind CSS + Vite
- **AI/ML**: RAG (Retrieval-Augmented Generation) system with vector database
- **Real-time**: WebSocket chat and live data streaming
- **Visualization**: Interactive maps (Leaflet), charts (Recharts), and data analytics

## Development Commands

### Quick Setup (Recommended)
```bash
# 1. Setup environment and dependencies
python simple_setup.py

# 2. Load sample data
python load_data.py

# 3. Start backend
python start_backend.py

# 4. Start frontend (new terminal)
cd frontend/web
npm install
npm run dev
```

### Docker Development
```bash
# Full stack with PostgreSQL
docker-compose up -d

# Production deployment
docker-compose -f docker-compose.prod.yml up -d
```

### Backend Development
```bash
cd backend

# Install dependencies
pip install -r requirements.txt

# Enhanced setup (includes all AI features)
pip install -r requirements_enhanced.txt

# Start with hot reload
python start_backend.py
# OR
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Initialize database
python -c "from app.cli_init_db import init_db; init_db()"
```

### Frontend Development
```bash
cd frontend/web

# Install dependencies
npm install

# Development server
npm run dev

# Production build
npm run build

# Preview production build
npm run preview
```

### Testing
```bash
# System integration test
python test_system.py

# API endpoint testing
python test_backend.py

# Chat API testing
python test_chat_api.py

# Frontend testing
cd frontend/web
npm test
```

## Architecture & Code Structure

### Backend Architecture (FastAPI)
- **Entry Point**: `backend/app/main.py` - FastAPI application with CORS, routers, and WebSocket endpoints
- **Database**: `backend/app/models.py` - SQLAlchemy models for ARGO profile data
- **API Routes**: 
  - `backend/app/routers.py` - Chat and AI routes
  - `backend/app/routes_data.py` - Data CRUD operations
  - `backend/app/routes_argo.py` - ARGO-specific endpoints
- **AI/RAG**: `backend/app/rag.py` - Retrieval-Augmented Generation system
- **Real-time**: `backend/app/realtime.py` - WebSocket connection management
- **Analytics**: `backend/app/analytics.py` - Statistical analysis engine

### Frontend Architecture (React + TypeScript)
- **Entry Point**: `frontend/web/src/main.tsx` → `App.tsx`
- **Main Components**:
  - `ChatInterface.tsx` - AI-powered chat with ARGO data insights
  - `MapVisualization.tsx` - Interactive maps with float locations
  - `DataVisualization.tsx` - Charts and data analytics
  - `InsertData.tsx` - Data insertion interface
- **Layout**: `components/Layout/` - Header, Sidebar navigation
- **UI Library**: `components/ui/` - Reusable components (Button, Card, Input, Badge)

### Key Data Models
```python
# backend/app/models.py
class Profile(Base):
    __tablename__ = 'profiles'
    
    id = Column(Integer, primary_key=True, index=True)
    float_id = Column(String, index=True)
    latitude = Column(Float, index=True) 
    longitude = Column(Float, index=True)
    depth = Column(Float)
    temperature = Column(Float)
    salinity = Column(Float)
    month = Column(Integer, index=True)
    year = Column(Integer, index=True)
    date = Column(Date, nullable=True)
```

## API Endpoints Structure

### Core Data API
- `GET /data/profiles` - Retrieve profiles with filtering
- `GET /data/stats` - Database statistics
- `POST /data/profile` - Insert new profile
- `GET /data/export` - Export data in various formats

### AI Chat API
- `POST /chat/query` - Natural language queries
- `GET /chat/suggestions` - Query suggestions
- `WebSocket /chat/stream` - Real-time chat
- `POST /rag/query` - RAG-enhanced queries

### WebSocket Endpoints
- `/ws/data-stream` - Real-time data updates
- `/ws/analytics` - Live analytics
- `/ws/alerts` - System alerts
- `/ws/chat` - Chat interface

## Environment Configuration

### Required Environment Variables
```bash
# Database
DATABASE_URL=sqlite:///./floatchat.db  # or PostgreSQL URL
DB_TYPE=sqlite

# API Configuration
API_HOST=0.0.0.0
API_PORT=8000
SECRET_KEY=your-secret-key-here

# AI/LLM Integration (optional but recommended)
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
COHERE_API_KEY=your_cohere_api_key_here

# Vector Database
VECTOR_DB_PATH=./data/vector_db
EMBEDDING_MODEL=all-MiniLM-L6-v2

# Frontend
VITE_API_URL=http://localhost:8000
```

## Development Workflow

### Making Changes to Backend
1. **Models**: Update `backend/app/models.py` for database schema changes
2. **API Routes**: Add endpoints in appropriate router files
3. **Business Logic**: Implement in service files or main route handlers
4. **Database**: Use `python -c "from app.cli_init_db import init_db; init_db()"` to reinitialize

### Making Changes to Frontend
1. **Components**: Add/modify in `frontend/web/src/components/`
2. **Routing**: Update navigation in `App.tsx` and `Layout/Sidebar.tsx`
3. **Styling**: Use Tailwind CSS classes, global styles in `index.css`
4. **API Integration**: Update API calls to match backend endpoints

### Real-time Features
- Use WebSocket connections defined in `backend/app/main.py`
- Connection management handled by `backend/app/realtime.py`
- Frontend components can subscribe to real-time updates

### AI/RAG System
- Knowledge base stored in `backend/app/rag.py`
- Natural language processing for oceanographic queries
- Context-aware responses with ARGO float domain knowledge

## Data Flow

1. **Data Ingestion**: Sample data loaded via `load_data.py` or uploaded through API
2. **Database Storage**: Profiles stored in SQLite/PostgreSQL with spatial indexing
3. **API Layer**: FastAPI serves data with filtering, pagination, and export
4. **Frontend Display**: React components visualize data with maps and charts
5. **AI Processing**: RAG system provides intelligent responses to user queries

## Service Access Points

### Development URLs
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **Frontend Web App**: http://localhost:5173
- **Streamlit Dashboard**: http://localhost:8501 (if using Docker)

### Production Considerations
- Use PostgreSQL with PostGIS for spatial operations
- Configure proper CORS origins
- Set up SSL/TLS certificates
- Use production-grade ASGI server (gunicorn + uvicorn)
- Implement rate limiting and authentication

## Sample Data

The repository includes 25 realistic ARGO profiles covering:
- Global ocean regions (Arctic, Atlantic, Pacific, Indian, Southern)
- Realistic temperature-salinity relationships
- Quality control flags and validation
- Time series data (April 2024 - March 2025)

Access sample data through API or directly query the profiles table.