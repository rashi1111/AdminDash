import React, { useState } from "react";
import axios from "axios";

function UploadComponent({ fetchUsers }) {
  const [message, setMessage] = useState("");

  const handleUpload = async (e) => {
    const file = e.target.files[0];
    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await axios.post("http://localhost:8000/upload-excel/", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      setMessage(res.data.message);
      fetchUsers();
    } catch (err) {
      if (err.response?.data?.detail) {
        setMessage(Array.isArray(err.response.data.detail) ? err.response.data.detail.join(" | ") : err.response.data.detail);
      } else {
        setMessage("Upload failed.");
      }
    }
  };

  return (
    <div>
      <input type="file" accept=".xlsx" onChange={handleUpload} />
      <div>{message}</div>
    </div>
  );
}

export default UploadComponent;