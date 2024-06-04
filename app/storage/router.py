from fastapi import APIRouter


router = APIRouter()


@router.get("/traces/all")
async def get_all_traces():
    return {"message": "Hello World"}


@router.get("/traces/{ip}")
async def get_trace(trace_ip):
    return {"message": f"trace for {trace_ip}"}