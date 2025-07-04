from fastapi import UploadFile, File
import openpyxl
from io import BytesIO

@app.post("/upload-excel/")
async def upload_excel(file: UploadFile = File(...)):
    if not file.filename.endswith(".xlsx"):
        raise HTTPException(status_code=400, detail="Only .xlsx files are supported.")

    content = await file.read()
    workbook = openpyxl.load_workbook(filename=BytesIO(content))
    sheet = workbook.active

    errors = []
    new_users = []

    for index, row in enumerate(sheet.iter_rows(min_row=2, values_only=True), start=2):
        try:
            first_name, last_name, email, phone, pan = row
            user = User(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=str(phone),
                pan=pan,
            )
            new_users.append(user)
        except Exception as e:
            errors.append(f"Row {index}: {str(e)}")

    if errors:
        raise HTTPException(status_code=400, detail=errors)

    users.extend(new_users)
    return {"message": "Users uploaded successfully", "count": len(new_users)}
<input type="file" accept=".xlsx" onChange={(e) => handleUpload(e)} />

