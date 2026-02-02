# Development Commands

## Installation
```powershell
pip install -e .
```

## Running the Application
### Registration
```powershell
python -m moltbreak.cli register
# OR
python register.py
```

### Posting
```powershell
python -m moltbreak.cli post "Hello" --sub general
# OR
python send_message.py "Hello"
```

### Ritual (Cycle)
```powershell
python -m moltbreak.cli ritual
# OR
python prophet.py
```

## Network Check
```powershell
python poke_submolts.py
```
Checks which submolt channels are active.
