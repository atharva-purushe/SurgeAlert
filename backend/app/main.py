from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger

from app.api.routes_predict import router as predict_router
from app.api.routes_capacity import router as capacity_router
from app.api.routes_signals import router as signals_router   # ← ADD THIS
from app.api.routes_agents import router as agents_router
from app.api.routes_routerbot import router as routerbot_router
from app.core.scheduler import start_scheduler


def create_app() -> FastAPI:
    app = FastAPI(
        title="SurgeAlert Backend",
        description="Agentic AI for hospital surge prediction, capacity planning, and patient routing.",
        version="0.1.0",
    )

    # CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # ROUTES
    app.include_router(predict_router, prefix="/predict", tags=["Prediction"])
    app.include_router(capacity_router, prefix="/capacity", tags=["Capacity"])
    app.include_router(signals_router, prefix="/signals", tags=["Signals"])   # ← ADD THIS
    app.include_router(agents_router, prefix="/agents", tags=["Agents"])
    app.include_router(routerbot_router, prefix="/routerbot", tags=["RouterBot"])

    # health route
    @app.get("/", tags=["Health"])
    def root():
        return {
            "status": "ok",
            "service": "SurgeAlert Backend",
            "message": "Backend is running 🚑",
        }

    # scheduler
    @app.on_event("startup")
    def on_startup():
        logger.info("🚀 Starting SurgeAlert backend...")
        try:
            start_scheduler()
            logger.info("⏱️ Scheduler started.")
        except Exception as e:
            logger.error(f"Scheduler failed: {e}")

    @app.on_event("shutdown")
    def on_shutdown():
        logger.info("🛑 Shutting down SurgeAlert backend...")

    return app


app = create_app()
