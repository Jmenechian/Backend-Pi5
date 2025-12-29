# Backend-Pi5
Backend: API to control GPIO Pins from personal Raspberry Pi

```bash
python -m uvicorn main:app --reload
```

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```


## Installation
```bash
pip install "fastapi[standard]"

pip install fastapi uvicorn[standard]
```