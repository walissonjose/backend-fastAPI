from fastapi import FastAPI
import uvicorn

from config.server import port
from controllers import routes


app = FastAPI(
    title='Hello layered-FastAPI using SQLAlchemy',
    version='0.0.1',
)

for router in routes:
    app.include_router(router)

if __name__ == '__main__':
    uvicorn.run('main:app', host='localhost', port=port, reload=True)
