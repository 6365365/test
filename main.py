import uvicorn
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from app.route.phones import phones_route
# from app.exception import NotFoundException


def create_app() -> FastAPI:
    app = FastAPI(title="Test Project")

    app.include_router(router=phones_route, prefix='/api/v1/phones', tags=["phones"])

    # @app.exception_handler(NotFoundException)
    # async def not_found_exception_handler(
    #         request: Request,
    #         exc: NotFoundException,
    #         status: status = status.HTTP_404_NOT_FOUND):
    #     status_code = status
    #     content = exc.__dict__['name']
    #     return JSONResponse(
    #         status_code=status_code,
    #         content=content,
    #     )

    return app


if __name__ == "__main__":
    uvicorn.run("main:create_app", port=8000,
                host="0.0.0.0", reload=True, factory=True)