import os
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    # 模拟读取环境变量，如果没有配置，则使用默认值
    app_env = os.getenv("APP_ENV", "development")
    db_host = os.getenv("DB_HOST", "localhost (default)")

    return {
        "message": "MVP Application is running!",
        "environment": app_env,
        "database_host": db_host,
    }
